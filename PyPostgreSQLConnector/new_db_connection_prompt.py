import postgre_database_prompt, sys

#NEW DB CONNECTION PROMPT
def new_db_connection_prompt(connection):
	try:
		new_connection = False 
		while not new_connection: 
			new_connection = input('\nNew Database connection? (Y/n) ').lower()
			if new_connection == 'y':
				connection.close()
				postgre_database_prompt.postgresql_database_prompt()
			elif new_connection == 'n':
				connection.close()
				print('\nGoodbye!\n')
			else:
				print('\nCheck your spelling.')
				new_connection = False
	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	