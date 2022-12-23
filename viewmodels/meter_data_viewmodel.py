import json

class MeterDataVM():
	def __init__(self, meter_id, timestamp, value, meter_label):
		self.meter_id = meter_id
		self.timestamp = timestamp
		self.value = value
		self.meter_label = meter_label
		
	def json(self):
		return {"meter_id":self.meter_id,"meter_label":self.meter_label,"timestamp":str(self.timestamp),"value":self.value}

	def fromModel(MeterDataModel, meter_label):
		return MeterDataVM(meter_id=MeterDataModel.meter_id,timestamp=MeterDataModel.timestamp,value=MeterDataModel.value,meter_label=meter_label)
