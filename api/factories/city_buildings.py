# api/factories/city_buildings.py
# This file contains the factory for creating city buildings.
# Imports from local packages
from api.models.city_buildings import CityBuildings as CityBuildingsPydanticModel
from db.migrations import CityBuildings as CityBuildingsDbModel


# Imports from third party packages


class CityBuildingsFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_pydantic_city_buildings_model(cb_id: int, city_id: int, building_id: int) -> CityBuildingsPydanticModel:
        return CityBuildingsPydanticModel(id=cb_id, city_id=city_id, building_id=building_id)

    @staticmethod
    def from_db_to_pydantic_city_buildings_model(city_building: CityBuildingsDbModel) -> CityBuildingsPydanticModel:
        city_building_dict = city_building.__dict__.copy()
        city_building_dict.pop('_sa_instance_state', None)
        return CityBuildingsPydanticModel(**city_building_dict)

    @staticmethod
    def from_pydantic_to_db_city_buildings_model(city_building_data: CityBuildingsPydanticModel) -> CityBuildingsDbModel:
        return CityBuildingsDbModel(**city_building_data.model_dump())

    @staticmethod
    def from_dict_to_db_city_buildings_model(city_building_data: dict) -> CityBuildingsDbModel:
        return CityBuildingsDbModel(**city_building_data)

    def from_list_db_to_list_pydantic_city_buildings_model(self, city_buildings: list[CityBuildingsDbModel]) \
            -> list[CityBuildingsPydanticModel]:
        return [self.from_db_to_pydantic_city_buildings_model(city_building) for city_building in city_buildings]
