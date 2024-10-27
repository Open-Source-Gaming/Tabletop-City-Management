# db.migrations.py
# # This file is responsible for managing database migrations.
# # Imports from local packages


# Imports from third party packages
from sqlalchemy import Engine, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, DeclarativeBase, Mapped


class Base(DeclarativeBase):
    pass


class Migration:
    def __init__(self):
        pass

    @staticmethod
    def run(engine: Engine) -> None:
        Base.metadata.create_all(engine)

    def rollback(self):
        # Logic for rolling back migrations
        pass


# Table Models
class Buildings(Base):
    __tablename__ = 'buildings'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String())
    level: Mapped[int] = mapped_column(Integer)
    cost: Mapped[int] = mapped_column(Integer)

    city_buildings = relationship("CityBuildings", back_populates="building")

    def __repr__(self) -> str:
        return f"Building(name={self.name!r}, level={self.level!r}, cost={self.cost!r})"


class Cities(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String())
    type: Mapped[str] = mapped_column(String())
    population: Mapped[int] = mapped_column(Integer)
    tax_per_month: Mapped[int] = mapped_column(Integer)

    city_buildings = relationship("CityBuildings", back_populates="city")

    def __repr__(self) -> str:
        return (f"City(name={self.name!r}, type={self.type!r}, population={self.population!r},"
                f" tax_per_month={self.tax_per_month!r})")


class CityBuildings(Base):
    __tablename__ = 'city_buildings'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    building_id: Mapped[int] = mapped_column(ForeignKey('buildings.id'))

    city = relationship("Cities", back_populates="city_buildings")
    building = relationship("Buildings", back_populates="city_buildings")

    def __repr__(self) -> str:
        return f"CityBuilding(city_id={self.city_id!r}, building_id={self.building_id!r})"

