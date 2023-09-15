import sqlalchemy
from sqlalchemy.orm import relationship

from data.db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'order'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id'))
    sub_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('subscription.id'))

    user = relationship('User')
    subscription = relationship('Subscription')

    def __repr__(self):
        return f'{self.id!r}'
