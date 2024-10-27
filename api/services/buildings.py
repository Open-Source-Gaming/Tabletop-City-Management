# api/services/buildings.py
# This file contains the service for interacting with buildings.
# Imports from local packages
from api.factories.buildings import BuildingsFactory
from api.models.buildings import Buildings as BuildingModel
from api.repositories.buildings import BuildingsRepository
from api.services import apply_filter
from db.config import DatabaseConfig
from db.migrations import Buildings


# Imports from third party packages


db = DatabaseConfig()
factory = BuildingsFactory()
repo = BuildingsRepository()


class BuildingsService:
    def __init__(self):
        pass

    @staticmethod
    def get_buildings(
            building_type: str | None = None,
            level_filter: str | None = None,
            level: int | None = None,
            cost_filter: str | None = None,
            cost: int | None = None,
    ) -> list[BuildingModel]:
        session = db.create_session()

        query = session.query(Buildings)

        if building_type:
            query = query.filter(Buildings.name == building_type)  # type: ignore

        if level_filter is not None:
            query = apply_filter(query, Buildings.level, level, level_filter)  # type: ignore

        if cost is not None:
            query = apply_filter(query, Buildings.cost, cost, cost_filter)  # type: ignore

        return factory.buildings_factory(repo.get_buildings(query=query))

    @staticmethod
    def get_building_by_id(building_id: int) -> BuildingModel:
        building = repo.get_building_by_id(building_id)
        return factory.building_factory(building)
