# api.models.city_buildings.py
# This file contains the models for city buildings.
# Imports from local packages


# Imports from third party packages
from pydantic import BaseModel


class CityBuildings(BaseModel):
    id: int
    city_id: int
    building_id: int
