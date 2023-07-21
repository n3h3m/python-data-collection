from fastapi import HTTPException, status, APIRouter
from sqlmodel import select, Session

import db_internal
from models import Farmer

router = APIRouter()


@router.get("/", response_model=list[Farmer])
async def get_farmers():
    with Session(db_internal.engine) as session:
        statement = select(Farmer)
        results = session.execute(statement)
        results = list(i[0] for i in results.all())
    if len(results) == 0:
        return []
    return results


@router.get("/{farmer_id}", response_model=Farmer)
async def get_farmer(farmer_id: int):
    with Session(db_internal.engine) as session:
        farmer = session.get(Farmer, farmer_id)
        if not farmer:
            raise HTTPException(status_code=404, detail="Farmer not found")
    return farmer


@router.delete("/{farmer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_farmer(farmer_id: int):
    with Session(db_internal.engine) as session:
        row = session.get(Farmer, farmer_id)
        if not row:
            raise HTTPException(status_code=404, detail="farmer_id not found")
        session.delete(row)
        session.commit()
        return


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Farmer)
async def create_farmer(farmer: Farmer):
    with Session(db_internal.engine) as session:
        session.add(farmer)
        session.commit()
        session.refresh(farmer)
        return farmer
