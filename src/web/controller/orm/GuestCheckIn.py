# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class GuestCheckIn(Base):
    __tablename__ = 'g_guest_checkin'
    HotelGuestID = Column(Integer, primary_key=True, autoincrement=True)
    HotelDocType = Column(Integer, nullable=True)
    HotelDocNo = Column(String(100), nullable=True)
    HotelDocName = Column(String(100), nullable=True)
    HotelGuestName = Column(String(100), nullable=True)
    HotelBornDate = Column(String(100), nullable=True)
    HotelSex = Column(String(100), nullable=True)
    HotelNation = Column(String(100), nullable=True)
    HotelAddress = Column(String(100), nullable=True)
    HotelRemark = Column(String(100), nullable=True)
    LastModifyTime = Column(DateTime, nullable=True)
    HotelLastModifyTime = Column(DateTime, nullable=True)
    HotelTel = Column(String(100), nullable=True)
    MatchResult = Column(Integer, nullable=True)
    MatchResultPercent = Column(Float, nullable=True)
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
