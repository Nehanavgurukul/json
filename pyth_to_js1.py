import json
detail={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
myfile=open("detail.json","w")
json.dump(detail,myfile,indent=2)
myfile.close()


