# api/controllers/buildings.py
# This file is responsible for handling requests related to buildings.
# Imports from local packages
from api.services.buildings import BuildingsService
from api.models.buildings import Buildings as BuildingsModel
from api.models.enums import BuildingType, BuildingLevel, BuildingCostFilter, BuildingLevelFilter


# Imports from third party packages
from fastapi import status, APIRouter


router = APIRouter(
    prefix="/buildings",
    tags=["buildings"],
)


service = BuildingsService()


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[BuildingsModel])
async def get_buildings(building_type: BuildingType | None = None, leve_filter: BuildingLevelFilter | None = None,
                        level: BuildingLevel | None = None,
                        cost_filter: BuildingCostFilter | None = None,
                        cost: int | None = None) -> list[BuildingsModel]:
    return service.get_buildings(building_type=building_type, level_filter=leve_filter, level=level,
                                 cost_filter=cost_filter, cost=cost)


@router.get("/{building_id}", status_code=status.HTTP_200_OK, response_model=BuildingsModel)
async def get_building_by_id(building_id: int):
    return service.get_building_by_id(building_id)
