"""handler_img"""

import json
import random
import time
from PIL import Image
# from wand.image import Image as WImage

def lambda_handler(event, context):
    t1 = time.time()
    img = Image.open("check.jpg")
    for i in range(0, 850):
        img.rotate(30)
    img.close()
    del img
    t2 = time.time()
    ret_message = {'predicttime': t2-t1, 'receivedTime': t1, 'sentTime': t2}
    # return {'statusCode': 200, 'predicttime': t2-t1, 'receivedTime': t1, 'sentTime': t2}

    out = {
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
                },
            # "body": {'predicttime': t2-t1, 'receivedTime': t1, 'sentTime': t2},
            "body": json.dumps(ret_message),
            "statusCode": 200
          }
    return out

if __name__ == "__main__":
    lambda_handler(None, None)