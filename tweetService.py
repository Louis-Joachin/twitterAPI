import tweepy
from urllib.request import urlretrieve
import os

class TweetService():

    def __init__(self):
        self.consumer_key = "6CH86t5f5cDuooRaaM37smblN"
        self.consumer_key_secret = "ozc69PmPhB5DUyydtnk0dj72wn2zOW8ZSRSUNvVPnC2fSJ9ptZ"
    
    def authentificationAPI1(self,access_token,access_token_secret):
        auth = tweepy.OAuth1UserHandler(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        return(tweepy.API(auth))

    def authenticationAPI2(self,access_token,access_token_secret):
        client = tweepy.Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        return client
    
    
    def fileUpload(self,api,url):
        imagePath = self.downloadFile(url)
        media = api.media_upload(imagePath)
        if os.path.exists(imagePath):
            os.remove(imagePath)
        else:
            print("The file does not exist")
        return media.media_id

    def downloadFile(self,url):
        path = urlretrieve(url)[0]
        return(path)

    def tweet(self,client,text,media_id):
        response = client.create_tweet(text=text,media_ids = [media_id])
        return(response.data["id"])
    
    def tweet(self,client,text):
        response = client.create_tweet(text=text)
        return(response.data["id"])
    
    def updateProfilePicture(self,client,url):
        imagePath = self.downloadFile(url)
        client.update_profile_image(imagePath)




