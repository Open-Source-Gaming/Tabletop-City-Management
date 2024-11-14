# api/controllers/forward_time.py
# Description: This file contains the controller for forwarding time.
# Imports from project directory
from api.models.forward_time import ForwardTime
from api.services.forward_time import ForwardTimeService


# Imports from third party packages
from fastapi import status, APIRouter


router = APIRouter(
    prefix="/forwardTime",
    tags=["forward time"],
)


service = ForwardTimeService()


@router.get("/", status_code=status.HTTP_200_OK, response_model=ForwardTime)
async def forward_time(city_id: int, players: int):
    return service.forward_time(city_id, players)
