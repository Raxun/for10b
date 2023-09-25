import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    Day = sqlalchemy.Column(sqlalchemy.String)
    Fir = sqlalchemy.Column(sqlalchemy.String)
    Sec = sqlalchemy.Column(sqlalchemy.String)
    Thi = sqlalchemy.Column(sqlalchemy.String)
    For = sqlalchemy.Column(sqlalchemy.String)
    Fiv = sqlalchemy.Column(sqlalchemy.String)
    Six = sqlalchemy.Column(sqlalchemy.String)
    Sev = sqlalchemy.Column(sqlalchemy.String)
    Eig = sqlalchemy.Column(sqlalchemy.String)
    Nin = sqlalchemy.Column(sqlalchemy.String)
    Ten = sqlalchemy.Column(sqlalchemy.String)


class Сountries(SqlAlchemyBase):
    __tablename__ = 'countries'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    Day = sqlalchemy.Column(sqlalchemy.String)
    Fir = sqlalchemy.Column(sqlalchemy.String)
    Sec = sqlalchemy.Column(sqlalchemy.String)
    Thi = sqlalchemy.Column(sqlalchemy.String)
    For = sqlalchemy.Column(sqlalchemy.String)
    Fiv = sqlalchemy.Column(sqlalchemy.String)
    Six = sqlalchemy.Column(sqlalchemy.String)
    Sev = sqlalchemy.Column(sqlalchemy.String)
    Eig = sqlalchemy.Column(sqlalchemy.String)
    Nin = sqlalchemy.Column(sqlalchemy.String)
    Ten = sqlalchemy.Column(sqlalchemy.String)


class Niggers(SqlAlchemyBase):
    __tablename__ = 'niggers'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    tag = sqlalchemy.Column(sqlalchemy.String)
    text = sqlalchemy.Column(sqlalchemy.String)
