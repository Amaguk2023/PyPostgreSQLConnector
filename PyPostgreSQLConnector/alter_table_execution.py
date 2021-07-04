from new_query_prompt import new_query_alter_prompt
import psycopg2

#ALTER PROMPT
def alter_table_ex(connection):
	Alter = False 
	while Alter == False:
		
		try: 
			Alter = input('\nAlter >> ') ######################### WE HAVE AN ERROR HERE
			cursor = connection.cursor()
			cursor.execute(Alter)  # Executing a SQL query
			connection.commit() #Alters database in postgresql
			if (connection):
				print('Process Completion Succesfull')
				cursor.close()
				new_query_alter_prompt(connection)

		except (psycopg2.errors.SyntaxError, psycopg2.errors.UndefinedTable, psycopg2.errors.InFailedSqlTransaction, psycopg2.extensions.connection, AttributeError, TypeError, psycopg2.ProgrammingError):
			print('\nQuery Error.')
			Alter = False