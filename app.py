from flask import Flask, render_template, request, redirect, url_for
from models import db, Brand, Series, Profile, Color
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    brands = Brand.query.all()
    return render_template('index.html', brands=brands)


@app.route('/import', methods=['POST'])
def import_prices():
    file = request.files['file']
    df = pd.read_excel(file)
    for _, row in df.iterrows():
        color = Color.query.filter_by(name=row['color']).first()
        if not color:
            color = Color(name=row['color'], multiplier=row.get('multiplier', 1.0))
            db.session.add(color)
        profile = Profile.query.filter_by(stock_code=row['stock_code']).first()
        if not profile:
            profile = Profile(
                stock_code=row['stock_code'],
                description=row['description'],
                unit_price=row['unit_price'],
                default_color=color,
            )
            db.session.add(profile)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/order', methods=['GET', 'POST'])
def order():
    profiles = Profile.query.all()
    colors = Color.query.all()
    if request.method == 'POST':
        profile_id = int(request.form['profile'])
        color_id = int(request.form['color'])
        width = float(request.form['width'])
        height = float(request.form['height'])
        wing_count = int(request.form['wing_count'])

        profile = Profile.query.get(profile_id)
        color = Color.query.get(color_id)

        perimeter = 2 * (width + height)
        length = perimeter * wing_count
        price = length * profile.unit_price * color.multiplier

        return render_template(
            'order_result.html',
            profile=profile,
            color=color,
            length=length,
            price=price,
        )
    return render_template('order.html', profiles=profiles, colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
