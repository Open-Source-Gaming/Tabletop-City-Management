# db/seed/buildings.py
# This file is responsible for seeding the buildings data into the database.
# Imports from local packages
from db.migrations import Buildings as BuildingsModel


# Imports from third party packages
from sqlalchemy.orm import Session


class Buildings:
    def __init__(self):
        pass

    @staticmethod
    def seed_data(session: Session) -> None:
        if not session.query(BuildingsModel).count():
            # Add static reference data
            buildings = [
                # Entertainment
                BuildingsModel(name="Entertainment", level=0, cost=0),
                BuildingsModel(name="Entertainment", level=1, cost=250),
                BuildingsModel(name="Entertainment", level=2, cost=750),
                BuildingsModel(name="Entertainment", level=3, cost=1000),
                BuildingsModel(name="Entertainment", level=4, cost=2500),
                BuildingsModel(name="Entertainment", level=5, cost=3000),

                # Lumber Yard
                BuildingsModel(name="Lumber Yard", level=0, cost=0),
                BuildingsModel(name="Lumber Yard", level=1, cost=500),
                BuildingsModel(name="Lumber Yard", level=2, cost=1000),
                BuildingsModel(name="Lumber Yard", level=3, cost=2000),
                BuildingsModel(name="Lumber Yard", level=4, cost=3000),
                BuildingsModel(name="Lumber Yard", level=5, cost=4500),

                # Mine
                BuildingsModel(name="Mine", level=0, cost=0),
                BuildingsModel(name="Mine", level=1, cost=500),
                BuildingsModel(name="Mine", level=2, cost=1000),
                BuildingsModel(name="Mine", level=3, cost=2000),
                BuildingsModel(name="Mine", level=4, cost=3000),
                BuildingsModel(name="Mine", level=5, cost=4500),

                # Farm
                BuildingsModel(name="Farm", level=0, cost=0),
                BuildingsModel(name="Farm", level=1, cost=3500),
                BuildingsModel(name="Farm", level=2, cost=7500),
                BuildingsModel(name="Farm", level=3, cost=12500),
                BuildingsModel(name="Farm", level=4, cost=20000),
                BuildingsModel(name="Farm", level=5, cost=25000),

                # Hunting
                BuildingsModel(name="Hunting", level=0, cost=0),
                BuildingsModel(name="Hunting", level=1, cost=500),
                BuildingsModel(name="Hunting", level=2, cost=750),
                BuildingsModel(name="Hunting", level=3, cost=1000),
                BuildingsModel(name="Hunting", level=4, cost=2500),
                BuildingsModel(name="Hunting", level=5, cost=3000),

                # Markets
                BuildingsModel(name="Markets", level=0, cost=0),
                BuildingsModel(name="Markets", level=1, cost=500),
                BuildingsModel(name="Markets", level=2, cost=750),
                BuildingsModel(name="Markets", level=3, cost=1000),
                BuildingsModel(name="Markets", level=4, cost=2500),
                BuildingsModel(name="Markets", level=5, cost=3000),

                # Smiting
                BuildingsModel(name="Smithy", level=0, cost=0),
                BuildingsModel(name="Smithy", level=1, cost=1500),
                BuildingsModel(name="Smithy", level=2, cost=3000),
                BuildingsModel(name="Smithy", level=3, cost=5000),
                BuildingsModel(name="Smithy", level=4, cost=9000),
                BuildingsModel(name="Smithy", level=5, cost=10000),

                # Schools
                BuildingsModel(name="Schools", level=0, cost=0),
                BuildingsModel(name="Schools", level=1, cost=1500),
                BuildingsModel(name="Schools", level=2, cost=3000),
                BuildingsModel(name="Schools", level=3, cost=5000),
                BuildingsModel(name="Schools", level=4, cost=10000),
                BuildingsModel(name="Schools", level=5, cost=25000),

                # Training Camps
                BuildingsModel(name="Training Camps", level=0, cost=0),
                BuildingsModel(name="Training Camps", level=1, cost=750),
                BuildingsModel(name="Training Camps", level=2, cost=1500),
                BuildingsModel(name="Training Camps", level=3, cost=5000),
                BuildingsModel(name="Training Camps", level=4, cost=7500),
                BuildingsModel(name="Training Camps", level=5, cost=20000),

                # Temples
                BuildingsModel(name="Temples", level=0, cost=0),
                BuildingsModel(name="Temples", level=1, cost=3000),
                BuildingsModel(name="Temples", level=2, cost=10000),
                BuildingsModel(name="Temples", level=3, cost=25000),
                BuildingsModel(name="Temples", level=4, cost=40000),
                BuildingsModel(name="Temples", level=5, cost=75000)
            ]
            session.add_all(buildings)
