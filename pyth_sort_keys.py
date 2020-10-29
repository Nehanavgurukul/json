import json
num={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(num)
print("\nJSON data:")
print(json.dumps(num, sort_keys=True,indent=6))
