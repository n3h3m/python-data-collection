from fastapi import HTTPException, status, APIRouter
from sqlmodel import select, Session

import db_internal


def crud(model):
    router = APIRouter()

    @router.get("/", response_model=list[model])
    async def get_items():
        with Session(db_internal.engine) as session:
            statement = select(model)
            results = session.execute(statement)
            results = list(i[0] for i in results.all())
        if len(results) == 0:
            return []
        return results

    @router.get("/{item_id}", response_model=model)
    async def get_item(item_id: int):
        with Session(db_internal.engine) as session:
            item = session.get(model, item_id)
            if not item:
                raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
        return item

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_item(item_id: int):
        with Session(db_internal.engine) as session:
            row = session.get(model, item_id)
            if not row:
                raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
            session.delete(row)
            session.commit()
            return

    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=model)
    async def create_item(item: model):
        with Session(db_internal.engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

    return router
