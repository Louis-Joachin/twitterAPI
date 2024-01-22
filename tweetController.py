from fastapi import FastAPI
from fastapi import Request
from tweetService import TweetService

app =FastAPI()
tweet_service = TweetService()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/Twitter/Post")
async def new_tweet(request: Request):
    json_object = await request.json()
    clientv2 = tweet_service.authenticationAPI2(json_object["access_token"],json_object["access_token_secret"])#client object API 2
    tweet_id = tweet_service.tweet(clientv2,json_object["text"],id)
    return "OK"

@app.post("/Twitter/PostWithPicture")
async def new_tweet_picture(request: Request):
    json_object = await request.json()
    clientv1 = tweet_service.authentificationAPI1(access_token=json_object["access_token"],access_token_secret=json_object["access_token_secret"]) #client object API 1
    id = tweet_service.fileUpload(clientv1,json_object["imageURL"])
    
    clientv2 = tweet_service.authenticationAPI2(json_object["access_token"],json_object["access_token_secret"])#client object API 2
    tweet_id = tweet_service.tweet(clientv2,json_object["text"],id)
    return tweet_id

@app.post("/Twitter/updateProfilePic")
async def updateProfilePic(request: Request):
    json_object = await request.json()
    clientv1 = tweet_service.authentificationAPI1(access_token=json_object["access_token"],access_token_secret=json_object["access_token_secret"]) #client object API 1
    tweet_service.updateProfilePicture(clientv1,json_object["imageURL"])
    return "OK"
    
    

