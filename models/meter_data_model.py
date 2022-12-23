from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MeterDataModel(db.Model):
	__tablename__='meter_data'

	id = db.Column(db.Integer, primary_key=True)
	meter_id = db.Column(db.Integer, ForeignKey('meters.id', ondelete='CASCADE'),nullable=False)
	backref=backref("meters", uselist=False))

	def __init__(self, label):
		self.label = label
	
	
