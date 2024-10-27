# api.services.city_buildings.py
# This file contains the service for city buildings.
# Imports from local packages
# from api.models.
from api.factories.city_buildings import CityBuildingsFactory
from api.models.city_buildings import CityBuildings as CityBuildingsPydanticModel
from api.repositories.city_buildings import CityBuildingsRepository
from api.services import verify_session
from db.config import DatabaseConfig
from db.migrations import CityBuildings as CityBuildingsDbModel


# Imports from third party packages
from sqlalchemy.orm import Session


db = DatabaseConfig()
factory = CityBuildingsFactory()
repo = CityBuildingsRepository()


class CityBuildingsService:
    def __init__(self):
        pass

    @staticmethod
    def get_city_buildings() -> list:
        pass

    @staticmethod
    def get_city_buildings_by_city_id(city_building_id: int, session: Session) -> list[CityBuildingsPydanticModel]:
        session = verify_session(session)

        query = session.query(CityBuildingsDbModel)
        query = query.filter(CityBuildingsDbModel.city_id == city_building_id)  # type: ignore
        return factory.from_list_db_to_list_pydantic_city_buildings_model(repo.get_city_buildings(query))

    @staticmethod
    def add_city_building_entry(city_building: CityBuildingsPydanticModel,
                                session: Session):
        city_building_data = city_building.model_dump(exclude={"id"})

        cb_db_model = factory.from_dict_to_db_city_buildings_model(city_building_data)

        repo.create_city_building(session, cb_db_model)

    def create_city_building(self, city_building: CityBuildingsPydanticModel,
                             session: Session | None = None) -> None:
        session = verify_session(session)

        try:
            self.add_city_building_entry(city_building, session)

        finally:
            session.close()

        self.add_city_building_entry(city_building, session)
