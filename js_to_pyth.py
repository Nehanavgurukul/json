import json 
a_file = open("sample_file.json", "r")

json_object = json.load(a_file)

a_file.close()

print(json_object)