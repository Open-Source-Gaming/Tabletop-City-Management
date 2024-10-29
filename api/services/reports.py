# api/services/reports.py
# This file is responsible for handling requests related to buildings.
# Imports from local packages
from api.models.enums import ReportType
from api.services.cities import CitiesService


# Imports from third party packages
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os


city_service = CitiesService()


class ReportsService:
    def __init__(self):
        pass

    @staticmethod
    def get_full_report(city_id: int, report_type: ReportType) -> str | bytes:
        template_path = os.path.join(os.path.dirname(__file__), "../../templates")
        env = Environment(loader=FileSystemLoader(template_path))
        template = env.get_template("city_report.html")
        city_info = city_service.get_city_with_metadata(city_id)
        html_content = template.render(city=city_info.city, buildings=city_info.buildings)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        report_dir = os.path.join(os.path.dirname(__file__), "../../reports")
        os.makedirs(report_dir, exist_ok=True)

        match report_type:
            case ReportType.html:
                file_path = os.path.join(report_dir, f"city_report_{timestamp}.html")
                with open(file_path, "w") as file:
                    file.write(html_content)
                return html_content

            case ReportType.pdf:
                file_path = os.path.join(report_dir, f"city_report_{timestamp}.pdf")
                pdfkit.from_string(html_content, file_path)
                with open(file_path, "rb") as pdf_file:
                    return pdf_file.read()
