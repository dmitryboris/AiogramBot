import sqlalchemy
from sqlalchemy.orm import relationship

from data.db_session import SqlAlchemyBase


class Subscription(SqlAlchemyBase):
    __tablename__ = 'subscription'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    order = relationship('Order', back_populates='subscription')

    def __repr__(self):
        return f'{self.name}'
