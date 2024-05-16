from pydantic import BaseModel , Field ,EmailStr


#USING PYDANTIC FOR VALIDATION PURPOSE
class PostSchema(BaseModel):
    id:int = Field(default=None)
    title:str = Field(default=None)
    content:str = Field(default=None)
     
    class Config:
        schema_extra={
            "post_demo":{
                "title":"some title about animals",
                "content":"some content about animals"
            }
        }
    

class UserSchema(BaseModel):
    full_name:str= Field(default=None)
    email:EmailStr=Field(defautl=None)
    password:str =Field(default=None)
    class Config:
        the_schema={
            'user_demo':{
                'name':'aaYUSH',
                'email':'a@a.com',
                'password':123
            }
        }

class UserLoginSchema(BaseModel):
    email:EmailStr=Field(defautl=None)
    password:str =Field(default=None)
    class Config:
        the_schema={
            'user_demo':{
                'email':'b@b.com',
                'password':1234
            }
        }
    