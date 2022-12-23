from flask import Flask,render_template,request
from flask_restful import Api, Resource
from repo.meter_repo import MeterRepo
from viewmodels.meter_viewmodel import MeterVM
from models.meter_model import db

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
	db.create_all()

# ideal case above 6 lines and also "db" must not be placed here, all general config related must be grouped and placed outside which I couldn't quite figure out how

class MeterListApi(Resource):
	def get(self):
		meterModels = MeterRepo.getAllMeters()
		print(meterModels)
		meter_viewmodels=[]
		for itm in meterModels:
			meter_viewmodels.append(MeterVM(itm.id,itm.label))
		return {'Meters':list(x.json() for x in meter_viewmodels)}

"""def post(self):
		data = request.get_json()
		new_meter = MeterModel(data['label'])
		db.session.add(new_meter)
		db.session.commit()
		return new_meter.json(),201"""


class Meter(Resource):
	def get(self,label):
		meterModel = MeterRepo.getByLabelMeter(label)
		if meterModel:
			meter_viewmodel = MeterVM(meterModel.id,meterModel.label)
			return meter_viewmodel.json()
		return {'message':'meter not found'},404

	def put(self,label):
		meterModel = MeterRepo.setMeter(label)
		meter_viewmodel = MeterVM(meterModel.id,meterModel.label)
		return meter_viewmodel.json()

	def delete(self,label):
		status = MeterRepo.deleteByLabelMeter(label)
		if status == "Ok":
			return {'message':'Deleted'}
		return {'message':'meter not found'},404

@app.route('/')
def RetrieveDataList():
	meterModels = MeterRepo.getAllMeters()
	print(meterModels)
	meter_viewmodels=[]
	for itm in meterModels:
		meter_viewmodels.append(MeterVM(itm.id,itm.label))
	return render_template('index.html',meterModels = meter_viewmodels)
	
api.add_resource(MeterListApi, '/api/meters')
api.add_resource(Meter,'/meter/<string:label>')

if __name__ == '__main__':
	app.run(host='localhost', port=5000)
