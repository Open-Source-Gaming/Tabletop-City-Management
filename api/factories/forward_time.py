# api/factories/forward_time.py
# Description: This file contains the factory for forwarding time.
# Imports from project directory
from api.models.forward_time import ForwardTime


# Imports from third party packages


class ForwardTimeFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_forward_time_model(king_tax_revenue: int, players_tax_revenue: int,
                                  village_gross_income: int, village_net_income: int):
        return ForwardTime(
            king_tax_revenue=king_tax_revenue,
            players_tax_revenue=players_tax_revenue,
            village_gross_income=village_gross_income,
            village_net_income=village_net_income
        )
