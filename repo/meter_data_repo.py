from models.meter_model import db, MeterDataModel, MeterModel
from repo.meter_repo import MeterRepo
from  getlineno import PrintException

	
class MeterDataRepo():
		
	def getAllMeterDatas():
		#Gets All Meter records
		return MeterDataModel.query.all()
		
	def setMeterData(meter_id, value):
		#Sets a new MeterData record if it is not available or returns the same
		try:
			meterData = MeterDataModel(meter_id=meter_id, value=value)
			db.session.add(meterData)
			db.session.commit()
			return meterData
		except ValueError as e:
			#PrintException()
			return "Invalid Meters"
		except Exception as e:
			#PrintException()
			return "Unknown Error"#
			
	def getAllMeterDataByMeterId(meter_id):
		#Gets the Meter record
		return MeterDataModel.query.filter_by(meter_id=meter_id).order_by(MeterDataModel.timestamp).all()		
		
