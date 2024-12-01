import os
import json

def load_from_json(json_file_path):
    if os.path.exists(json_file_path): # Check if the file exists
        try:
            with open(json_file_path, "r") as file: # Open the file in read mode
                data = json.load(file) # Load the JSON data from the file
                return data # Return the JSON data
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")
    else:
        print(f"File not found: {json_file_path}")
    return []