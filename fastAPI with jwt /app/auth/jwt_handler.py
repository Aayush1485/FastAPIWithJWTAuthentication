#This file is responsible for handling ,securing,encoding,decoding and returning jwt Tokens.  

import time #importing time to set the expiry of any jwt tokens
import jwt  #responsible for encoding and decoding jwt tokens.
from decouple import config

 
JWT_SECRET=config("secret")
JWT_ALGO=config("algorithm")

#Function responsible to returns the generate token (JWT's)
def token_res(token:str):
    return{
        "access_token":token
    }



#fucntion used for signing jwt token
def signJWT(userId:str):
    payload={
        "userId":userId,
        "expiry":time.time()+600
    }
    print('payload:',payload)
    
    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGO)
    return token_res(token)

def decode_jwt(token:str):
    try:
        decode_token=jwt.decode(token,JWT_SECRET,algorithm=JWT_ALGO)
        return decode_token if decode_token['expires']>=time.time() else None
    except:
        return{}

