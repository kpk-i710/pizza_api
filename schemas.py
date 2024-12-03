from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = None
    is_active: Optional[bool] = None

    class Config:
        org_mode = True
        json_schema_extra = {  # Обновлено в Pydantic 2
            'example': {
                "username": "johndoe",
                "email": "john@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True,
            }
        }