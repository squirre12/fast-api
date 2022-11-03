from fastapi import FastAPI

from endpoints import users_endpoint

app = FastAPI()
app.include_router(users_endpoint.router, prefix="/users", tags=["users"])
