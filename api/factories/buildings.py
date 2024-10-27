# api/factories/buildings.py
# This file contains the factory for creating buildings.
# Imports from local packages
from db.migrations import Buildings as BuildingsDbModel
from api.models.buildings import Buildings as BuildingsPydanticModel


class BuildingsFactory:
    def __init__(self):
        pass

    @staticmethod
    def building_factory(building: BuildingsDbModel) -> BuildingsPydanticModel:
        building_dict = building.__dict__.copy()
        building_dict.pop('_sa_instance_state', None)
        return BuildingsPydanticModel(**building_dict)

    def buildings_factory(self, buildings: list[BuildingsDbModel]) -> list[BuildingsPydanticModel]:
        return [self.building_factory(building) for building in buildings]
