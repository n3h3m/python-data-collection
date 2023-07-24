from fastapi import status
from fastapi.testclient import TestClient

from main import app
from models import Activity
from utils import truncate_table


def create_activity(client) -> dict:
    response = client.post("/activities", json={
        "activity_type": "planting",
        "crop_id": 0,
        "farmer_id": 0,
        "farm_id": 0,
        "contractor_id": 0,
        "date_time": "2023-07-24T01:00:46.674Z",
        "notes": "string"
    })
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()


def get_all_activitys(client) -> dict:
    response = client.get("/activities")
    assert response.status_code == status.HTTP_200_OK
    return response.json()


def delete_activity(client, activity_id: int):
    response = client.delete(f"/activities/{activity_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_crud_activity():
    with TestClient(app) as client:
        truncate_table(Activity.__table__)
        response = get_all_activitys(client)
        assert len(response) == 0

        # create an entry
        response = create_activity(client)
        activity_id = response["id"]

        # get entry
        response = get_all_activitys(client)
        assert len(response) == 1
        assert response[0]["id"] == activity_id
        assert response[0]["activity_type"] == "planting"

        # delete entry
        response = delete_activity(client, activity_id=activity_id)
        response = get_all_activitys(client)
        assert len(response) == 0
