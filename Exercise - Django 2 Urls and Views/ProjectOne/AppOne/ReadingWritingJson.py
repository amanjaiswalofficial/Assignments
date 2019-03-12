import json

#Reading from Files
with open('Data',mode='r') as json_data:
    data=json.load(json_data)
    
    print(data['Names']['Name'])

Value={"name":"Karan","section":"Arjun"}

#Writing Into Files
with open('Data',mode='w') as json_data:
    json.dump(Value,json_data)