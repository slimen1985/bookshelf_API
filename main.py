from fastapi import FastAPI
from app.core.config import Settings
import logging


logger = logging.getLogger("bookshelf")


def start_application(config: Settings):
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description="Book store emulator"
    )
    return application


settings = Settings()

app = start_application(settings)


@app.get("/")
async def root():
    logger.info("Start application")
    return {"message": "Hello FastApi"}
