from fastapi import FastAPI

from .routers import status, patient
from .constants import PROJECT_NAME, VERSION_NAME


def start_application(title, version):
    application = FastAPI(title=title, version=version)
    application.include_router(status.router)
    application.include_router(patient.router)
    return application


app = start_application(title=PROJECT_NAME, version=VERSION_NAME)
