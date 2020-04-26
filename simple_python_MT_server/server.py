# python2
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
#from http.server import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import time
import json
import math
import random
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        return

    def do_POST(self):
        print ('received')
        t1 = time.time()
        #time.sleep(2)
        result = 0

        for j in range(60):
            if random.randint(1,11)<2:
                for i in range(800000):
                    result += math.atan(i) * math.atan(i+1) * math.atan(i+2);
            else:time.sleep(1)
        t2 = time.time()
        self.send_response(200)
        self.end_headers()
        ret_dict = {"predicttime": t2-t1, "receivedTime": t1, "sentTime": t2}
        #print(""type(ret_dict))
        #print (ret_dict)
        self.wfile.write(json.dumps(ret_dict))
        #self.wfile.write("\n")
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8080), Handler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
