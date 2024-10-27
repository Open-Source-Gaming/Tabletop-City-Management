# api.repositories
# This file contains the repository for interacting with the buildings table in the database.
# Imports from local packages


# Imports from third party packages
from sqlalchemy.orm import Session


def get_scalars(session: Session, query: any) -> list[any]:
    return session.execute(query).scalars().all()  # type: ignore
