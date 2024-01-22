from oauthService import OAuthService
from fastapi import FastAPI

app = FastAPI()
oauth = OAuthService()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/OAuth/new")
def new_oauth():
    return(oauth.getRequestToken())

@app.get("/OAuth/createNewToken")
def new_oauth_token(temp_oauth_token,oauth_verifier):
    print("temp_oauth_token : " + temp_oauth_token +" ,oauth_verifier :"+oauth_verifier)
    infos = oauth.getUserInfos(temp_oauth_token)
    result = oauth.getOAuthToken(infos["resource_owner_key"],infos["resource_owner_secret"],oauth_verifier)
    oauth.updateUser(infos["id"],result)
    return
    
    

    
    