from fastapi import FastAPI
from  app.controllers import addition_controller

app = FastAPI()

app.include_router(addition_controller.router)