import json

# Read the contents of the file
with open('jsonfile1.json', 'r') as file:
    data_list = dict(json.load(file))

# Now data_list contains a list of dictionaries, each representing one JSON object in the file
print(data_list)

print(data_list['question'])
