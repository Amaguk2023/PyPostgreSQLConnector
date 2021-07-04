from new_db_connection_prompt import new_db_connection_prompt
import query_alter_prompt, sys

#NEW QUERY PROMPT
def new_query_alter_prompt(connection): 
	try:
		new_query = False
		while new_query == False:
			new_query = input('\nGo back to alter/query prompt? (Y/n) ').lower()
			if new_query == 'y':
				query_alter_prompt.query_or_alter_database_prompt(connection)
			elif new_query == 'n':
				connection.close()
				print('\nDatabase connection closed.')
				new_db_connection_prompt(connection)
			else:
				print('\nCheck your spelling.')
				new_query = False
	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	