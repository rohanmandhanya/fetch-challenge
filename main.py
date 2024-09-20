from fastapi import FastAPI
import logging
import time

from api import router


def start_app():

    app = FastAPI()
    app.include_router(
        router,
        prefix="/receipts",
        responses={404: {"description": "Not found"}},
    )

    return app


app = start_app()


@app.get("/", include_in_schema=False)
def hello_world():
    logging.info("App running fine")
    return {"message": "Hello World"}
