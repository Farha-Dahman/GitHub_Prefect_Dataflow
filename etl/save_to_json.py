import json

def save_json(data, filename):
    """
    Saves data to a JSON file.

    Args:
    - data: The data to be saved.
    - filename: The name of the JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)