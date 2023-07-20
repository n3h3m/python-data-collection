from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Farmer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    farm_size: float
    location: str


class Crop(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    variety: str


class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    activity_type: str
    date_time: datetime
    crop_id: int = Field(foreign_key="crop.id")
    farmer_id: int = Field(foreign_key="farmer.id")
