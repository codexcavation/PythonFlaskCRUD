from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm as orm
from sqlalchemy.sql import func 

db = SQLAlchemy()

class MeterModel(db.Model):
	__tablename__='meters'

	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(80), unique=True)
	meterdatamodel = db.relationship("MeterDataModel", back_populates="metermodel")
	#with_meter_data = orm.relationship('MeterDataModel', backref='meters', lazy=True)


	def __init__(self, id, label):
		if id!=-1:
			self.id = id
		self.label = label
	
	def json(self):
		return {"label":self.label}
		
		
class MeterDataModel(db.Model):
	__tablename__='meter_data'

	id = db.Column(db.Integer, primary_key=True)
	meter_id = db.Column(db.Integer, db.ForeignKey('meters.id', ondelete='CASCADE'),nullable=False)
	timestamp = db.Column(db.DateTime,server_default=func.now())
	value = db.Column(db.Integer)
	metermodel = db.relationship("MeterModel", back_populates="meterdatamodel")

	def __init__(self, meter_id, value):
		self.meter_id = meter_id
		#self.timestamp = timestamp
		self.value = value
		"""attrs = vars(self)
		print(', '.join("%s: %s" % item for item in attrs.items()))
		#self.meter_label = self.meter"""
		
	def json(self):
		return {"meterDataModel":{"meter_id":self.meter_id,"timestamp":self.timestamp,"value":self.value}}
