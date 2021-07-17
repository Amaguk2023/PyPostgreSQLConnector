import psycopg2, pandas as pd, sys
import csv_xlsx_prompt 
from new_query_prompt import new_query_alter_prompt
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



#QUERY PROMPT
def query_ex(connection):
	Q = False 
	while not Q:	
		try: 
			Q = input('\nQuery >> ')
			if Q == 'menu':
				new_query_alter_prompt(connection)
			else:
				cursor = connection.cursor() 
				cursor.execute(Q)  
				records = cursor.fetchall() 
				new_record = pd.read_sql(Q, connection)
				header = [i[0] for i in cursor.description] 
				csv_xlsx_prompt.csv_xlsx_(new_record, records, header, connection, cursor)	
		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction):
			print('\nQuery Error.')
			connection.rollback() 
			Q = False	
		except KeyboardInterrupt:
			print('\nGoodbye!')
			sys.exit()	

#ALTER TABLE PROMPT
def alter_table_ex(connection):
	Alter = False 
	while not Alter:
		try: 
			Alter = input('\nAlter >> ') 
			if Alter == 'menu':
				new_query_alter_prompt(connection)
			else:
				cursor = connection.cursor()
				cursor.execute(Alter)   
				connection.commit() 
				if (connection):
					print('\nDatabase alteration succesfull.')
					cursor.close()	
					new_query_alter_prompt(connection)
		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction):
			print('\nQuery Error.')
			connection.rollback()  
			Alter = False
			

#DATABASE CREATION PROMPT
def db_creation_ex(connection):
	datab = False 
	while not datab:
		datab = input('\nInsert Database Name >> ')
		connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		cursor = connection.cursor()
		if datab == 'menu':
				new_query_alter_prompt(connection)
		else:
			cursor.execute('CREATE DATABASE {dbname}'.format(dbname=datab))
			if (connection):
				print('\nDatabase creation succesfull.')
				cursor.close()	
				new_query_alter_prompt(connection)















