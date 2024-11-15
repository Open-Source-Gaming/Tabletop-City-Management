# api/services/forward_time.py
# Description: This file contains the service for forwarding time.
# Imports from third party packages


# Imports from project directory
from api.factories.forward_time import ForwardTimeFactory
from api.models.enums import TaxRecipient
from api.services.cities import CitiesService
from api.services.revenue import RevenueService
from api.services.taxes import TaxesService
from api.utils.config import Config


city_service = CitiesService()
config = Config()
factory = ForwardTimeFactory()
revenue_service = RevenueService()
tax_service = TaxesService()


class ForwardTimeService:
    def __init__(self):
        pass

    @staticmethod
    def forward_time(city_id: int, players: int):
        city_info = city_service.get_city_with_metadata(city_id)

        revenue = revenue_service.calculate_revenue(city_info.city.population,
                                                    config.rate_of_time_forward_by_players(players),
                                                    city_info.buildings)

        remaining_revenue = revenue
        tax_results = {}

        for recipient in tax_service.tax_priority_order():
            tax_revenue, remaining_revenue = tax_service.calculate_tax(remaining_revenue, recipient)
            tax_results[recipient] = tax_revenue

        king_tax_revenue = tax_results[TaxRecipient.KING]
        player_tax_revenue = tax_results[TaxRecipient.PLAYERS]

        return factory.create_forward_time_model(king_tax_revenue, player_tax_revenue, revenue, remaining_revenue)
