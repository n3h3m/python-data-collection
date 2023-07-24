from fastapi import status
from fastapi.testclient import TestClient

from main import app
from models import Activity
from utils import truncate_table


def create_activity(client) -> dict:
    response = client.post("/activities", json={
        "activity_type": "Planting",
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
        assert response[0]["activity_type"] == "Planting"

        # delete entry
        response = delete_activity(client, activity_id=activity_id)
        response = get_all_activitys(client)
        assert len(response) == 0


def test_tilling_validators():
    with TestClient(app) as client:
        # Case 0:
        # Tilling activity will succeed when
        # - activity type is Tilling
        # - till_type is present and one of Plowing|Harrowing|Conventional|Reduced
        # - till_depth is >= 0 and < 10
        response = client.post("/activities", json={
            "activity_type": "Tilling",
            "crop_id": 0,
            "farmer_id": 0,
            "farm_id": 0,
            "contractor_id": 0,
            "date_time": "2023-07-24T01:00:46.674Z",
            "till_type": "Reduced",
            "till_depth": 4
        })
        assert response.status_code == status.HTTP_201_CREATED

        # Case 1:
        # Tilling activity will fail when
        # - activity type is Tilling
        # - till_type is missing
        response = client.post("/activities", json={
            "activity_type": "Tilling",
            "crop_id": 0,
            "farmer_id": 0,
            "farm_id": 0,
            "contractor_id": 0,
            "date_time": "2023-07-24T01:00:46.674Z",
            "till_depth": 4
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert "till_type and till_depth are mandatory for activity_type 'Tilling'" in response.json()["detail"][0][
            "msg"]

        # Case 2:
        # Tilling activity will fail when
        # - activity type is Tilling
        # - till_type is present
        # - till_type is not in Plowing|Harrowing|Conventional|Reduced
        response = client.post("/activities", json={
            "activity_type": "Tilling",
            "crop_id": 0,
            "farmer_id": 0,
            "farm_id": 0,
            "contractor_id": 0,
            "date_time": "2023-07-24T01:00:46.674Z",
            "till_depth": 4,
            "till_type": "xxx",
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        # Case 3:
        # Tilling activity will fail when
        # - activity type is Tilling
        # - till_type is present and valid
        # - till_depth is present
        # - till_depth is greater than 10 or equal to 10
        response = client.post("/activities", json={
            "activity_type": "Tilling",
            "crop_id": 0,
            "farmer_id": 0,
            "farm_id": 0,
            "contractor_id": 0,
            "date_time": "2023-07-24T01:00:46.674Z",
            "till_depth": 11,
            "till_type": "Reduced",
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        response = client.post("/activities", json={
            "activity_type": "Tilling",
            "crop_id": 0,
            "farmer_id": 0,
            "farm_id": 0,
            "contractor_id": 0,
            "date_time": "2023-07-24T01:00:46.674Z",
            "till_depth": 10,
            "till_type": "Reduced",
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
