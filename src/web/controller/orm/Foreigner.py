# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class Foreigner(Base):
    __tablename__ = 'g_foreigner'
    ForeignerID = Column(Integer, primary_key=True, autoincrement=True)
    GuestDocID = Column(Integer, nullable=True)
    PassNo = Column(String(111), nullable=True)
    VisaDeadline = Column(DateTime, nullable=True)
    DepartureTime = Column(DateTime, nullable=True)
    EntryTime = Column(DateTime, nullable=True)
    EntryPlace = Column(String(100), nullable=True)
    DeparturePlace = Column(String(100), nullable=True)
    VisaType = Column(String(11), nullable=True)
    Nationality = Column(String(11), nullable=True)
    CreateTime = Column(Integer, nullable=True)
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
