from typing import List
import fastapi as _fastapi
from auth_routes import auth_router
from order_routes import order_router

app = _fastapi.FastAPI()

@app.get('/')
def read_root():
    return {"Hello":"world"}

app.include_router(auth_router)
app.include_router=(order_router)


