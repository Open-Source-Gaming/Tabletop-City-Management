# api/factories/forward_time.py
# Description: This file contains the factory for forwarding time.
# Imports from project directory
from api.models.forward_time import ForwardTime


# Imports from third party packages


class ForwardTimeFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_forward_time_model(king_tax_revenue: float, players_tax_revenue: float,
                                  village_gross_income: float, village_net_income: float):
        return ForwardTime(
            king_tax_revenue=king_tax_revenue,
            players_tax_revenue=players_tax_revenue,
            village_gross_income=village_gross_income,
            village_net_income=village_net_income
        )
