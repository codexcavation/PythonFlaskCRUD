from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MeterModel(db.Model):
	__tablename__='meters'

	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(80))

	def __init__(self, label):
		self.label = label
	
	def json(self):
		return {"label":self.label}
