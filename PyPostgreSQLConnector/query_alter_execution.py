import psycopg2, pandas as pd, sys
import csv_xlsx_prompt 
from new_query_prompt import new_query_alter_prompt

#QUERY PROMPT
def query_ex(connection):

	Q = False 
	while Q == False:
		
		try: 
			
			Q = input('\nQuery >> ')
			cursor = connection.cursor() 
			cursor.execute(Q)  
			records = cursor.fetchall() 
			new_record = pd.read_sql(Q, connection)
			header = [i[0] for i in cursor.description] 
			csv_xlsx_prompt.csv_xlsx_(new_record, records, header, connection, cursor)	

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction, psycopg2.errors.SyntaxError):
			print('\nQuery Error.')
			connection.rollback() 
			Q = False
			


		except KeyboardInterrupt:
			print('\nGoodbye!')
			sys.exit()	

#ALTER TABLE PROMPT
def alter_table_ex(connection):
	Alter = False 
	while Alter == False:
		
		try: 
			Alter = input('\nAlter >> ') 
			cursor = connection.cursor()
			cursor.execute(Alter)   
			connection.commit() 
			if (connection):
				print('\nProcess Completion Succesfull.')
				cursor.close()
				print('\nCursor closed.')	
				new_query_alter_prompt(connection)
				

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction):
			print('\nQuery Error.')
			connection.rollback()  
			Alter = False
		except KeyboardInterrupt:
			print('\nGoodbye!')
			sys.exit()		