# api/services/taxes.py
# Description: This file contains the service for Taxes
# Imports from third party packages


# Imports from project directory
from api.utils.config import Config
from api.models.enums import TaxRecipient


config = Config()


class TaxesService:
    def __init__(self):
        pass

    @staticmethod
    def calculate_tax(gross_income: float, tax_recipient: TaxRecipient) -> tuple:
        tax_rate = 0
        match tax_recipient:
            case TaxRecipient.KING:
                tax_rate = config.king_tax_rate()
            case TaxRecipient.PLAYERS:
                tax_rate = config.players_tax_rate()

        tax_revenue = gross_income * tax_rate
        net_income = gross_income - tax_revenue
        return tax_revenue, net_income

    @staticmethod
    def tax_priority_order() -> list:
        return [TaxRecipient.KING, TaxRecipient.PLAYERS]
