# Create your views here.
from django.http import HttpResponse
from twython import Twython#importamos el Twython que descargamos

def index(request):
	usuario = "@Jandrey15"#definimos una variable 

	twitter = Twython()#creamos un objeto la clase Twython

	followers = twitter.getFollowersIDs( screen_name = usuario)#traemos los usuarios muy facil
    #tweets = twitter.getPublicTimeline()

	return HttpResponse(followers)
