from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
Base=declarative_base()
DB_URI = 'postgresql+psycopg2://postgres:steriowolf@localhost/moonproduct'
class moonproduct(Base):
 __tablename__='retailer'
 id = Column(Integer,primary_key=True)
 name = Column(String(100))
 Contact_number = Column(Integer)
 Contact_emailId = Column(String(50))
if __name__=="__main__":
 from sqlalchemy import create_engine
 engine = create_engine(DB_URI)
 Base.metadata.drop_all(engine)
 Base.metadata.create_all(engine)
