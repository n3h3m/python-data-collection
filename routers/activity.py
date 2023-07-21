from fastapi import HTTPException, status, APIRouter
from sqlmodel import select, Session

import db_internal
from models import Activity

router = APIRouter()


@router.get("/", response_model=list[Activity])
async def get_activities():
    with Session(db_internal.engine) as session:
        statement = select(Activity)
        results = session.execute(statement)
        results = list(i[0] for i in results.all())
    if len(results) == 0:
        return []
    return results


@router.get("/{activity_id}", response_model=Activity)
async def get_activity(activity_id: int):
    with Session(db_internal.engine) as session:
        activity = session.get(Activity, activity_id)
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_activity(activity_id: int):
    with Session(db_internal.engine) as session:
        row = session.get(Activity, activity_id)
        if not row:
            raise HTTPException(status_code=404, detail="activity_id not found")
        session.delete(row)
        session.commit()
        return


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Activity)
async def create_activity(activity: Activity):
    with Session(db_internal.engine) as session:
        session.add(activity)
        session.commit()
        session.refresh(activity)
        return activity
