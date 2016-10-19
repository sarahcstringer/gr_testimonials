from flask_sqlalchemy import SQLAlchemy
# from server import app



db = SQLAlchemy()


######################

assocation_table = Table('association', Base.metadata, 
            Column('testimonial_id', Integer, ForeignKey('testimonials.id')),
            Column('instructor_id', Integer, ForeignKey('instructors.id')))

class Instructor(db.Model):
    """Instructor table model"""

    __tablename__ = 'instructors'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(40), nullable=False)
    lname = db.Column(db.String(40), nullable=False)


    def __repr__(self):
        """Produce helpful representation of object"""

        return '<Instructor {} {}>'.format(self.fname, self.lname)

class Testimonial(db.Model):
    """Testimonial table model"""

    __tablename__ = 'testimonials'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    testimonial_text = db.Column(db.Text, nullable=False)
    subjects = relationship('Instructor', secondary=assocation_table)

    def __repr__(self):
        """Produce helpful representation of object"""

        return '<Testimonial {}>'.format(self.id)



######################
def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///testimonials'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."