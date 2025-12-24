#!/usr/local/bin/python3
import os
import sys
# Assuming 'pikepdf' is what you intended to use, 
# since 'pikepdf' was the subject of your previous errors.
from pikepdf import Pdf


# helper function to list PDF files in a directory
def ls(contents):
    for index, pdf in enumerate(contents):
        print(index, ": ", pdf)


# modify PDF list based on type (exclude/include)
def modify(pdfs, type):
    pdf_selections = input(
        "\nEnter the PDF filenames which should be excluded/included from the list separated by a SPACE:\n> "
    ).split()

    # Use a set for quick lookups of valid selections
    valid_selections = set()

    # check if files exist and build the valid_selections set
    for selection in pdf_selections:
        if selection not in pdfs:
            print(
                f"\n❗️ '{selection}' does not exist in the current list! Skipping it...\n"
            )
        else:
            valid_selections.add(selection)
            if type == "exclude":
                print(f"\n❌ Excluding '{selection}' from the final list...")
            else:
                print(f"\n✅ Including '{selection}' in the final list...")

    # --- CORRECTED LOGIC ---
    if type == "exclude":
        # Create a new list containing only PDFs that were NOT selected for exclusion
        pdfs = [pdf for pdf in pdfs if pdf not in valid_selections]
    else:
        # Create a new list containing only PDFs that WERE selected for inclusion
        # This will discard all files not explicitly named by the user
        pdfs = [pdf for pdf in pdfs if pdf in valid_selections]

    # return modified list
    return pdfs


if __name__ == "__main__":
    merger = Pdf.new()

    # take directory location from command line argument (if given) else choose current directory as default
    if len(sys.argv[1:]) > 0:
        dir = sys.argv[1]
        if not os.path.isdir(dir):
            exit(f"Directory not found: {dir}")
        contents = os.listdir(dir)
    else:
        dir = os.getcwd()
        contents = os.listdir()

    print("\n\nContents of directory:\n")
    ls(contents)

    # Filter out non-PDFs and store all PDF filenames
    # Sorting logic applied to PDF files only
    pdf_contents = list(filter(lambda x: x.endswith(".pdf"), contents))
    
    # Sort PDFs by created time (os.path.getctime)
    sorted_contents = sorted(
        list(map(lambda x: os.path.join(dir, x), pdf_contents)), key=os.path.getctime
    )
    # Extract just the filename back from the full path
    pdfs = [os.path.basename(s) for s in sorted_contents]

    # start the loop similar to 'do-while' format:
    confirmation = "n"
    while confirmation not in ["y", "Y"]:
        if not pdfs:
            exit("No PDFs to merge... Exiting...")

        print("\nThe final list of PDFs to be merged: \n")
        ls(pdfs)

        # option to modify the list of PDFs
        confirmation = input(
            f"\nTotal: {len(pdfs)}\n\nCONTINUE? ['y'/'Y'] OR MODIFY THIS LIST? ['n'/'N']\n> "
        )

        # start merging final list
        if confirmation in ["y", "Y"]:
            file_name = input(
                "\nEnter the name of the final merged pdf (without the extension - 'pdf'):\n> "
            )

            # prevent user from adding '.pdf' at the end
            file_name = file_name.strip()
            while file_name.endswith(".pdf") or not file_name:
                file_name = input(
                    "\nEnter a valid name of the final merged pdf (WITHOUT THE EXTENSION - '.pdf'):\n> "
                ).strip()

            # if file already exists, prompt user to re-enter file name
            final_file_name = file_name + ".pdf"
            while final_file_name in os.listdir(dir):
                file_name = input(
                    "\nThe file name already exists in this folder! Please give a unique name!\n> "
                )
                final_file_name = file_name + ".pdf"
            
            # Re-read final file name from the corrected variable
            file_name = final_file_name

            # add PDFs to be merged
            successful_merges = 0
            for file in pdfs:
                try:
                    path = os.path.join(dir, file)
                    merger.pages.extend(Pdf.open(path).pages)
                    successful_merges += 1
                except Exception as e:
                    print(
                        f"❗️ The following PDF: {file} seems to be corrupted... Skipping it. Error: {e} ❗️"
                    )

            # merge the PDFs and save the file in current directory.
            if successful_merges > 0:
                merger.save(os.path.join(dir, file_name))
            else:
                exit(f"\nNo valid PDFs remaining to merge... Exiting...")

            print(
                "\nThe PDFs have been successfully merged as/in: ",
                os.path.abspath(os.path.join(dir, file_name)),
                " ✅",
            )

        # allows user wants to modify list before merging:
        else:
            # get user's numeric input - 1 or 2
            type_choice = input(
                "\n1: Specify filenames to EXCLUDE\n2: Specify filenames to INCLUDE\n\nEnter the choice (number):\n> "
            )
            while type_choice not in ("1", "2"):
                type_choice = input(
                    "\n1: Specify filenames to EXCLUDE\n2: Specify filenames to INCLUDE\n\nEnter the choice (please enter '1' or '2'):\n> "
                )

            # exclude or include user's list
            action_type = "exclude" if type_choice == "1" else "include"
            pdfs = modify(pdfs, action_type)