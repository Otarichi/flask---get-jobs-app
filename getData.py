import requests
from bs4 import BeautifulSoup


def getAndInsertDataInDB(db, Jobs):
    Request = requests.get("https://jobs.ge/?page=1&q=&cid=6&lid=&jid=")
    soup = BeautifulSoup(Request.content, "html.parser")

    jobDiv = soup.find('div', class_="regularEntries").table
    for tr in jobDiv.findAll('tr'):
        jobName = None
        jobID = None
        jobCompanyName = None
        for td in tr.findAll('td'):
            try:
                jobID = td.img['id']
            except:
                pass
            try:
                if jobName == None:
                    jobName = td.a.text.strip()
                else:
                    jobCompanyName = td.a.text.strip()
            except:
                pass


        if jobName == None or jobID == None or jobCompanyName == None:
            pass
        else:
            try:
                db.create_all()
                job = Jobs(jobID=jobID, jobName=jobName, jobCompanyName=jobCompanyName)
                db.session.add(job)
                db.session.commit()
            except:
                pass


# def getDataFromDB():
#     try:
#         connect = sqlite3.connect('flaskBlogDB.sqlite')
#         c = connect.cursor()
#         c.execute("SELECT * FROM jobs")
#         return c.fetchall()
#     except:
#         return "No posts were found"
