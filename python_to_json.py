import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
name_file = open("neha.json","w")
json.dump(python_obj,name_file,indent=6)
name_file.close()