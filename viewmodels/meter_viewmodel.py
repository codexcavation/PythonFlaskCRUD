class MeterVM():
	def __init__(self,id, label):
		self.id = id
		self.label = label
		
	def json(self):
		return {"label":self.label}
