import sys
import os
from datetime import datetime, date
import enum
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_utils.function import database_exists
import sqlalchemy_utils
import os
from dotenv import load_dotenv
load_dotenv()


db_config = os.getenv('SQLALCHEMY_DB_CONFIG') 

#if 'sqlite' in db_config and 'check_same_thread=False' not in db_config:
#    db_config += '?check_same_thread=False'

ENGINE = create_engine(
    db_config,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()



class RoleEnum(enum.Enum):
    staff = "staff"
    admin = "admin"

class UserModel(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    last_name = Column('last_name', String(200), unique=True)
    first_name = Column('first_name', String(200), unique=True)
    phone = Column('phone', String(200))
    address = Column('address', String(400))
    email = Column('email', String(200), unique=True)
    couple = Column('couple', String(200))
    enfants = Column('enfants', String(200))
    allergies = Column('allergies', String(400))
    regime = Column('regime', String(400))
    commentaires = Column('commentaires', String(400))
    gphoto = Column('gphoto', String(400))
    created_at = Column('created_at', DATETIME, default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DATETIME, default=datetime.now, nullable=False)

    def __init__(self,  last_name: str, first_name: str, phone: str, address: str,email: str,couple: str,enfants: str,allergies: str,regime: str, commentaires: str, gphoto: str):
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.phone: str = phone
        self.address: str = address
        self.email: str = email
        self.couple: str = couple
        self.enfants: str = enfants
        self.allergies: str = allergies
        self.regime: str = regime
        self.commentaires: str = commentaires
        self.gphoto: str = gphoto


def auto_create_table():
    Base.metadata.create_all(bind=ENGINE)
