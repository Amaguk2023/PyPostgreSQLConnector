import psycopg2, csv, pandas as pd
from new_query_prompt import new_query_alter_prompt

#CSV FILE CREATION
def csv_ction(records, header, connection, cursor):

	try:

		file_name = input('\nFile Name >> ') 
		with open(file_name +'.csv', 'w', newline='') as data:
			writer = csv.writer(data) # create csv writer object
			writer.writerow(header) #writes headers to csv
			for row in records: #iterates through item and adds rows to csv.
				writer.writerow(row)
		
			print('\ncsv file has been exported.')
			cursor.close()
			print('\nCursor closed.')
			new_query_alter_prompt(connection)

	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	

#XLSX FILE CREATION
def xlsx_ction(new_record, connection, cursor):
	try:

		file_name = input('\nFile Name >> ')
		writer = pd.ExcelWriter(file_name + '.xlsx') # create excel writer object
		new_record.to_excel(writer) # write dataframe to excel
		writer.save() # save the excel
		print('\nxlsx file has been exported!')
		cursor.close()
		print('\nCursor closed.')
		new_query_alter_prompt(connection)

	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	