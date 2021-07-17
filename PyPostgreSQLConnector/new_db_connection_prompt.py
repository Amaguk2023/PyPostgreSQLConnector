import __main__, sys

#NEW DB CONNECTION PROMPT
def new_db_connection_prompt():
	try:
		new_connection = False 
		while not new_connection: 
			new_connection = input('\nNew Database connection? (Y/n) ').lower()
			if new_connection == 'y':
				__main__.postgresql_database_prompt()
			elif new_connection == 'n':
				print('\nGoodbye!\n')
				sys.exit()
			else:
				print('\nCheck your spelling.')
				new_connection = False
	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	