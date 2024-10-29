# api/controllers/reports.py
# This file is responsible for handling requests related to buildings.
# Imports from local packages
from api.models.enums import ReportType
from api.services.reports import ReportsService


# Imports from third party packages
from fastapi import status, APIRouter, Response


router = APIRouter(
    prefix="/reports",
    tags=["reports"],
)


service = ReportsService()


@router.get("/{city_id}", status_code=status.HTTP_200_OK)
async def get_full_report(city_id: int, report_type: ReportType):
    pass
    match report_type:
        case ReportType.html:
            return Response(content=service.get_full_report(city_id, report_type), media_type="text/html")
        case ReportType.pdf:
            return Response(content=service.get_full_report(city_id, report_type), media_type="application/pdf")
        case _:
            return Response(status_code=status.HTTP_400_BAD_REQUEST, content="Invalid report type")
