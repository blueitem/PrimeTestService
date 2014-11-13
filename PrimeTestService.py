""" 
   PrimeTestService is a class that checks whether a number is a Prime number or not.
   It also prints a list of prime numbers up to a given point, which is established by 
   a user input

   Developer: Jovaughn Chin
   Date:      11/13/2014

"""

import rpyc
import math

from rpyc.utils.server import ThreadedServer

class PrimeTestService(rpyc.Service):

	prime_num = []

    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass
 
    
    # Exposed method that checks whether or not a number is a prime

    def exposed_is_prime(self, num): 
        
         valid = False

        if num < 2:
            return valid

        i = int(math.sqrt(num) + 1)

        while (num % i) != 0:
            i -= 1

        if i == 1:
            valid = True

        return valid


# Exposed method that output prime numbers up to a given number

    def exposed_get_primes(self,x): 

        if (x >= 2):
            self.prime_num.append(2)

        for y in range(1,x+1,2):
            if self.is_prime(y):
                self.prime_num.append(y)

        print (" ".join(str(e) for e in self.prime_num))


if __name__ == '__main__':
   s = ThreadedServer(PrimeTestService, port=12345)
   s.start()