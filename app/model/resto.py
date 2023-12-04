
from app import db

class Resto(db.Model):
    __tablename__ = 'resto'
    Place_Id = db.Column(db.String(255), primary_key=True)
    Place_Name = db.Column(db.String(50), nullable=False)
    Culinary_Ratings = db.Column(db.String(5), nullable=False)
    Category = db.Column(db.String(30), nullable=False)
    Address = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.String(500), nullable=False)
    Coordinate = db.Column(db.String(50), nullable=False)
    Lat = db.Column(db.String(50), nullable=False)
    Long = db.Column(db.String(50), nullable=False)
 

    def __repr__(self):
        return '<Resto {}>'.format(self.Place_Name)
    
    
