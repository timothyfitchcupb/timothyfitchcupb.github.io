from typing import Optional, List

from fastapi import FastAPI, Depends
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import init_db, get_db
from .models import Member

app = FastAPI(title="Healthcare Worker Advocacy CRM")  #API app


@app.on_event("startup")
def on_startup():
    init_db()  #create tables on startup


@app.get("/health")
def health():
    return {"status": "ok"}  #sanity check


#-------------------------
#Schemas
#-------------------------
class MemberCreate(BaseModel):
    name: str
    email: Optional[str] = None


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class MemberOut(BaseModel):
    id: int
    name: str
    email: Optional[str] = None

    class Config:
        from_attributes = True  #allow ORM -> schema


#-------------------------
#Member endpoints (starter)
#-------------------------
@app.post("/members", response_model=MemberOut)
def create_member(payload: MemberCreate, db: Session = Depends(get_db)):
    m = Member(name=payload.name, email=payload.email)  #new row
    db.add(m)  #stage insert
    db.commit()  #save
    db.refresh(m)  #load generated id
    return m


@app.get("/members", response_model=List[MemberOut])
def list_members(db: Session = Depends(get_db)):
    return db.query(Member).all()  #return all members


@app.get("/members/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        return {"error": "Member not found"}
    return member    


@app.patch("/members/{member_id}", response_model=MemberOut)
def update_member(member_id: int, payload: MemberUpdate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        return {"error": "Member not found"}
    if payload.name is not None:
        member.name = payload.name
    if payload.email is not None:
        member.email = payload.email
    db.commit()
    db.refresh(member)
    return member

@app.delete("/members/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    db.delete(member)
    db.commit()
    return {"deleted": True, "member_id": member_id}