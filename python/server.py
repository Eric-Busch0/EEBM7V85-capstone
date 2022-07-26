
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import request
import json
import pickle
import numpy as np
filename = 'ecg_svm'
model = pickle.load(open(filename, 'rb'))
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

 
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/',methods = ['POST'])
# ‘/’ URL is bound with hello_world() function.
def ml_predict():

    
    try:
        ret =json.loads(request.get_json())['data1']
        data = np.array(ret)
     
        prediction = model.predict(data)
        abnormal = 0
        normal = 0
        
        for x in prediction:
            if x == 1:
                normal +=1
            else:
                abnormal += 1
        
        result = {'normal': normal,
                  'abnormal': abnormal}
        
        return result
    
    except:
        return "Error parsing"
    return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()