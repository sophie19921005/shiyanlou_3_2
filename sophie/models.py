from sqlalchemy import String,Integer,Column,create_engine,DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')
Base = declarative_base()
class Repositories(Base):
    __tablename__='repositories'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)

if __name__=="__main__":
    Base.metadata.create_all(engine)


