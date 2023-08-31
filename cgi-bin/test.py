#!/usr/bin/python3
import time
import math
import ast
import json
import requests
def lambda_handler():
    t1 = time.time()
    res = 0 
    for x in range(300000,-1, -1):
        a = math.atan(x) * math.atan(x+1)*math.atan(x+2) 
        res = res + a
    t2 = time.time()
    delta = t2 - t1
    response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    instance_id = response.text
    return {
        'statusCode': 200,
        "predicttime": str(delta),
        "receivedTime": t1,
        "sentTime": t2,
        "instance_id": instance_id
        }
print('Content-type: application/json') # the mime-type header.
print() # header must be separated from body by 1 empty line.

ret = lambda_handler()
print(json.dumps(ret))
