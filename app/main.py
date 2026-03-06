from typing import Optional, List
from datetime import date
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import init_db, get_db
from .models import Member, Campaign, Interaction

app = FastAPI(title="Healthcare Worker Advocacy CRM")  # API app


@app.on_event("startup")
def on_startup():
    init_db()  #create tables on startup


@app.get("/health")
def health():
    return {"status": "ok"}  #sanity check


# -------------------------
# Schemas
# -------------------------
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


class CampaignCreate(BaseModel):
    title: str
    description: Optional[str] = None


class CampaignUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class CampaignOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class InteractionCreate(BaseModel):
    member_id: int
    campaign_id: int
    date: Optional[date] = None
    type: Optional[str] = None
    notes: Optional[str] = None


class InteractionUpdate(BaseModel):
    member_id: Optional[int] = None
    campaign_id: Optional[int] = None
    date: Optional[date] = None
    type: Optional[str] = None
    notes: Optional[str] = None


class InteractionOut(BaseModel):
    id: int
    member_id: int
    campaign_id: int
    date: Optional[date] = None
    type: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


# -------------------------
# Member endpoints
# -------------------------
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
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@app.patch("/members/{member_id}", response_model=MemberOut)
def update_member(member_id: int, payload: MemberUpdate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

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


# -------------------------
# Campaign endpoints
# -------------------------
@app.post("/campaigns", response_model=CampaignOut)
def create_campaign(payload: CampaignCreate, db: Session = Depends(get_db)):
    c = Campaign(title=payload.title, description=payload.description)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c


@app.get("/campaigns", response_model=List[CampaignOut])
def list_campaigns(db: Session = Depends(get_db)):
    return db.query(Campaign).all()


@app.get("/campaigns/{campaign_id}", response_model=CampaignOut)
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign


@app.patch("/campaigns/{campaign_id}", response_model=CampaignOut)
def update_campaign(campaign_id: int, payload: CampaignUpdate, db: Session = Depends(get_db)):
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    if payload.title is not None:
        campaign.title = payload.title
    if payload.description is not None:
        campaign.description = payload.description

    db.commit()
    db.refresh(campaign)
    return campaign


@app.delete("/campaigns/{campaign_id}")
def delete_campaign(campaign_id: int, db: Session = Depends(get_db)):
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    db.delete(campaign)
    db.commit()
    return {"deleted": True, "campaign_id": campaign_id}


# -------------------------
# Interaction endpoints
# -------------------------
@app.post("/interactions", response_model=InteractionOut)
def create_interaction(payload: InteractionCreate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == payload.member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    campaign = db.query(Campaign).filter(Campaign.id == payload.campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    i = Interaction(
        member_id=payload.member_id,
        campaign_id=payload.campaign_id,
        date=payload.date,
        type=payload.type,
        notes=payload.notes,
    )

    db.add(i)
    db.commit()
    db.refresh(i)
    return i


@app.get("/interactions", response_model=List[InteractionOut])
def list_interactions(
    member_id: Optional[int] = None,
    campaign_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Interaction)

    if member_id is not None:
        query = query.filter(Interaction.member_id == member_id)

    if campaign_id is not None:
        query = query.filter(Interaction.campaign_id == campaign_id)

    return query.all()


@app.get("/interactions/{interaction_id}", response_model=InteractionOut)
def get_interaction(interaction_id: int, db: Session = Depends(get_db)):
    interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return interaction


@app.patch("/interactions/{interaction_id}", response_model=InteractionOut)
def update_interaction(
    interaction_id: int, payload: InteractionUpdate, db: Session = Depends(get_db)
):
    interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    if payload.member_id is not None:
        member = db.query(Member).filter(Member.id == payload.member_id).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        interaction.member_id = payload.member_id

    if payload.campaign_id is not None:
        campaign = db.query(Campaign).filter(Campaign.id == payload.campaign_id).first()
        if not campaign:
            raise HTTPException(status_code=404, detail="Campaign not found")
        interaction.campaign_id = payload.campaign_id

    if payload.date is not None:
        interaction.date = payload.date
    if payload.type is not None:
        interaction.type = payload.type
    if payload.notes is not None:
        interaction.notes = payload.notes

    db.commit()
    db.refresh(interaction)
    return interaction


@app.delete("/interactions/{interaction_id}")
def delete_interaction(interaction_id: int, db: Session = Depends(get_db)):
    interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    db.delete(interaction)
    db.commit()
    return {"deleted": True, "interaction_id": interaction_id}