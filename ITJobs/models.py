from ITJobs import db


class Jobs(db.Model):
    __tablename__ = 'jobs'

    jobID = db.Column('jobID', db.String, primary_key=True)
    jobName = db.Column('jobName', db.String)
    jobCompanyName = db.Column('jobCompanyName', db.String)

    def __repr__(self):
        return f"Jobs('{self.jobID}', '{self.jobName}', '{self.jobCompanyName}')"