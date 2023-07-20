from datetime import datetime
from typing import List

from sqlmodel import Session

from models import User, Farmer, Crop, Activity


def generate_users() -> List[User]:
    sample_users = [
        User(name="John"),
        User(name="Jane"),
        User(name="Alice"),
        User(name="Bob"),
    ]
    return sample_users


def farming_data():
    sample_data = []

    # Sample farmers
    farmer_1 = Farmer(id=1, name="John Doe", email="john@example.com", farm_size=50.0, location="Farmville")
    farmer_2 = Farmer(id=2, name="Jane Smith", email="jane@example.com", farm_size=75.0, location="Countryside")
    sample_data.extend([farmer_1, farmer_2])

    # Sample crops
    crop_1 = Crop(name="Corn", variety="Yellow Corn", id=1)
    crop_2 = Crop(name="Wheat", variety="Winter Wheat", id=2)
    crop_3 = Crop(name="Rice", variety="Long Grain", id=3)
    sample_data.extend([crop_1, crop_2, crop_3])

    # Sample activities
    activity_1 = Activity(activity_type="Planting", date_time=datetime(2023, 7, 20), crop_id=crop_1.id,
                          farmer_id=farmer_1.id)
    activity_2 = Activity(activity_type="Harvesting", date_time=datetime(2023, 10, 5), crop_id=crop_1.id,
                          farmer_id=farmer_1.id)
    activity_3 = Activity(activity_type="Irrigation", date_time=datetime(2023, 7, 25), crop_id=crop_2.id,
                          farmer_id=farmer_2.id)
    sample_data.extend([activity_1, activity_2, activity_3])

    return sample_data
