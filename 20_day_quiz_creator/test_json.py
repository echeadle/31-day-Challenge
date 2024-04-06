import json



with open("data_file.json", "r") as read_content:
    json_string= json.load(read_content)

json_dict=json.loads(json_string)
