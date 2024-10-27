# api.services.__init__.py
# # This file is responsible for initializing the repositories package.
# Imports from local packages
from api.models.enums import FilterType
from db.config import DatabaseConfig


# Imports from third party packages
from typing import Any
from sqlalchemy import Column
from sqlalchemy.orm import Query, Session


db = DatabaseConfig()


def apply_filter(query: Query, column: Column, value: Any, filter_type: str) -> Query:
    if filter_type == FilterType.greater:
        return query.filter(column > value)
    elif filter_type == FilterType.greater_or_equal:
        return query.filter(column >= value)
    elif filter_type == FilterType.less_or_equal:
        return query.filter(column <= value)
    elif filter_type == FilterType.less:
        return query.filter(column < value)
    else:
        return query.filter(column == value)


def verify_session(session: Session | None = None) -> Session:
    if session is None:
        session = db.create_session()
    return session
