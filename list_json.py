import json
python_list={"5875645"}
list1=open("list.json","w")
json.dump(python_list,list1,indent=6)
python_list.close()