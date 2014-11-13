""" RPyc Client


Developer: Jovaughn Chin

"""


# import RPyc Python 3.4
import rpyc

#ask Client the location/server of the Service he wish to access

serviceAddress= input(" What is the IP of the Service you wish to access?")

empty_str=""

if serviceAddress==empty_str:
	serviceAddress=input("Sorry, no input given. What is the IP of the Service you wish to access?")

# connect to server
c=rypc.connect(serviceAddress,1234) 


num =int( input("What number would you like to check if prime?))

print(c.root.is_prime(num))

print(c.root.get_primes())

