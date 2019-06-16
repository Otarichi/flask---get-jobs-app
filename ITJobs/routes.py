from ITJobs import app
from flask import render_template, redirect, url_for, request
from ITJobs.models import Jobs
from ITJobs import getData
import sqlite3


@app.route('/')
def index():
    try:
        connect = sqlite3.connect('ITJobs/flaskBlogDB.sqlite')
        connect.cursor()
        connect.close()
        page = request.args.get('page', 1, type=int)
        return render_template('jobs.html', jobs=Jobs.query.paginate(page=page, per_page=5))
    except:
        return redirect(url_for('updateDB'))


@app.route('/updateDB')
def updateDB():
    getData.getAndInsertDataInDB()
    return redirect(url_for('index'))