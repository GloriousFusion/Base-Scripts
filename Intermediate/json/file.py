### INTERMEDIATE JSON DATA MANAGEMENT (READ/WRITE/MODIFY/APPEND NESTED JSON DATA) ###

import json # Default python library for parsing json files
path = "json/data.json" # Path to data.json file


def read_data():
    with open(path, "r") as file:
        json_data = json.load(file)
        return json_data


def modify_data(json_data, user_id=0, field="name", data="Administrator"):
    with open(path, "w") as file:
        users = json_data["users"]
        users[user_id][field] = data
        json.dump(json_data, file, indent=4)


def append_data(json_data, user_id=0, key="new", data="test"):
    with open(path, "w") as file:
        users = json_data["users"]
        users[user_id][key] = data
        json.dump(json_data, file, indent=4)


def create_data(json_data, key="name", data="Example"):
    with open(path, "w") as file:
        users = json_data["users"]
        users.append({key: data})
        json.dump(json_data, file, indent=4)


modify_data(read_data(), user_id=1, field="description", data="Default User Account") # Example of data modification for a specific value

append_data(read_data(), user_id=1, key="balance", data=5) # Example of data addition for a key and value pair

create_data(read_data()) # Example of data creation with a base key and value pair (Using default values defined in the function)
