from os import access
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from app.schema import UserLogin

from .. import database, schema, model, oauth2

router = APIRouter(tags=['Authentication'])

@router.post("/login", status_code=status.HTTP_200_OK, response_model=schema.Token)
def login(user_credentials: schema.UserLogin, db: Session = Depends(database.get_db)):

    user = db.query(model.User).filter(
        model.User.identification == user_credentials.identification
        ).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}