from fastapi import status
from fastapi.testclient import TestClient

from main import app
from models import Farmer
from utils import truncate_table


def create_farmer(client) -> dict:
    response = client.post("/farmers", json={
        "name": "string",
        "email": "string",
        "phone_number": "string",
        "address": "string"
    })
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()


def get_all_farmers(client) -> dict:
    response = client.get("/farmers")
    assert response.status_code == status.HTTP_200_OK
    return response.json()


def delete_farmer(client, farmer_id: int):
    response = client.delete(f"/farmers/{farmer_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_crud_farmer():
    with TestClient(app) as client:
        truncate_table(Farmer.__table__)
        response = get_all_farmers(client)
        assert len(response) == 0

        # create an entry
        response = create_farmer(client)
        farmer_id = response["id"]

        # get entry
        response = get_all_farmers(client)
        assert len(response) == 1
        assert response[0]["id"] == farmer_id
        assert response[0]["name"] == "string"

        # delete entry
        response = delete_farmer(client, farmer_id=farmer_id)
        response = get_all_farmers(client)
        assert len(response) == 0
