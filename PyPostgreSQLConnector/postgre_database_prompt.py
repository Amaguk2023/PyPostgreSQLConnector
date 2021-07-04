import psycopg2, sys
import query_alter_prompt


#DATABASE CREDENTIALS PROMPT.
def postgresql_database_prompt():
	print('\nAGK PostgreSQL Connector')
	
	dbname_ = False #Variable is False
	while dbname_ == False:
	
		try:

			dbname_ = input('\nDatabase >> ') #Variable is true
			user = input('User >> ')
			password = input('Password >> ')
			host = input('Host >> ') #This is not needed in my case, dunno why
			port = input('Port >> ')
			
			connection = psycopg2.connect(dbname = dbname_ , user = user, password = password, host = host, port = port) #postgresql connection.

			if (connection): #If the connection is true.
				print('\nConnected to {} database.'.format(dbname_))
				query_alter_prompt.query_or_alter_database_prompt(connection)

		except (KeyboardInterrupt):
			print('\nGoodbye!\n')
			sys.exit(0)

		except (psycopg2.OperationalError, UnboundLocalError):
			print('\nError while connecting to PostgreSQL, please verify your credentials.\n')
			dbname_ = False #Back to false and restarts function.




if __name__ == '__main__':			
	postgresql_database_prompt()






