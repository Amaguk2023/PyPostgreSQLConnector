import psycopg2, sys
import query_alter_execution
from art import tprint
import sys

#QUERY AND ALTER DATABASE PROMPT.
def query_alter_database_prompt(connection):
	try:
		menu_prompt = False 
		while not menu_prompt:
			tprint('Menu')
			print('''
Query (Q)
Alter Database (AD)
Create Database (CD)
Exit''')
			menu_prompt = input('\n>> ').lower()
			if menu_prompt == 'q':
				query_alter_execution.query_ex(connection)
			elif menu_prompt == 'ad':
				query_alter_execution.alter_table_ex(connection)
			elif menu_prompt == 'cd':
				query_alter_execution.db_creation_ex(connection)
			elif menu_prompt == 'exit':
				print('\nGoodbye!\n')
				sys.exit()
			else:
				print('\nPlease check your spelling')
				menu_prompt = False	
	except KeyboardInterrupt:
		print('\nGoodbye!')
		sys.exit()	