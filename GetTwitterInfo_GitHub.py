import twitter

def main():

	### Use your own Twitter API Key
	api = twitter.Api(consumer_key='', #Use your own consumer_key
					  consumer_secret='',  #Use your own consumer_secret
					  access_token_key='',  #Use your own access_token_key
					  access_token_secret='')  #Use your own access_token_secret

	####### USER = the twitter handle of a user #################################
	
	### Twitter users without the @ before their user name
	user = ['theportugalnews',
	'abolapt',
	'algarve24',
	'portugalpress',
	'algarve_news',
	'cmjornal',
	'chorrord',
	'correiodominho',
	'asbeiras',
	'expresso']

	####### USER2 = the twitter ID of a user######################################
	
	### Twitter users ID
	user2 = [419304022, 2097571]

	getTwitterID(api, user)
	getTwitterHandle(api, user2)

#################################################################################################
#################################################################################################
#################################################################################################

def getTwitterID(api, user):

	### CONVERSION OF TWITTER HANDLE TO TWITTER ID ###

	names = api.UsersLookup(screen_name=user)
	idNumbers = [s.id for s in names]
	dictionary = dict(zip(user, idNumbers )) 
	print dictionary


#################################################################################################
#################################################################################################
#################################################################################################

def getTwitterHandle(api, user2):

# 	### CONVERSION OF TWITTER ID TO TWITTER HANDLE ###

	ids = api.UsersLookup(user_id=user2)
	handleNames = [s.name for s in ids]
	dictionary2 = dict(zip(user2, handleNames))
	print dictionary2



if __name__ == '__main__':
	main()

