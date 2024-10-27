# api/factories/cities.py
# This file contains the factory for creating buildings.
# Imports from local packages
from db.migrations import Cities as CitiesDbModel
from api.models.buildings import Buildings as BuildingPydanticModel
from api.models.city import City as CityPydanticModel, CityWithMetadata as CityWithMetadataPydanticModel


# Imports from third party packages


class CitiesFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_city_with_metadata(city: CityPydanticModel, buildigs: list[BuildingPydanticModel]) \
            -> CityWithMetadataPydanticModel:
        return CityWithMetadataPydanticModel(city=city, buildings=buildigs)

    @staticmethod
    def from_db_to_pydantic_city_model(city: CitiesDbModel) -> CityPydanticModel:
        city_dict = city.__dict__.copy()
        city_dict.pop('_sa_instance_state', None)
        return CityPydanticModel(**city_dict)

    @staticmethod
    def from_pydantic_to_db_city_model(city_data: CityPydanticModel) -> CitiesDbModel:
        return CitiesDbModel(**city_data.model_dump())

    @staticmethod
    def from_dict_to_db_city_model(city_data: dict) -> CitiesDbModel:
        return CitiesDbModel(**city_data)

    def from_list_db_to_list_pydantic_city_model(self, cities: list[CitiesDbModel]) -> list[CityPydanticModel]:
        return [self.from_db_to_pydantic_city_model(city) for city in cities]
