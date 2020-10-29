import json 
name='{ "neha":"engneering","pooja":"student","radha":"woman"}'
x=json.loads(name)
print(x["pooja"])
print(x["radha"])
print(x["neha"])
print(type(name))
print(type(x))