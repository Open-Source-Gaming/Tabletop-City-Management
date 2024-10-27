# api.services.py
# This file contains the service for interacting with cities.
# # Imports from local packages
from api.factories.cities import CitiesFactory
from api.factories.city_buildings import CityBuildingsFactory
from api.models.buildings import Buildings as BuildingPydanticModel
from api.models.city import City as CityPydanticModel, CityWithMetadata as CityWithMetadataPydanticModel
from api.models.enums import BuildingLevel
from api.repositories import get_scalars
from api.repositories.cities import CitiesRepository
from api.services import verify_session
from api.services.buildings import BuildingsService
from api.services.city_buildings import CityBuildingsService
from db.config import DatabaseConfig
from db.migrations import Cities as CityDbModel, Buildings as BuildingDbModel


# Imports from third party packages
from sqlalchemy import select


building_service = BuildingsService()
cb_service = CityBuildingsService()
city_repo = CitiesRepository()
db = DatabaseConfig()
city_factory = CitiesFactory()
cb_factory = CityBuildingsFactory()


class CitiesService:
    def __init__(self):
        pass

    @staticmethod
    def get_cities() -> list:
        session = db.create_session()
        try:
            session = db.create_session()

            query = session.query(CityDbModel)

            cities = city_repo.get_cities(query)
        finally:
            session.close()

        return city_factory.from_list_db_to_list_pydantic_city_model(cities)

    @staticmethod
    def get_city_by_id(city_id: int) -> CityPydanticModel:
        session = verify_session()

        try:
            query = session.query(CityDbModel)

            query = query.filter(CityDbModel.id == city_id)  # type: ignore

            return city_factory.from_db_to_pydantic_city_model(city_repo.get_city_by_id(query))
        finally:
            session.close()

    @staticmethod
    def get_city_with_metadata(city_id: int) -> CityWithMetadataPydanticModel:
        session = verify_session()

        try:
            query = session.query(CityDbModel)

            query = query.filter(CityDbModel.id == city_id)  # type: ignore

            city = city_factory.from_db_to_pydantic_city_model(city_repo.get_city_by_id(query))

            buildings: list[BuildingPydanticModel] = []

            buildings_id: list[int] = []

            city_buildings = cb_service.get_city_buildings_by_city_id(city_id, session)

            for building in city_buildings:
                buildings_id.append(building.building_id)

            for building_id in buildings_id:
                buildings.append(building_service.get_building_by_id(building_id))

            return city_factory.create_city_with_metadata(city, buildings)
        finally:
            session.close()

    @staticmethod
    def create_city(city: CityPydanticModel) -> int:
        session = db.create_session()
        try:
            city_data = city.model_dump(exclude={"id"})

            db_city = city_factory.from_dict_to_db_city_model(city_data)

            city_repo.create_city(session, db_city)

            select_buildings = (select(BuildingDbModel.id)
                                .where(BuildingDbModel.level == BuildingLevel.level_0))  # type: ignore

            buildings_ids = get_scalars(session, select_buildings)

            for building_id in buildings_ids:
                city_building_model = cb_factory.create_pydantic_city_buildings_model(cb_id=0, city_id=db_city.id,
                                                                                      building_id=building_id)
                cb_service.create_city_building(city_building_model, session)

            return city_factory.from_db_to_pydantic_city_model(db_city).id
        finally:
            session.close()
