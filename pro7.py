def lang():
    """Defines and returns the language data dictionary."""
    data = {
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
            "Other": ["Hindi", "Tamil", "Kannada", "Marathi", "Oriya",]
        }
    }
    return data 

def find_max_lang(lang_data): 
    max_count = 0
    max_state = ""
    
    
    for state_name, lang_dict in lang_data.items(): 
        
        
        all_lang = set(lang_dict["Official"] + lang_dict["Other"]) 
        
        current_count = len(all_lang)
        

        if current_count > max_count:
            max_count = current_count
            max_state = state_name 
            
    return max_state
def nip(data ,state_name):
    return len(data[state_name]["other"])


language_data = lang() 


result_1 = find_max_lang(language_data) 

print(f"Option 1: State with Max Languages: {result_1}")
