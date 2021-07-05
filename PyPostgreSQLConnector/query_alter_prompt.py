import psycopg2, sys
import query_alter_execution

#QUERY AND ALTER DATABASE PROMPT.
def query_or_alter_database_prompt(connection):
	try:
		query_alter_table = False 
		while not query_alter_table:
			query_alter_table = input('\nAre you going to query or alter database? ').lower()
			if query_alter_table == 'query':
				query_alter_execution.query_ex(connection)
			elif query_alter_table in ('alter', 'alter database'):
				query_alter_execution.alter_table_ex(connection)
			else:
				print('\nPlease check your spelling')
				query_alter_table = False	
	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	