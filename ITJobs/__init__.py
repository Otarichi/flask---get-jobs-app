from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///flaskBlogDB.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from ITJobs import routes
