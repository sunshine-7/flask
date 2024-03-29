# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
# from app import db

# Define a base model for other database tables to inherit
class Base(object):

    __abstract__  = True

    id            = "" #db.Column(db.Integer, primary_key=True)
    date_created  = "" #db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = "" #db.Column(db.DateTime,  default=db.func.current_timestamp(),
                        #                   onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name    = "ww"   #db.Column(db.String(128),  nullable=False)

    # Identification Data: email & password
    email    = "dyh@sina.com"  #db.Column(db.String(128),  nullable=False,
                 #                           unique=True)
    password = "12345" #db.Column(db.String(192),  nullable=False)

    # Authorisation Data: role & status
    role     = "ceo" #db.Column(db.SmallInteger, nullable=False)
    status   =  "on" #db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)