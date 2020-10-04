from fawry_billers import fawry_billers_excel, get_biller_record

#print_values("", billers)

#list_billers(billers['biller_records'])
#print (billers['biller_records'])
#list_billers(billers['biller_records'])
#list_biller_info(billers['biller_records'], 'biller_information')
file_name = r'.\response.json'
fawry_billers_excel(file_name)
#print ('output file:', file_name +".xlsx" )
get_biller_record(file_name, 'Vodafone')
