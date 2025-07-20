from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship('Brand', backref=db.backref('series', lazy=True))


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    multiplier = db.Column(db.Float, default=1.0)


series_profiles = db.Table(
    'series_profiles',
    db.Column('series_id', db.Integer, db.ForeignKey('series.id')),
    db.Column('profile_id', db.Integer, db.ForeignKey('profile.id')),
)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))
    unit_price = db.Column(db.Float, nullable=False)
    default_color_id = db.Column(db.Integer, db.ForeignKey('color.id'))
    default_color = db.relationship('Color')
    series = db.relationship(
        'Series', secondary=series_profiles, backref=db.backref('profiles', lazy='dynamic')
    )

