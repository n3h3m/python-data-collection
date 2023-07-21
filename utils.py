from sqlalchemy import Table
from sqlmodel import Session

import db_internal


def truncate_table(table: Table):
    with Session(db_internal.engine) as session:
        session.execute(table.delete())
        session.commit()
