
import requests
import scipy.io
import numpy as np
import json
from json import JSONEncoder
ENDPOINT = "http://127.0.0.1:5000"
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

x_test = scipy.io.loadmat('xtest.mat')['x_test'].astype(int)
data0 = np.transpose(x_test)[0].tolist()
data1 = np.transpose(x_test)[1].tolist()


json_str = json.dumps({'data1' :x_test.tolist()})
print(json_str)

resp = requests.post(ENDPOINT, json=json_str)

if resp.status_code == 200:
    print(resp.content)
else:
    print(resp.status_code)