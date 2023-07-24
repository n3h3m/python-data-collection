from fastapi import status
from fastapi.testclient import TestClient

from main import app
from models import Farm
from utils import truncate_table


def create_farm(client) -> dict:
    response = client.post("/farms", json={
        "name": "string",
        "farmer_id": 0,
        "size": 0,
        "city": "string",
        "state": "string",
        "zip_code": "string"
    })
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()


def get_all_farms(client) -> dict:
    response = client.get("/farms")
    assert response.status_code == status.HTTP_200_OK
    return response.json()


def delete_farm(client, farm_id: int):
    response = client.delete(f"/farms/{farm_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_crud_farm():
    with TestClient(app) as client:
        truncate_table(Farm.__table__)
        response = get_all_farms(client)
        assert len(response) == 0

        # create an entry
        response = create_farm(client)
        farm_id = response["id"]

        # get entry
        response = get_all_farms(client)
        assert len(response) == 1
        assert response[0]["id"] == farm_id
        assert response[0]["name"] == "string"

        # delete entry
        response = delete_farm(client, farm_id=farm_id)
        response = get_all_farms(client)
        assert len(response) == 0
