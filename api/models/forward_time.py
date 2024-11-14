# api/models/forward_time.py
# This file contains the Pydantic models for the cities.
# Imports from local packages


# Imports from third party packages
from pydantic import BaseModel


class ForwardTime(BaseModel):
    king_tax_revenue: int
    players_tax_revenue: int
    village_gross_income: int
    village_net_income: int
