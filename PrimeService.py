# Author: Jon Gonzoph

# Prime Service for Server, connects on port 12345

import math
import rpyc

class PrimeService(rpyc.Service):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def exposed_checkPrime(self,number):
        for i in range(2,int(math.sqrt(number)+1)):
            if (number % i) == 0:
                return False
        return True

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PrimeService, port = 12345)
    t.start()