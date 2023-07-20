from fastapi import FastAPI
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session

import db_internal
from fixtures import generate_users, farming_data
from models import User

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


@app.get("/users", response_model=list[User])
async def get_users():
    with Session(db_internal.engine) as session:
        statement = select(User)
        results = session.execute(statement)
        results = list(i[0] for i in results.all())
    if len(results) == 0:
        return []
    return results


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    with Session(db_internal.engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    with Session(db_internal.engine) as session:
        row = session.get(User, user_id)
        if not row:
            raise HTTPException(status_code=404, detail="user_id not found")
        session.delete(row)
        session.commit()
        return


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: User):
    with Session(db_internal.engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
