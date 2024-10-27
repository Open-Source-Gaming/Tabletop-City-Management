# api/repositories/buildings.py
# This file contains the repository for interacting with the buildings table in the database.
# Imports from local packages
from db.config import DatabaseConfig
from db.migrations import Buildings


# Imports from third party packages


db = DatabaseConfig()


class BuildingsRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_buildings(query: str) -> list[Buildings]:
        session = db.create_session()
        try:
            return query.all()  # type: ignore
        finally:
            session.close()

    @staticmethod
    def get_building_by_id(building_id: int) -> Buildings:
        session = db.create_session()
        try:
            return session.query(Buildings).filter(Buildings.id == building_id).one()  # type: ignore
        finally:
            session.close()
