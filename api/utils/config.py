# api/utils/config.py
# Description: This file contains the configurations for the application.
# Imports from third party packages
import json
import os


# Imports from project directory


class Config:
    def __init__(self):
        pass

    @staticmethod
    def city_base_revenue_rate():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, 'utils', 'config.json')
        with open(file_path, 'r') as file:
            revenue = json.load(file)["Revenue"]
        return revenue

    @staticmethod
    def king_tax_rate():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, 'utils', 'config.json')
        with open(file_path, 'r') as file:
            king_tax_rate = json.load(file)["Taxes"]["King"]
        return king_tax_rate

    @staticmethod
    def players_tax_rate():
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, 'utils', 'config.json')
        with open(file_path, 'r') as file:
            players_tax_rate = json.load(file)["Taxes"]["Players"]
        return players_tax_rate

    @staticmethod
    def rate_of_time_forward_by_players(players: int):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, 'utils', 'config.json')
        with open(file_path, 'r') as file:
            if players <= 0:
                rate_of_time_passed_data = json.load(file)["TimePassedRateByPlayer"]["1"]
            elif players >= 8:
                rate_of_time_passed_data = json.load(file)["TimePassedRateByPlayer"]["7"]
            else:
                rate_of_time_passed_data = json.load(file)["TimePassedRateByPlayer"][f"{players}"]
        return rate_of_time_passed_data
