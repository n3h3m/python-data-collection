from fastapi import HTTPException, status, APIRouter
from sqlmodel import select, Session

import db_internal
from models import Crop

router = APIRouter()


@router.get("/", response_model=list[Crop])
async def get_crops():
    with Session(db_internal.engine) as session:
        statement = select(Crop)
        results = session.execute(statement)
        results = list(i[0] for i in results.all())
    if len(results) == 0:
        return []
    return results


@router.get("/{crop_id}", response_model=Crop)
async def get_crop(crop_id: int):
    with Session(db_internal.engine) as session:
        crop = session.get(Crop, crop_id)
        if not crop:
            raise HTTPException(status_code=404, detail="Crop not found")
    return crop


@router.delete("/{crop_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_crop(crop_id: int):
    with Session(db_internal.engine) as session:
        row = session.get(Crop, crop_id)
        if not row:
            raise HTTPException(status_code=404, detail="crop_id not found")
        session.delete(row)
        session.commit()
        return


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Crop)
async def create_crop(crop: Crop):
    with Session(db_internal.engine) as session:
        session.add(crop)
        session.commit()
        session.refresh(crop)
        return crop
