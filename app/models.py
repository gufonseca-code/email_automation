from app import db 

class EmailLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    error = db.Column(db.String(512), nullable=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
