import crud
from core import config
from schema.users import UserInCreate
from db.base_class import Base
from db.session import engine

def init_db(db_session):
    Base.metadata.create_all(bind=engine)
    user = crud.user.get_by_email(db_session, email=config.FIRST_SUPERUSER)
    if not user:
        user_in = UserInCreate(
            email=config.FIRST_SUPERUSER,
            password=config.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db_session, user_in=user_in)
