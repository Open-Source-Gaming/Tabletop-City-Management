# api.cities.py
# This file contains the repository for cities.
# Imports from local packages
from db.migrations import Cities as CitiesDbModel


# Imports from third party packages
from sqlalchemy.orm import Session


class CitiesRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_cities(query) -> list[CitiesDbModel]:
        return query.all()

    @staticmethod
    def get_city_by_id(query) -> CitiesDbModel:
        return query.one()

    @staticmethod
    def create_city(session: Session, city: CitiesDbModel) -> None:
        session.add_all([city])
        session.commit()
