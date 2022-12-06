from flask import Flask, render_template

from controllers.homepage_controller import homepage_blueprint
from controllers.member_controller import members_blueprint
from controllers.class_controller import classes_blueprint
from controllers.booking_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(homepage_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)
app.register_blueprint(bookings_blueprint)

# @app.route('/')
# def home():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)