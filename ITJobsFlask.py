from flask import Flask, render_template, redirect, url_for
from getData import getAndInsertDataInDB
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///flaskBlogDB.sqlite'
db = SQLAlchemy(app)


class Jobs(db.Model):
    jobID = db.Column(db.String(15), primary_key=True)
    jobName = db.Column(db.String(100), nullable=False)
    jobCompanyName = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Jobs('{self.jobID}', '{self.jobName}', '{self.jobCompanyName}')"


@app.route('/')
def index():
    getAndInsertDataInDB(db, Jobs)
    return render_template('jobs.html', jobs=Jobs.query.all())


app.run(host='localhost', port=8080, debug=True)