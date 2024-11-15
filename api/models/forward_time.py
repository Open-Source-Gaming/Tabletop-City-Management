# api/models/forward_time.py
# This file contains the Pydantic models for the cities.
# Imports from local packages


# Imports from third party packages
from pydantic import BaseModel


class ForwardTime(BaseModel):
    king_tax_revenue: float
    players_tax_revenue: float
    village_gross_income: float
    village_net_income: float
