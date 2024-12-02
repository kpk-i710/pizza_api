from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum as EnumType
from sqlalchemy.orm import relationship
from typing import Optional

class SignUpModel (BaseModel):
    id = Optional[int]
    username :str
    email = str
    password = str
    is_staff:Optional[bool]
    is_active = Optional[bool]


    class Config:
        org_mode=True
        schema_extra = {
            'example':{
                "username":"johndoe",
                "email":"john@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True,
            }
        }

