from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT

from auth_routes import auth_router
from order_routes import order_router
from schemas import Settings

app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth_router)
app.include_router(order_router)

@app.get('/')
async def root():
    return {'message': 'Delivery project is running in my local machine'}
