import os

PROJECT_NAME = "Fastapi template"
API_V1_STR = "/api/v1"
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:pass@localhost/test_db"

FIRST_SUPERUSER = "test@leaplending.co.uk"
FIRST_SUPERUSER_PASSWORD = "test"

SECRET_KEY = os.getenv("SECRET_KEY", "development")


ACCESS_TOKEN_EXPIRE_MINUTES = 30