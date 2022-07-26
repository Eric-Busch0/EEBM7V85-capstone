
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import request
import json
import pickle
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
    print(request.data)
    try:
        data = json.loads(request.data)['data']
        model.predict(data)
    except:
        return "Error parsing"
    return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()