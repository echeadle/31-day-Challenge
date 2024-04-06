import json

# Read the contents of the file
with open('data_file.json', 'r') as file:
    file_contents = file.read()

# Split the file contents into individual JSON objects
json_objects = file_contents.split('\n}\n')

# Initialize an empty list to store dictionaries
data_list = []

# Iterate through each JSON object, load it as a dictionary, and append to the list
for obj in json_objects:
    # Add back the closing brace that was removed during splitting
    obj += '\n}'
    data_list.append(json.loads(obj))

# Now data_list contains a list of dictionaries, each representing one JSON object in the file
print(data_list)
