from statistics import mode
from .. import model, schema
from ..database import get_db
from typing import List
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import oauth2

router = APIRouter(
    prefix="/words",
    tags=["Words"]
)

@router.get("/", response_model=List[schema.WordResponse])
def get_words(request: str, db: Session = Depends(get_db)):

    words = db.query(model.Word).filter(model.Word.kazakh.like(request + "%")).all()
    words = words + db.query(model.Word).filter(model.Word.russian.like(request + "%")).all()
    words = list(dict.fromkeys(words))
    return words

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.WordResponse)
def add_word(word: schema.WordCreate, db: Session = Depends(get_db), current_user: model.User = Depends(oauth2.get_current_user)):
    new_word = model.Word(who_added=current_user.id, **word.dict())
    existing_word = db.query(model.Word).filter(
        model.Word.kazakh == new_word.kazakh and model.Word.russian == new_word.russian
        ).first()
    if existing_word:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Word already exists with id:{existing_word.id}"
            )

    db.add(new_word)
    db.commit()
    db.refresh(new_word)
    return new_word

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_word(id: int, db: Session = Depends(get_db), current_user: model.User = Depends(oauth2.get_current_user)):
    word = db.query(model.Word).filter(model.Word.id == id)
    if not word.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id: {id} was not found"
            )
    word.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schema.WordResponse)
def update_word(id: int, word: schema.WordCreate, db: Session = Depends(get_db), current_user: model.User = Depends(oauth2.get_current_user)):
    update_word_query = db.query(model.Word).filter(model.Word.id == id)
    if not update_word_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id: {id} was not found"
            )
    update_word_query.update(word.dict(), synchronize_session=False)
    db.commit()
    return update_word_query.first()