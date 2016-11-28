import tweepy
from weather.map.models import Tweets
from weather.map.models import Region

def pullTweets(r, latitude, longitude): #r is the region
    auth = tweepy.OAuthHandler('ngUgwteOKxvdrdW9RKjBtxDY6', 'sjgFfZxYLQf31bNHQTBQtfxbkFsLULE2AJPjlcuCWyLiFxvF4a')
    auth.set_access_token('524971431-pRjRIEoMA4xRCShSSFYB0hVgx2k6MWPk71t4zvgr', 'TGIXTci4tZp8OlXKvo0y1Lj0yg7QD1n59w1WDrijliOK7')
    api = tweepy.API(auth)
    
    located_tweets = api.search(q="", count = 100, show_user=0, geocode=""+str(latitude)+","+str(longitude)+","+"1000mi")
    high_id = located_tweets[0].id
    for tw in located_tweets:
        t = Tweets.objects.create(region = r, tweet = tw.text)
        t.save()
        if tw.id < high_id:
            high_id = tw.id

    for x in range(0,3):
        located_tweets = api.search(q="", count = 100, show_user=1, max_id = high_id, geocode=""+str(latitude)+","+str(longitude)+","+"1000mi")
        for tw in located_tweets:
            if (tw.id < high_id):
                t = Tweets.objects.create(region = r, tweet = tw.text)
                t.save()
                high_id = tw.id
