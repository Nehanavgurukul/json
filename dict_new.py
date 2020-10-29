import json 
details={
    "name":"neha",
    "age":"21",
    "address":"bhander"
}
my_file1=open("neha1.json","w")
json.dump(details,my_file1,indent=3)
my_file1.close()
