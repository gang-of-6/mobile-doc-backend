from fastapi import FastAPI

from .routers import status, patient, medicine, session
from .constants import PROJECT_NAME, VERSION_NAME


def start_application(title, version):
    application = FastAPI(title=title, version=version)
    application.include_router(status.router)
    application.include_router(patient.router)
    application.include_router(medicine.router)
    application.include_router(session.router)
    return application


app = start_application(title=PROJECT_NAME, version=VERSION_NAME)
