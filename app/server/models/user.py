from server import db
from server.models.utilities.base_model import BaseModel


class User(BaseModel):
    """

    """
    __tablename__ = 'users'

    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.user
