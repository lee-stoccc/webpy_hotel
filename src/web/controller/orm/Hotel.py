# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class Hotel(Base):
    __tablename__ = 'h_hotel'
    HotelID = Column(Integer, primary_key=True, autoincrement=True)
    HotelCode = Column(String(111), nullable=True)
    HotelName = Column(String(111), nullable=True)
    HotelAddr = Column(String(111), nullable=True)
    HotelTel = Column(String(111), nullable=True)
    LegalTel = Column(String(100), nullable=True)
    LegalPerson = Column(String(100), nullable=True)
    LegalDocNo = Column(String(100), nullable=True)
    Coordinate = Column(String(100), nullable=True)
    ProvinceID = Column(Integer, nullable=True)
    Province = Column(String(100), nullable=True)
    CityID = Column(Integer, nullable=True)
    CityName = Column(String(100), nullable=True)
    DistrictID = Column(Integer, nullable=True)
    District = Column(String(100), nullable=True)
    State = Column(Integer, nullable=True)
    HotelType = Column(Integer, nullable=True)
    CreateUserID = Column(Integer, nullable=True)
    CreateUserName = Column(String(100), nullable=True)
    ResponPersonTel = Column(String(111), nullable=True)
    ResponPerson = Column(String(100), nullable=True)
    ApplyTime = Column(DateTime(100), nullable=True)
    AuditTime = Column(DateTime(100), nullable=True)
    AuditUserID = Column(String(100), nullable=True)
    AuditUserCode = Column(String(100), nullable=True)
    RoomCount = Column(Integer, nullable=True)
    BedCount = Column(Integer, nullable=True)
    AuditState = Column(Integer, nullable=True)
    AuditStateName = Column(String(100), nullable=True)
    BusLicenseCode = Column(String(100), nullable=True)
    BusLicenseName = Column(String(100), nullable=True)
    RegStartTime = Column(DateTime, nullable=True)
    Remark = Column(String(1000), nullable=True)
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
