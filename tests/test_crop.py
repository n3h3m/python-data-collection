from fastapi import status
from fastapi.testclient import TestClient

from main import app
from models import Crop
from utils import truncate_table


def create_crop(client) -> dict:
    response = client.post("/crops", json={
        "name": "string",
        "variety": "string",
        "planting_season": "spring",
        "harvest_season": "spring"
    })
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()


def get_all_crops(client) -> dict:
    response = client.get("/crops")
    assert response.status_code == status.HTTP_200_OK
    return response.json()


def delete_crop(client, crop_id: int):
    response = client.delete(f"/crops/{crop_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_crud_crop():
    with TestClient(app) as client:
        truncate_table(Crop.__table__)
        response = get_all_crops(client)
        assert len(response) == 0

        # create an entry
        response = create_crop(client)
        crop_id = response["id"]

        # get entry
        response = get_all_crops(client)
        assert len(response) == 1
        assert response[0]["id"] == crop_id
        assert response[0]["name"] == "string"

        # delete entry
        response = delete_crop(client, crop_id=crop_id)
        response = get_all_crops(client)
        assert len(response) == 0
