from models.meter_model import db, MeterModel


	
class MeterRepo():
		
	def getAllMeters():
		"""Gets All Meter records"""
		return MeterModel.query.all()
		
	def setMeter(label):
		"""Sets a new Meter record if it is not available or returns the same"""
		meter = MeterModel.query.filter_by(label=label).first()

		if not meter:
			meter = MeterModel(id=-1,label=label)
			db.session.add(meter)
			db.session.commit()
		else:
			return "Already Exists"
		return meter
		
	def getByLabelMeter(label):
		"Gets the MeterData records"
		return MeterModel.query.filter_by(label=label).first()
		
	def deleteByLabelMeter(label):
		"Deletes the Meter record"
		meter = MeterModel.query.filter_by(label=label).first()
		if meter:
			db.session.delete(meter)
			db.session.commit()
		else:
			return "Not Found"
		return "Ok"
		
		
