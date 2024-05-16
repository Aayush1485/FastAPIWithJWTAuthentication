#The function of this file is to check whether the request is authorized or not [Verification of the Protected Route.]

from fastapi import Request,HTTPException #importing Request to authorized the request made by user .
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer 
from app.auth.jwt_handler import decode_jwt

class jwtBearer(HTTPBearer):
    def __init(self,auto_Error:bool=True):
        super(jwtBearer,self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer,self).__call__(request)
    
        if credentials:
            if not credentials.scheme=="Bearer":
                raise HTTPException(status_code=403,details="Invalid or Expired Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403,details="Invalid or Expired Token")
        
    def verify_jwt(self,jwttoken:str):
        istokenvalid:bool =False
        payload=decode_jwt(jwttoken)
        if payload:
            istokenvalid:True
        return istokenvalid
