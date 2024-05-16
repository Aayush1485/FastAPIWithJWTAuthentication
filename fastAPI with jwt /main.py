#Yotube Video Link: https://www.youtube.com/watch?v=0_seNFCtglk

#uvicorn for serving the app on local
import uvicorn
from fastapi import FastAPI,Body,Depends
from app.model import PostSchema
from app.model import UserSchema,UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

  
posts=[  
    {
        "id":1,
        "title":'penguns',
        "content":"all about penguins"

    },
    {
        "id":2,
        "title":'tigers',
        "content":"all about tigers"

    },
        {
        "id":3,
        "title":'lions',
        "content":"all about lions"

    }
]  

app=FastAPI()


users=[]


#creating get type url using @app decorator-object of fastAPI
@app.get('/',tags=['test'])
def greet():
    return {"hello welcome to the FAST-API tutorial"}


#TO Get all POST 
@app.get('/posts',tags=["all_posts"])
def get_all_post():
    return posts

#TO get one post by id
@app.get('/get_post_by_id/{id}',tags=["get_post_by_id"])
def get_one_post(id:int):
    if id >len(posts):
        return{"post is not availabe with this post"}
    else:
        for ps in posts:
            if ps["id"] == id:
                return {"data":ps}
    

#To create Post
@app.post('/create_post',dependencies=[Depends(jwtBearer)],tags=['create_post'])

#use PostSchema in function for Pydantic Validation
def create_post(post:PostSchema):
    post.id=len(posts)+1
    posts.append(post.dict())
    return {"info":'post Added!',
            "data":posts
            }   

#To signup new user 
@app.post('/user/signup',tags=['user_signup'])
def user_signup(user:UserSchema = Body(default=None)):
    print('user:',user)
    users.append(user)
    return signJWT(user.email)

def check_user(data):
    for user in users:
        if user.email ==data.email and user.password == data.password:
            return True
        else:
            False

@app.post("/user/login",tags=["user"])
def user_login(user:UserLoginSchema=Body(default=None)):
  if check_user(user):
      return signJWT(user.email)  
  else:
      return {
          "error":'Invalid Login Credentials!'
      }
  

#Next for checking each request maded by is valid and authorized or not , for that we can use HTTP bearer class.







