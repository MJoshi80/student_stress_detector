import json
#imports the library containing json operation modules
import os
FILE_NAME = "entries.json"
#specifies the file containing the entires
def save_entry(date, day, statement, score, sentiment):
    entries = get_entries()
    #calls the get_entries() module
    new_entry = {
        "date": date,
        "day": day,
        "statement": statement,
        "score": score,
        "sentiment": sentiment
    }
    #creation of a new entry dictionary
    entries.append(new_entry)  
    # adds the new entry to the list
    with open(FILE_NAME, "w") as f:
        json.dump(entries, f)
        #saving into the file
def get_entries():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)
        #reading the file