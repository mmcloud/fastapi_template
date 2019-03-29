from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api.utils.db import get_db
from api.utils.security import get_current_active_superuser, get_current_active_user
from models.user import User as DBUser
from schema import User, UserInCreate, UserInDB, UserInUpdate

router = APIRouter()


# CRUD /users/
@router.get("/users/", tags=["users"], response_model=List[User])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: DBUser = Depends(get_current_active_superuser)):  # TODO depend on superuser
    """
    List all current users
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/users/", tags=['users'], response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserInCreate,
    current_user: DBUser = Depends(get_current_active_superuser)): # TODO depend on superuser
    """
    Create a new user
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, user_in=user_in)
    # TODO celery service for emails
    return user


@router.get("/users/{user_id}", tags=["users"], response_model=User)
def read_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_active_superuser)):
    """
    Get a specific user by ID
    """
    user = crud.user.get(db, user_id=user_id)
    return user

@router.put("/users/{user_id}", tags=['users'], response_model=User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: UserInUpdate,
    current_user: DBUser = Depends(get_current_active_superuser)
):
    """
    Update a user
    """
    user = crud.user.get(db, user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Invalid User ID"
        )
    user = crud.user.update(db, user=user, user_in=user_in)
    return user