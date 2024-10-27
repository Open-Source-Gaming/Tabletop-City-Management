# api/models/cities.py
# This file contains the Pydantic models for the cities.
# Imports from local packages
from api.models.buildings import Buildings


# Imports from third party packages
from pydantic import BaseModel


class City(BaseModel):
    id: int
    name: str
    type: str
    population: int
    tax_per_month: int

    class Config:
        model_config = {'from_attributes': True}


class CityWithMetadata(BaseModel):
    city: City
    buildings: list[Buildings]

    class Config:
        model_config = {'from_attributes': True}
