import os

PROJECT_NAME = "My fastapi template"
API_V1_STR = "/api/v1"
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:pass@localhost/quotation"

FIRST_SUPERUSER = "matthew@leaplending.co.uk"
FIRST_SUPERUSER_PASSWORD = "myroot"

SECRET_KEY = os.getenv("SECRET_KEY", "development")


ACCESS_TOKEN_EXPIRE_MINUTES = 30