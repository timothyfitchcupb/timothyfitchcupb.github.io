from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()  #base class for ORM models


class Member(Base):
    __tablename__ = "members"  #table name

    id = Column(Integer, primary_key=True)  #PK
    name = Column(String(100), nullable=False)  #required
    email = Column(String(120))  

    interactions = relationship("Interaction", back_populates="member")  # 1tomany


class Campaign(Base):
    __tablename__ = "campaigns"  

    id = Column(Integer, primary_key=True)  # PK
    title = Column(String(150), nullable=False)  # required
    description = Column(Text)  # optional long text

    interactions = relationship("Interaction", back_populates="campaign")  # 1tomany


class Interaction(Base):
    __tablename__ = "interactions"  
    
    id = Column(Integer, primary_key=True)  # PK
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)  # FK
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)  # FK

    date = Column(Date)  
    type = Column(String(50))  # call/email/event
    notes = Column(Text)  

    member = relationship("Member", back_populates="interactions")  # manyto1
    campaign = relationship("Campaign", back_populates="interactions")  # manyto1
