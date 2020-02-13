from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import pbkdf2_sha256

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    password = Column(String)

    def has_password(self, raw_password):
        return pbkdf2_sha256.hash(raw_password)

    def verify_password(self, input_password):
        return pbkdf2_sha256.verify(input_password, self.password)
