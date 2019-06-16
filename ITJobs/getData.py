import requests
from bs4 import BeautifulSoup
from ITJobs import db
from ITJobs.models import Jobs


def getAndInsertDataInDB():
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
                job_01 = Jobs(jobID=jobID, jobName=jobName, jobCompanyName=jobCompanyName)
                db.session.add(job_01)
                db.session.commit()
            except:
                pass
