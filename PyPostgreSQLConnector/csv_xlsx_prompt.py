import psycopg2, sys
import csv_xlsx_file_creation

#CSV/XLSX PROMPT
def csv_xlsx_(new_record, records, header, connection, cursor):
	try:
		
		save_record = False 
		while save_record == False:

			save_record = input('\nExport Query as csv or xlsx? ').lower()
			if save_record == 'csv':
				csv_xlsx_file_creation.csv_ction(records, header, connection, cursor)
	
			elif save_record == 'xlsx':
				csv_xlsx_file_creation.xlsx_ction(new_record, connection, cursor)

			else:
				print('\nCheck your spelling.')
				save_record = False

	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	
