import psycopg2, sys, csv, pandas as pd, openpyxl, socket

#DATABASE CREDENTIALS PROMPT.
def postgre_database_prompt():
	
	dbname_ = False #Variable is False
	while dbname_ == False:
	
		try:

			dbname_ = input('\nDatabase >> ') #Variable is true
			user = input('User >> ')
			host = input('Host >> ') #This is not needed in my case, dunno why
			port = input('Port >> ')
			postgre_connection(dbname_, user, host, port)

		except (KeyboardInterrupt):
			print('\nGoodbye!\n')
			sys.exit(0)

		except (psycopg2.OperationalError, UnboundLocalError):
			print('\nError while connecting to PostgreSQL, please verify your credentials.\n')
			dbname_ = False #Back to false and restarts function.

#DATABASE CONNECTION.
def postgre_connection(dbname_, user, host, port):
	
	connection = psycopg2.connect(dbname = dbname_ , user = user, host = host, port = port) #postgresql connection.

	if (connection): #If the connection is true.
		print('\nConnected to {} database.'.format(dbname_))
		query_or_alter_database_prompt(connection)

#QUERY AND ALTER DATABASE PROMPT.
def query_or_alter_database_prompt(connection):
	query_alter_table = False 
	while query_alter_table == False:

		query_alter_table = input('\nAre you going to query or alter database? ').lower()
		if query_alter_table == 'query':
			query_execution(connection)
		elif query_alter_table in ('alter', 'alter database'):
			alter_table_execution(connection)
		else:
			print('\nPlease check your spelling')
			query_alter_table = False			

#QUERY PROMPT
def query_execution(connection):

	Q = False 
	while Q == False:
		
		try: 
			
			Q = input('\nQuery >> ')
			cursor = connection.cursor() ######################### WE HAVE AN ERROR HERE
			cursor.execute(Q)  # Executing a SQL query
			records = cursor.fetchall() #returns tuple 
			new_record = pd.read_sql(Q, connection)
			header = [i[0] for i in cursor.description] #prints header from the cursor using list comprehension.
			csv_xlsx_prompt(new_record, records, header, connection)	

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction, psycopg2.extensions.connection, AttributeError, TypeError, psycopg2.ProgrammingError):
			print('\nQuery Error.')
			Q = False

#ALTER PROMPT
def alter_table_execution(connection):
	Alter = False 
	while Alter == False:
		
		try: 
			Alter = input('\nAlter >> ') ######################### WE HAVE AN ERROR HERE
			cursor = connection.cursor()
			cursor.execute(Alter)  # Executing a SQL query
			connection.commit() #Alters database in postgresql
			if (connection):
				print('Process Completion Succesfull')
				new_query_prompt(connection)

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction, psycopg2.extensions.connection, AttributeError, TypeError, psycopg2.ProgrammingError):
			print('\nQuery Error.')
			Alter = False

#CSV/XLSX PROMPT
def csv_xlsx_prompt(new_record, records, header, connection):
	
	save_record = False 
	while save_record == False:

		save_record = input('\nExport Query as csv or xlsx? ').lower()
		if save_record == 'csv':
			csv_creation(records, header, connection)
	
		elif save_record == 'xlsx':
			xlsx_creation(new_record, connection)

		else:
			print('\nCheck your spelling.')
			save_record = False

#CSV FILE CREATION
def csv_creation(records, header, connection):

	file_name = input('\nFile Name >> ') 
	with open(file_name +'.csv', 'w', newline='') as data:
		writer = csv.writer(data) # create csv writer object
		writer.writerow(header) #writes headers to csv
		for row in records: #iterates through item and adds rows to csv.
			writer.writerow(row)
		
		print('\ncsv file has been exported.')
		new_query_prompt(connection)
		
#XLSX FILE CREATION
def xlsx_creation(new_record, connection):
	file_name = input('\nFile Name >> ')
	writer = pd.ExcelWriter(file_name + '.xlsx') # create excel writer object
	new_record.to_excel(writer) # write dataframe to excel
	writer.save() # save the excel
	print('\nxlsx file has been exported!')
	new_query_prompt(connection)

#NEW QUERY PROMPT
def new_query_prompt(connection): 
	new_query = False
	while new_query == False:
		new_query = input('\nGo back to alter/query prompt? (Y/n) ').lower()
		if new_query == 'y':
			query_or_alter_database_prompt(connection)
		elif new_query == 'n':
			new_db_connection_prompt()
		else:
			print('\nCheck your spelling.')
			new_query = False

#NEW DB CONNECTION PROMPT
def new_db_connection_prompt():
	new_connection = False 
	while new_connection == False: 
		new_connection = input('\nNew Database connection? (Y/n) ').lower()
		if new_connection == 'y':
			if __name__ == '__main__':
				postgre_database_prompt()

		elif new_connection == 'n':
			print('\nGoodbye!\n')

		else:
			print('\nCheck your spelling.')
			new_connection = False

print('\nAmaguk PostgreSQL Database Connection\n') 
postgre_database_prompt()





