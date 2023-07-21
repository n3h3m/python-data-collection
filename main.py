from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

import db_internal
from fixtures import generate_users, farming_data
from models import User, Farmer, Crop, Activity
from routers.generic_router import crud

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    db_internal.create_db()
    sample_users = generate_users()
    sample_data = farming_data()
    with Session(db_internal.engine) as session:

        session.add_all(sample_users)
        session.commit()

        # Add one by one
        for item in sample_data:
            try:
                session.add(item)
                session.commit()
            except IntegrityError as e:
                session.rollback()
                print(f"IntegrityError: {e}")


app.include_router(crud(User), prefix="/users", tags=["Users"])
app.include_router(crud(Farmer), prefix="/farmers", tags=["Farmers"])
app.include_router(crud(Crop), prefix="/crops", tags=["Crops"])
app.include_router(crud(Activity), prefix="/activities", tags=["Activities"])
