from fastapi import FastAPI
from controllers.analysis_controller import router

app = FastAPI()

app.include_router(router)