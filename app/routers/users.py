from .. import model, schema, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.UserResponse)
def add_user(user: schema.UserCreate, db: Session = Depends(get_db), current_user: model.User = Depends(oauth2.get_current_user)):

    new_user = model.User(**user.dict())

    existing_user = db.query(model.User).filter(
        model.User.identification == new_user.identification
        ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User already exists with id:{existing_user.id}"
            )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user