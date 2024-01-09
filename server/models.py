from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    
    # Establish relationship with the Animal model
    animals = db.relationship('Animal', back_populates='zookeeper')

    def __repr__(self):
        return f"Zookeeper(id={self.id}, name={self.name}, birthday={self.birthday})"


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)

    environment = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=True)
    
    # Establish relationship with the Animal model
    animals = db.relationship('Animal', back_populates='enclosure')

    def __repr__(self):
        return f"Enclosure(id={self.id}, environment={self.environment}, open_to_visitors={self.open_to_visitors})"


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'), nullable=False)

    # Establish relationships with Zookeeper and Enclosure models
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')

    def __repr__(self):
        return f"Animal(id={self.id}, name={self.name}, species={self.species})"