# api/controllers/cities.py
# This file contains the controller for cities.
# Imports from local packages
from api.models.city import City as CitiesModel, CityWithMetadata as CityWithMetadataModel
from api.services.cities import CitiesService


# Imports from third party packages
from fastapi import status, APIRouter


router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


service = CitiesService()


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CitiesModel])
async def get_cities():
    return service.get_cities()


@router.get("/{city_id}", status_code=status.HTTP_200_OK, response_model=CitiesModel)
async def get_city_by_id(city_id: int):
    return service.get_city_by_id(city_id)


@router.get("/{city_id}/metadata", status_code=status.HTTP_200_OK, response_model=CityWithMetadataModel)
async def get_city_metadata(city_id: int):
    return service.get_city_with_metadata(city_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=int)
async def create_city(city: CitiesModel):
    return service.create_city(city)
