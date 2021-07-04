import psycopg2, sys
import query_alter_prompt


#DATABASE CREDENTIALS PROMPT.
def postgresql_database_prompt():
	print('\nAGK PostgreSQL Connector')
	
	dbname_ = False 
	while dbname_ == False:
	
		try:

			dbname_ = input('\nDatabase >> ') 
			user = input('User >> ')
			password = input('Password >> ')
			host = input('Host >> ') 
			port = input('Port >> ')
			
			connection = psycopg2.connect(dbname = dbname_ , user = user, password = password, host = host, port = port) 

			if (connection): 
				print('\nConnected to {} database.'.format(dbname_))
				query_alter_prompt.query_or_alter_database_prompt(connection)

		except (KeyboardInterrupt):
			print('\nGoodbye!\n')
			sys.exit(0)

		except (psycopg2.OperationalError, UnboundLocalError):
			print('\nError while connecting to PostgreSQL, please verify your credentials.\n')
			dbname_ = False 

if __name__ == '__main__':			
	postgresql_database_prompt()






