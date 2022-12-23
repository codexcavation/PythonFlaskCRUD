from models.meter_model import db, MeterModel


	
class MeterRepo():
		
	def getAllMeters():
		"""Gets All Meter records"""
		return MeterModel.query.all()
		
	def setMeter(label):
		"""Sets a new Meter record if it is not available or returns the same"""
		meter = MeterModel.query.filter_by(label=label).first()

		if not meter:
			meter = MeterModel(label=label)
			db.session.add(meter)
			db.session.commit()
		return meter
		
	def getByLabelMeter(label):
		"Gets the Meter record"
		return MeterModel.query.first()
		
	def deleteByLabelMeter(label):
		"Deletes the Meter record"
		meter = MeterModel.query.filter_by(label=label).first()
		if meter:
			db.session.delete(meter)
			db.session.commit()
		else:
			return "Not Found"
		return "Ok"
		
		
