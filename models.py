from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import constr, condecimal, validator
from sqlmodel import SQLModel, Field


# Enum for different types of farming activities
class ActivityType(str, Enum):
    planting = "Planting"
    irrigation = "Irrigation"
    fertilizing = "Fertilizing"
    harvesting = "Harvesting"
    tilling = "Tilling"


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
    plowing = "Plowing"
    harrowing = "Harrowing"
    conventional = "Conventional"
    reduced = "Reduced"


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
    till_type: constr(regex="^(Plowing|Harrowing|Conventional|Reduced)$") = None
    till_depth: condecimal(ge=0, lt=10, decimal_places=1) = None
    date_time: datetime
    notes: Optional[str]

    @validator('till_type', 'till_depth', pre=True, always=True)
    def check_tilling_fields(cls, value, values):
        if values.get('activity_type') == 'Tilling':
            if value is None:
                raise ValueError("till_type and till_depth are mandatory for activity_type 'Tilling'")
        return value

    class Config:
        orm_mode = True
