import json
import openpyxl

file_name = "response.json"


def print_keys(prefix_id, parent_dict_key, dictx):

    for p_id, p_info in dictx.items():
        v = "-> " + p_info if type(p_info) == str else ""
        print(prefix_id, "-", parent_dict_key, ":", p_id, v)

        if type(p_info) == list:
            for biller in p_info:   # array
                print_keys(prefix_id+1, p_id, biller)
        elif type(p_info) == dict:
            print_keys(prefix_id + 1, p_id, p_info)
    if prefix_id == 2:
        print("-----", 20 * str(prefix_id), "------")

def print_values(prefix, dictx):

    for p_id, p_info in dictx.items():
        print (p_id, type(p_info))
        if type(p_info) == dict:
            for k, v in p_info.items():
                print(prefix, k, v)

        elif type(p_info) == list:
            for biller in p_info:  # array
                print_values(p_id, biller)
                # for key in biller:
                #     print(p_id, key + ':', biller[key])
        else:
            print(prefix, p_id, p_info)

def list_billers (dicx):

    headers = dicx[0]
    arr=[]
    for k, v in headers.items():
        if type(v) not in (dict, list) :
            arr.append(k)
    print (arr)

    for biller in dicx:
        arr=[]
        for k, v in biller.items():
            if type(v) not in (dict, list) :
                arr.append(v)
        print (arr)

def list_biller_info (dicx, key):

    headers = dicx[0][key]
    if type(headers) == list:
        # arr=[]
        # for k, v in headers[0].items():
        #     if type(v) not in (dict, list) :
        #         arr.append(k)
        # print (arr)`

        for item in dicx:
            for biller in item[key]:
                print(biller.keys())
                arr=[]
                for k, v in biller.items():
                    if type(v) not in (dict, list) :
                        arr.append(v)
                print(arr)

with open(file_name, 'r', encoding ='UTF-8') as myfile:
    data=myfile.read()
myfile.close
# parse file
billers = json.loads(data)

fp = open('biller.json', 'wt')
json.dump(billers, fp, indent=4)


print_keys(0, "billers", billers)
#print_values("", billers)
#list_billers(billers['biller_records'])
#print (billers['biller_records'])
#list_billers(billers['biller_records'])
# list_biller_info(billers['biller_records'], 'biller_information')




