def analyze_marks(marks_list):
    total = 0
    status = "pass" # Start by assuming "pass"

    for mark in marks_list:
        total += mark # FIX 1: Add the single 'mark', not the 'marks' list
        
        # FIX 2: Only change to "fail". Never change back to "pass".
        # Remove the 'else' block.
        if mark < 50:
            status = "fail" 
            
    if len(marks_list) > 0:
        avg = total / len(marks_list) # FIX 3: Divide by the LENGTH of the list
    else:
        avg = 0
        
    return total, avg, status

# --- Main Program ---
marks = []
n = 5

print(f"Enter marks for {n} subjects:")
for m in range(n):
    mark = int(input())
    marks.append(mark)

# FIX 4 & 5: You MUST capture the returned values into new variables
total_marks, avg_percentage, overall_status = analyze_marks(marks) 

# Now, print the variables you just captured
print("\n--- Analysis Report ---")
# Use an f-string (with 'f' at the start) to print variables
print(f"The result: {overall_status}")
print(f"The average: {avg_percentage:.2f}") # .2f formats it nicely
print(f"The total: {total_marks}")