# api/models/buildings.py
# This file contains the Pydantic models for the buildings.
# Imports from local packages


# Imports from third party packages
from pydantic import BaseModel


class Buildings(BaseModel):
    id: int
    name: str
    level: int
    cost: int
    revenue_modifier: float

    class Config:
        model_config = {'from_attributes': True}
