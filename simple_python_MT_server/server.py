# python3
from http.server import HTTPServer, BaseHTTPRequestHandler
#from http.server import BaseHTTPRequestHandler,HTTPServer
from socketserver import ThreadingMixIn
import threading
import time
import json
import math
import random

from PIL import Image
#from wand.image import Image as WImage


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        return

    def do_POST(self):
        print ('received')
        t1 = time.time()
        
        #time.sleep(5) 
        #imgList = []
        img = Image.open("/home/ubuntu/EC2_application/simple_python_MT_server/check.jpg")
        for i in range(0, 1000):
            #img = Image.open("check10.jpg")
            #imgList.append(img.getdata())
            img.rotate(30)
        img.close()
        del img
        #newImage = Image.blend(image1, image2, 0.5)

        t2 = time.time()
        self.send_response(200)
        self.end_headers()
        ret_dict = {"predicttime": t2-t1, "receivedTime": t1, "sentTime": t2}
        #print(""type(ret_dict))
        print (ret_dict)
        self.wfile.write(json.dumps(ret_dict).encode())
        #self.wfile.write("\n")
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8080), Handler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
