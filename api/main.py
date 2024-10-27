# api/main.py
# This is the main file for the FastAPI application. It contains the main logic for the application.
# Imports from local packages
from db.config import DatabaseConfig
from api.controllers import buildings
from api.controllers import cities


# Imports from third party packages
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


app = FastAPI()
db = DatabaseConfig()


app.include_router(buildings.router)
app.include_router(cities.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Tabletop City Management API",
        description="This is a city builder manager for tabletop players.",
        routes=app.routes,
        version="0.1.0",
        openapi_version="3.0.2",
        servers=[{"url": "http://127.0.0.1:8000"}, {"url": "http://0.0.0.0:8080"}],
    )
    app.openapi_schema = openapi_schema
    for _, method_item in app.openapi_schema.get("paths").items():
        for _, param in method_item.items():
            responses = param.get("responses")
            if "422" in responses:
                del responses["422"]
    for _, schema in app.openapi_schema.get("components").items():
        if "ValidationError" in schema:
            del schema["ValidationError"]
        if "HTTPValidationError" in schema:
            del schema["HTTPValidationError"]
    return openapi_schema


app.openapi = custom_openapi
db.initialize_sql_migration()

