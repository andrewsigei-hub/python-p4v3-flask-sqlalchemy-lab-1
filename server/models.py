from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Earthquake(db.Model, SerializerMixin):
    """
    Model representing an earthquake event in the database.
    """

    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)  # ✅ Capital I
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)  # ✅ Capital I - not db.int

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
