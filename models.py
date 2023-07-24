from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field


# Enum for different types of farming activities
class ActivityType(str, Enum):
    planting = "planting"
    watering = "watering"
    fertilizing = "fertilizing"
    harvesting = "harvesting"


# Enum for different seasons
class Season(str, Enum):
    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"
    fall = "fall"
    year_round = "year-round"


# Enum for different tilling types
class TillingType(str, Enum):
    plowing = "plowing"
    harrowing = "harrowing"
    conventional = "conventional"
    reduced = "reduced"


# Contractor model to represent external contractors
class Contractor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone_number: Optional[str]
    address: Optional[str]
    service_provided: Optional[str]


# Farmer model
class Farmer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone_number: Optional[str]
    address: Optional[str]


# Farm model
class Farm(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    farmer_id: int = Field(foreign_key="farmer.id")
    size: Optional[float]
    city: str
    state: str
    zip_code: str


# Crop model
class Crop(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    variety: str
    planting_season: Optional[Season]
    harvest_season: Optional[Season]


# Activity model to track farming activities
class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    activity_type: ActivityType
    crop_id: int = Field(foreign_key="crop.id")
    farmer_id: int = Field(foreign_key="farmer.id")
    farm_id: int = Field(foreign_key="farm.id")
    contractor_id: Optional[int] = Field(default=None, foreign_key="contractor.id")
    date_time: datetime
    notes: Optional[str]
