# api.city_buildings.py
# This file contains the repository for city_buildings.
# Imports from local packages
from api.models.city import City as CitiesPydanticModel
from db.migrations import CityBuildings as CityBuildingsDbModel


# Imports from third party packages
from sqlalchemy.orm import Session


class CityBuildingsRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_city_buildings(query) -> list[CityBuildingsDbModel]:
        return query.all()

    @staticmethod
    def get_city_building_by_id(query) -> CityBuildingsDbModel:
        return query.first()

    @staticmethod
    def create_city_building(session: Session, city_building: CityBuildingsDbModel) -> None:
        session.add_all([city_building])
        session.commit()
