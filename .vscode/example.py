def get_language_data():
    """Stores the language data in a nested dictionary structure."""
    return {
        "Andhra Pradesh": {
            "Official": ["Telugu", "English"],
            "Other": ["Urdu", "Hindi", "Banjara", "Tamil", "Kannada", "Marathi", "Oriya"]
        },
        "Karnataka": {
            "Official": ["Kannada", "English"],
            "Other": ["Urdu", "Telugu", "Tamil", "Marathi"]
        },
        "Kerala": {
            "Official": ["Malayalam", "English"],
            "Other": ["Hindi", "Kannada", "Tamil", "Tulu"]
        },
        "Tamilnadu": {
            "Official": ["Tamil", "English"],
            "Other": ["Telugu", "Kannada", "Urdu", "Malayalam", "Hindi"]
        },
        "Telangana": {
            "Official": ["Telugu", "Urdu"],
            "Other": ["Hindi", "Tamil", "Kannada", "Marathi", "Oriya"]
        }
    }

# --- Menu Logic Functions ---

def option_1_max_languages_state(data):
    """Returns the state with the maximum number of unique languages."""
    max_count = -1
    max_state = ""
    for state, languages in data.items():
        # Combine lists and use set() to count unique languages
        all_languages = set(languages["Official"] + languages["Other"])
        current_count = len(all_languages)
        
        if current_count > max_count:
            max_count = current_count
            max_state = state
    return max_state

def option_2_count_other_languages(data, state_name):
    """Returns the count of spoken languages excluding official languages."""
    # We rely on the main function to validate the state_name exists
    return len(data[state_name]["Other"])

def option_3_states_by_non_official_language(data, language_name):
    """Returns a list of states where the language is spoken but NOT official."""
    result_states = []
    for state, languages in data.items():
        # Check if the language is in the 'Other' list
        is_other = language_name in languages["Other"]
        # AND check if the language is NOT in the 'Official' list
        is_not_official = language_name not in languages["Official"]
        
        if is_other and is_not_official:
            result_states.append(state)
    return result_states

def option_4_list_unique_languages(data):
    """Returns a list of languages used in only ONE state."""
    language_use_count = {}
    
    # 1. Count usage across all states
    for languages in data.values():
        all_languages_in_state = set(languages["Official"] + languages["Other"])
        for lang in all_languages_in_state:
            language_use_count[lang] = language_use_count.get(lang, 0) + 1
            
    # 2. Filter for languages used only once
    unique_languages = [lang for lang, count in language_use_count.items() if count == 1]
    return unique_languages

# --- Main Program Execution ---

def main():
    """Handles the menu, input parsing, validation, and output."""
    data = get_language_data()
    
    # Take input as required by the prompt
    # Note: In a real system, you might use a loop or read from stdin/file
    user_input = input().strip()
    
    # Use split(',', 1) to separate the choice from the parameter using the first comma
    parts = user_input.split(',', 1)
    
    menu_choice = parts[0]
    
    # --- 1. Menu Choice Validation ---
    if menu_choice not in ('1', '2', '3', '4'):
        print("Error")
        return # End execution
        
    parameter = parts[1] if len(parts) > 1 else None

    # --- 2. Input Format Validation (Checks for missing/extra parameters) ---
    
    if menu_choice in ('1', '4'):
        # Options 1 and 4 must have NO parameter
        if parameter is not None:
            print("Error")
            return
            
    elif menu_choice in ('2', '3'):
        # Options 2 and 3 MUST have a parameter
        if parameter is None or not parameter.strip():
            print("Error")
            return
            
    # --- 3. Execute Option Logic ---
    
    if menu_choice == '1':
        result = option_1_max_languages_state(data)
        print(result)
        
    elif menu_choice == '2':
        state_name = parameter
        if state_name not in data: # Validate State Name
            print("Error")
            return
        result = option_2_count_other_languages(data, state_name)
        print(result)

    elif menu_choice == '3':
        language_name = parameter
        result = option_3_states_by_non_official_language(data, language_name)
        # Output is a list of state names (as per the prompt's implied format)
        print(result) 
        
    elif menu_choice == '4':
        result = option_4_list_unique_languages(data)
        # Output is a list of unique languages (as per the prompt's implied format)
        print(result)

if __name__ == "__main__":
    main()