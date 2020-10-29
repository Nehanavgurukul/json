import json
# python object (dictionary)
marks={
    "neha":"89",
    "ravina":{
        "physics":"97",
        "chemistry":"96",
        "maths":"100"
    },
    "bharti":"98"}
marks_files=open("neha.json","w")
json.dump(marks,marks_files,indent=2)
marks_files.close()