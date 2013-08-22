from twython import Twython

usuario = "andrey"#definimos una variable 
twitter = Twython()#creamos un objeto la clase Twython

followers = twitter.getFollowersIDs( screen_name = usuario)#traemos los usuarios muy facil

for follower_id in followers:
	print "Usuario %d sigue a %s"%(follower_id,usuario)

tweets = twitter.getPublicTimeline()#traemos los twees

for tweet in tweets:
	print tweet['user']['name'].encode('utf-8')
	print tweet['text'].encode('utf-8')


results = twitter.getDailytrends()#usando el objeto usamos ese metodo

#esto se llama o se dice iterar objetos
for time, trend_list in results['trends'].iteritems():
	print time
	for trend in trend_list:
		print trend['query']