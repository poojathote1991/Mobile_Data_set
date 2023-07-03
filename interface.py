from flask import Flask,jsonify,request,render_template
from utils import MobileData
import config
app=Flask(__name__)

@app.route('/')
def home_page():

    return render_template("mobile_price.html")

@app.route('/predicted_price',methods=['GET','POST'])
def predicted_price():
    data=request.args.get
    if request.method=='GET':
        print("Data: ",data)
        Sale=eval(data('Sale'))
        weight=eval(data('weight'))
        resoloution=eval(data('resoloution'))
        ppi=eval(data('ppi'))
        cpu_core=eval(data('cpu_core'))
        cpu_freq=eval(data('cpu_freq'))
        internal_mem=eval(data('internal_mem'))
        ram=eval(data('ram'))
        RearCam=eval(data('RearCam'))
        Front_Cam=eval(data('Front_Cam'))
        battery=eval(data('battery'))
        thickness=eval(data('thickness'))
        mobile=MobileData(Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness)
        pred_price=mobile.get_predicted_mobile_price()
        return render_template("mobile_price.html",prediction=pred_price)
    
    elif request.method=='POST':
        print("Data: ",data)
        Sale=data['Sale']
        weight=data['weight']
        resoloution=data['resoloution']
        ppi=data['ppi']
        cpu_core=data['cpu_core']
        cpu_freq=data['cpu_freq']
        internal_mem=data['internal_mem']
        ram=data['ram']
        RearCam=data['RearCam']
        Front_Cam=data['Front_Cam']
        battery=data['battery']
        thickness=data['thickness']

        mobile=MobileData(Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness)
        pred_price=mobile.get_predicted_mobile_price()
        return render_template("mobile_price.html",prediction=pred_price)
if __name__== "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER) 