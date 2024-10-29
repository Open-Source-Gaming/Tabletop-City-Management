# api.models.enums.py
# This file contains the enumeration for Controllers types.
# Imports from local packages


# Imports from third party packages
from enum import Enum


class BuildingType(str, Enum):
    entertainment = "Entertainment"
    lumber_yard = "Lumber Yard"
    mine = "Mine"
    farm = "Farm"
    hunting = "Hunting"
    markets = "Markets"
    smithy = "Smithy"
    schools = "Schools"
    training_camps = "Training Camps"
    temples = "Temples"


class BuildingLevel(int, Enum):
    level_0 = 0
    level_1 = 1
    level_2 = 2
    level_3 = 3
    level_4 = 4
    level_5 = 5


class BuildingLevelFilter(str, Enum):
    less = "less"
    less_or_equal = "less_or_equal"
    exact = "exact"
    greater_or_equal = "greater_or_equal"
    greater = "greater"


class BuildingCostFilter(str, Enum):
    less = "less"
    less_or_equal = "less_or_equal"
    exact = "exact"
    greater_or_equal = "greater_or_equal"
    greater = "greater"


class ReportType(str, Enum):
    pdf = "pdf"
    html = "html"


class FilterType(str, Enum):
    less = "less"
    less_or_equal = "less_or_equal"
    exact = "exact"
    greater_or_equal = "greater_or_equal"
    greater = "greater"
