from flask import Flask,render_template,request
from flask_restful import Api, Resource
from repo.meter_repo import MeterRepo
from repo.meter_data_repo import MeterDataRepo
from viewmodels.meter_viewmodel import MeterVM
from viewmodels.meter_data_viewmodel import MeterDataVM
from models.meter_model import db

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meters_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
	db.create_all()

# ideal case above 6 lines and also "db" must not be placed here, all general config related must be grouped and placed outside which I couldn't quite figure out how


class Meter(Resource):
	
	def get(self,id):
		meterDataModels = MeterDataRepo.getAllMeterDataByMeterId(id)
		if meterDataModels:
			meter_viewmodels=[]
			for itm in meterDataModels:				meter_viewmodels.append(MeterDataVM.fromModel(itm,itm.metermodel.label).json())
			return meter_viewmodels
		return {'message':'meter not found'},404		

	def post(self,label):
		meterModel = MeterRepo.setMeter(label)
		if meterModel == "Already Exists":
			return {'message':'Already Exists'},406
		meter_viewmodel = MeterVM(meterModel.id,meterModel.label)
		return meter_viewmodel.json()

	def delete(self,label):
		status = MeterRepo.deleteByLabelMeter(label)
		if status == "Ok":
			return {'message':'Deleted'}
		return {'message':'meter not found'},404

class MeterData(Resource):
	
	def post(self,label):
		print(MeterRepo.getByLabelMeter(label))
		meter_id=int(MeterRepo.getByLabelMeter(label).id)
		meterDataModel = MeterDataRepo.setMeterData(meter_id=meter_id, value=int(request.form['value']))
		if str(type(meterDataModel)) == "<class 'str'>":
			return {'message':meterDataModel},406
		meterData_viewmodel = MeterDataVM(meter_id=meterDataModel.meter_id,timestamp=meterDataModel.timestamp, value=meterDataModel.value,meter_label=meterDataModel.metermodel.label)
		return meterData_viewmodel.json()
				
@app.route('/meters')
def RetrieveDataList():
	meterModels = MeterRepo.getAllMeters()
	meter_viewmodels=[]
	for itm in meterModels:
		meter_viewmodels.append(MeterVM(itm.id,itm.label))
	return render_template('index.html',meterModels = meter_viewmodels)
	
#api.add_resource(Meter,'/meters/upload/<string:label>')
#api.add_resource(MeterData,'/meters_data/upload/<string:label>')
api.add_resource(Meter,'/meters/<int:id>')#While entering data 

if __name__ == '__main__':
	app.run(host='localhost', port=5000)
