import psycopg2, pandas as pd, sys
import csv_xlsx_prompt 
from new_query_prompt import new_query_alter_prompt

#QUERY PROMPT
def query_ex(connection):

	Q = False 
	while Q == False:
		
		try: 
			
			Q = input('\nQuery >> ')
			cursor = connection.cursor() ######################### WE HAVE AN ERROR HERE. ERROR FIXED
			cursor.execute(Q)  # Executing a SQL query. IF THIS FAILS AND THE EXCEPT IS EXECUTED I HAVE TO ROLLBACK THE CONNECTION, SINCE THE NEW QUERY WILL BE EXECUTED IN A AN ALREADY ABORTED TRANSACTION, BUT NOT ROLL BACKED. 
			records = cursor.fetchall() #returns tuple 
			new_record = pd.read_sql(Q, connection)
			header = [i[0] for i in cursor.description] #prints header from the cursor using list comprehension.
			csv_xlsx_prompt.csv_xlsx_(new_record, records, header, connection, cursor)	

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction, psycopg2.errors.SyntaxError):
			print('\nQuery Error.')
			connection.rollback() #	psycopg2.errors.InFailedSqlTransaction: current transaction is aborted, commands ignored until end of transaction block. Rollback fixes this. 
			Q = False
			


		except KeyboardInterrupt:
			print('\nGoodbye!')
			sys.exit()	

#ALTER TABLE PROMPT
def alter_table_ex(connection):
	Alter = False 
	while Alter == False:
		
		try: 
			Alter = input('\nAlter >> ') ######################### WE HAVE AN ERROR HERE. ERROR FIXED
			cursor = connection.cursor()
			cursor.execute(Alter)  # Executing a SQL query. IF THIS FAILS AND THE EXCEPT IS EXECUTED I HAVE TO ROLLBACK THE CONNECTION, SINCE THE NEW QUERY WILL BE EXECUTED IN A AN ALREADY ABORTED TRANSACTION, BUT NOT ROLL BACKED. 
			connection.commit() #Alters database in postgresql
			if (connection):
				print('\nProcess Completion Succesfull.')
				cursor.close()
				print('\nCursor closed.')	
				new_query_alter_prompt(connection)
				

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction):
			print('\nQuery Error.')
			connection.rollback() #	psycopg2.errors.InFailedSqlTransaction: current transaction is aborted, commands ignored until end of transaction block. Rollback fixes this. 
			Alter = False
		except KeyboardInterrupt:
			print('\nGoodbye!')
			sys.exit()		