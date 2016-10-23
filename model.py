from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


######################

# assocation_table = db.Table('association', db.metadata, 
#             db.Column('testimonial_id', db.Integer, db.ForeignKey('testimonials.id')),
#             db.Column('instructor_id', db.Integer, db.ForeignKey('instructors.id')))

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
    subjects = db.relationship('Instructor', secondary=assocation_table)

    def __repr__(self):
        """Produce helpful representation of object"""

        return '<Testimonial {}>'.format(self.id)

class Course(db.Model):
    pass

class CourseCategory(db.Model):
    pass

class InstructorCourse(db.Model):
    pass

class Staff(db.Model):
    pass

class Activity(db.Model):
    pass

class General(db.Model):
    pass

class TestimonialSubject(db.Model):
    pass

    __tablename__ = 'test_subjs'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey)
    subj_id = db.Column(db.Integer)


class Source(db.Model):
    pass



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
    db.create_all()
    print "Connected to DB."