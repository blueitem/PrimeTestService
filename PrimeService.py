# Author: Jon Gonzoph

# Prime Service for Server, connects on port 12345

# import statement, math for sqrt in checkPrime, rpyc for connection
import math
import rpyc


class PrimeService(rpyc.Service):

    # unused
    def on_connect(self):
        pass

    #unused
    def on_disconnect(self):
        pass

    #given an integer, checks whether that integer is prime and returns true or false
    def exposed_checkPrime(self,number):
        for i in range(2,int(math.sqrt(number)+1)):
            if (number % i) == 0:
                return False
        return True

#starts the service on port 12345
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PrimeService, port = 12345)
    t.start()