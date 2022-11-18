from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#DATABASE_URL = "postgresql://postgresql:postgres@localhost:5432/python_db"
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/test"
#DATABASE_URL = "sqlite:///data.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()