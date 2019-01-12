# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class GuestDoc(Base):
    __tablename__ = 'g_guest_doc'
    GuestDocID = Column(Integer, primary_key=True, autoincrement=True)
    GuestType = Column(Integer, nullable=True)
    DocType = Column(String(100), nullable=True)
    DocNo = Column(String(100), nullable=True)
    DocName = Column(String(100), nullable=True)
    GuestName = Column(String(100), nullable=True)
    BornDate = Column(String(100), nullable=True)
    Sex = Column(String(100), nullable=True)
    NativePlace = Column(String(100), nullable=True)
    Nation = Column(String(100), nullable=True)
    AuthStatus = Column(String(100), nullable=True)
    ResAddress = Column(String(100), nullable=True)
    State = Column(Integer, nullable=True)
    CertiOffice = Column(String(100), nullable=True)
    CertiEffStartTime = Column(DateTime, nullable=True)
    CertiEffEndTime = Column(DateTime, nullable=True)
    DocPhotoURL = Column(String(100), nullable=True)
    Remark = Column(String(100), nullable=True)
    CreateTime = Column(DateTime, nullable=True)
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
