# api/services/revenue.py
# Description: This file contains the service for calculating revenue.
# Imports from third party packages


# Imports from project directory
from api.models.buildings import Buildings
from api.utils.config import Config


config = Config()


class RevenueService:
    def __init__(self):
        pass

    @staticmethod
    def calculate_revenue(population: int, time_passed: int, buildings: list[Buildings]) -> float:
        revenue = population * config.city_base_revenue_rate() * time_passed
        revenue_modifier = 0

        for building in buildings:
            revenue_modifier += building.revenue_modifier

        revenue = revenue + (revenue * revenue_modifier)

        return revenue
