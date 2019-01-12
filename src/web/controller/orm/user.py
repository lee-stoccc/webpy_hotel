# coding=utf-8
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()
BaseModel = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:911789@localhost:3306/webpy', echo=True)


class User(Base):
    __tablename__ = 'u_user'
    UserID = Column(Integer, primary_key=True, autoincrement=True, doc='用户ID')
    UserCode = Column(String(100), nullable=True, doc='用户名')
    Password = Column(String(100), nullable=True, doc='密码')
    Tel = Column(Integer, nullable=True, doc='联系方式')
    State = Column(Integer, nullable=True, doc='状态')
    WorkCode = Column(String(100), nullable=True, doc='人员编号')
    UserName = Column(String(100), nullable=True, doc='人员姓名')
    Post = Column(String(100), nullable=True, doc='岗位')
    UserDataRoleList = Column(String(100), nullable=True, doc='数据权限列表')
    RoleList = Column(String(100), nullable=True)
    Remark = Column(String(100), nullable=True)
    CreateTime = Column(DateTime, nullable=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    def user_to_json(self):
        self.jsonUser = {}
        self.jsonUser["UserID"] =self.UserID
        self.jsonUser["UserName"] = self.UserName
        self.jsonUser["UserCode"] =self.UserName
        # jsonUser = json.dumps(self.jsonUser)
        # print jsonUser
        return self.jsonUser


def init_db():
    BaseModel.metadata.create_all(engine)


init_db()
