from fastapi import FastAPI
from sqlmodel import Session

import db_internal
from fixtures import fixtures_data
from models import Farmer, Crop, Activity, Contractor, Farm
from routers.generic_router import crud

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    db_internal.create_db()
    with Session(db_internal.engine) as session:
        for model_name, data in fixtures_data.items():
            model_cls = globals()[model_name]
            for entry_data in data:
                entry = model_cls(**entry_data)
                session.add(entry)

        session.commit()


app.include_router(crud(Farmer), prefix="/farmers", tags=["Farmers"])
app.include_router(crud(Farm), prefix="/farms", tags=["Farms"])
app.include_router(crud(Contractor), prefix="/contractors", tags=["Contractors"])
app.include_router(crud(Crop), prefix="/crops", tags=["Crops"])
app.include_router(crud(Activity), prefix="/activities", tags=["Activities"])
