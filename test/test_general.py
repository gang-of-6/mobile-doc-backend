from fastapi.testclient import TestClient
from app.main import app
from app.app_models.EHR import Medicine


client = TestClient(app)


def test_index():
    """Checking if the status returns success"""
    response = client.get("/")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["success"] is True


def test_medicine():
    """Checks the status and class type of get_medicine endpoint"""
    response = client.get("/medicine/all")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["success"] is True
    # Ensuring that the element of all_medicines is of type Medicine
    med = response_json["all_medicines"][0]
    assert med == Medicine.parse_obj(med).dict()


def test_get_patient():
    """Checking if the status returns success"""
    response = client.get("/patient/0001")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["success"] is True


def test_get_patient_EHR():
    """Checking if the status returns success"""
    response = client.get("/patient/EHR/0001")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["success"] is True
