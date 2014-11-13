""" 
    Prime Service for Server, connects on port 12345
    PrimeService is a class that checks whether a number is a Prime number or not.

   (Python 3.4.2)
   
   Author: Jovaughn Chin
           Jonathan Gonzoph

   Date:   11/13/2014

"""

#import statement, math for sqrt in checkPrime, rpyc for connection
import math
import rpyc


class PrimeService(rpyc.Service):

   prime_num = []

   #unused
    def on_connect(self):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass
    #unused
    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    #given an integer, checks whether that integer is prime and returns true or false
    def exposed_isPrime(self,number):


        if number < 2:
            return False

        for i in range(2,int(math.sqrt(number)+1)):
            if (number % i) == 0:
                return False
        return True

#starts the service on port 12345
from rpyc.utils.server import ThreadedServer

if __name__ == "__main__":
    
    t = ThreadedServer(PrimeService, port = 12345)
    t.start()