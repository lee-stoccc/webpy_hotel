# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class OperatingLog(Base):
    __tablename__ = 'l_operating_log'
    OperaLogID = Column(Integer, primary_key=True, autoincrement=True)
    LoginTime = Column(DateTime, nullable=True)
    WorkCode = Column(String(100), nullable=True)
    UserName = Column(String(100), nullable=True)
    OperaType = Column(String(20), nullable=True)
    KeyWord = Column(String(1024), nullable=True)
    IP = Column(String(100), nullable=True)
    CreateTime = Column(DateTime, nullable=True)
    Remark = Column(String(256), nullable=True)
    DeviceCode = Column(String(100), nullable=True)
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
