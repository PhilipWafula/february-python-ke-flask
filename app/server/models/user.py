from app import add_parent_directory_to_system_path
from app.server import db
from app.server.models.utilities.base_model import BaseModel


class User(BaseModel):
    """
    Creates a user object and defines other user specific operations.
    """
    __tablename__ = 'users'

    # user information
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String, index=True, unique=True)
    date_of_birth = db.Column(db.Date)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.user
