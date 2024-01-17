# Using OAuth1 auth helper
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

class OAuthService():
    def __init__(self):
        self.client_key = "6CH86t5f5cDuooRaaM37smblN"
        self.client_secret = "ozc69PmPhB5DUyydtnk0dj72wn2zOW8ZSRSUNvVPnC2fSJ9ptZ"
        
        self.request_token_url = 'https://api.twitter.com/oauth/request_token'
        self.base_authorization_url = 'https://api.twitter.com/oauth/authorize'
        self.access_token_url = 'https://api.twitter.com/oauth/access_token'
        
        self.oauth = OAuth1(self.client_key, client_secret=self.client_secret)
    
    def getRequestToken(self):
        r = requests.post(url=self.request_token_url, auth=self.oauth)
        credentials = parse_qs(r.content)
        
        resource_owner_key = str(credentials.get(b'oauth_token')[0], encoding='utf-8')
        resource_owner_secret = str(credentials.get(b'oauth_token_secret')[0], encoding='utf-8')
        
        authorization_url = self.base_authorization_url + '?oauth_token=' + resource_owner_key
        
        ret = {"resource_owner_key":resource_owner_key,"resource_owner_secret":resource_owner_secret,"authorization_url":authorization_url}
        return(ret)
    
    def getUserInfos(self,temp_oauth_token):
        r = requests.get("localhost:80/user/getByOAuthToken/"+temp_oauth_token)
        if r.status_code == 200 :
            return r.json
    
    def getOAuthToken(self,resource_owner_key,resource_owner_secret,verifier):
        oauth = OAuth1(self.client_key,
                   client_secret=self.client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)
        r = requests.post(url=self.access_token_url, auth=oauth)
        credentials = parse_qs(r.content)
        oauth_token = str(credentials.get(b'oauth_token')[0], encoding='utf-8')
        oauth_token_secret = str(credentials.get(b'oauth_token_secret')[0], encoding='utf-8')
        ret = {"oauth_token":oauth_token,"oauth_token_secret":oauth_token_secret}
        return(ret)
    
    def updateUser(userId,jsonObject):
        r = requests.patch("localhost:80/user/update/"+userId,jsonObject)
        return
        