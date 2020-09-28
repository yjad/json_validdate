import json
file_name = "C:\\Users\\YJAD\\Documents\\branch-ar.json"

with open(file_name, 'r') as myfile:
    data=myfile.read()
myfile.close
# parse file
brs = json.loads(data)
#print(json.dumps(brs['id'], indent=4))
for b in brs:
    #print(json.dumps(b, indent=4))
    print (b['id'], b['title'], "city: ", b['address']['city'])

