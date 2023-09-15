import sqlalchemy
from sqlalchemy.orm import relationship

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, unique=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    order = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'{self.name}'
