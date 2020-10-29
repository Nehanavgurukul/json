import json
family={ "grand_maa":"vimla","mother":"sunita","father":"netsingh"}
file_1=open("family.json","w")
json.dump(family,file_1,indent=4)
file_1.close()





# relation=json.loads(faimly)
# print(faimly)
# print(relation)
