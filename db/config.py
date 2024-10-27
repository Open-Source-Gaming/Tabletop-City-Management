# db/config.py
# This file contains the configuration for the database.
# Imports from local packages
from db.migrations import Migration
from db.seed.buildings import Buildings as BuildingsSeeder


# Imports from third party packages
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session


building_seeder = BuildingsSeeder()
migration = Migration()


class DatabaseConfig:
    def __init__(self):
        pass

    @staticmethod
    def create_engine() -> Engine:
        return create_engine("sqlite:///town-city-management.db", echo=True)

    @staticmethod
    def create_base_metadata(engine) -> None:
        migration.run(engine)

    @staticmethod
    def create_seed_data(session: Session) -> None:
        building_seeder.seed_data(session)

    def create_session(self) -> Session:
        engine = self.create_engine()
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return session_local()

    def initialize_sql_migration(self) -> None:
        engine = self.create_engine()

        self.create_base_metadata(engine)
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = session_local()

        self.create_seed_data(session)
        session.commit()
