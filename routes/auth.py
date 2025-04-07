from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserOut
from utils.security import hash_password, verify_password, create_access_token
from database import get_db

router = APIRouter()

@router.post("/login", response_model=UserOut)
async def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create JWT Token
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
