# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class UserDataRole(Base):
    __tablename__ = 'u_user_data_role'
    UserDataRoleID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(String(100), nullable=True)
    DataRoleID = Column(Integer, nullable=True)
    BeginValue = Column(String(100), nullable=True)
    EndValue = Column(String(100), nullable=True)
    ValueSet = Column(String(100), nullable=True)
    Flag = Column(Integer, nullable=True)
    Remark = Column(String(100), nullable=True)
    CreateTime = Column(DateTime, nullable=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    def user_to_json(self):
        self.jsonDataRole = {}
        self.jsonDataRole["UserID"] =self.UserID
        self.jsonDataRole["UserDataRoleID"] = self.UserDataRoleID
        self.jsonDataRole["Remark"] = self.Remark
        # self.jsonUser["UserCode"] =self.UserName
        return self.jsonDataRole


def init_db():
    BaseModel.metadata.create_all(engine)


init_db()
