# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class RelationCheckIn(Base):
    __tablename__ = 'h_relation_checkin'
    RelationCheckInID = Column(Integer, primary_key=True, autoincrement=True)
    CheckInID = Column(Integer, nullable=True)
    HotelGuestID = Column(Integer, nullable=True)
    GuestDocID = Column(Integer, nullable=True)
    CheckInType = Column(Integer, nullable=True)
    CheckInTime = Column(DateTime, nullable=True)
    CheckOutTime = Column(DateTime, nullable=True)
    GuestState = Column(Integer, nullable=True)
    LastModifyTime = Column(DateTime, nullable=True)
    HotelLastModifyTime = Column(DateTime, nullable=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # def user_to_json(self):
    #     self.jsonDataRole = {}
    #     self.jsonDataRole["UserID"] =self.UserID
    #     self.jsonDataRole["UserDataRoleID"] = self.UserDataRoleID
    #     self.jsonDataRole["Remark"] = self.Remark
    #     # self.jsonUser["UserCode"] =self.UserName
    #     return self.jsonDataRole


def init_db():
    BaseModel.metadata.create_all(engine)


init_db()
