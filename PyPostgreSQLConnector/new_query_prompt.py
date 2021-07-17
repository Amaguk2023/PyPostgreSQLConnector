from new_db_connection_prompt import new_db_connection_prompt
import query_alter_prompt, sys

#NEW QUERY PROMPT
def new_query_alter_prompt(connection): 
	try:
		new_query = False
		while not new_query:
			new_query = input('\nGo back to Menu (Y/n) ').lower()
			if new_query == 'y':
				query_alter_prompt.query_alter_database_prompt(connection)
			elif new_query == 'n':
				connection.close()
				new_db_connection_prompt()
			else:
				print('\nCheck your spelling.')
				new_query = False
	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	