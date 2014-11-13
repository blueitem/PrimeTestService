""" RPyc Client

(Python 3.4.2)

Developer: Jovaughn Chin
Date:      11/13/2014

"""


# import RPyc Python 3.4
import rpyc
import ipaddress

#ask Client the location/server of the Service he wish to access
IPAddress= input(" What is the location(IP) of the server you wish to access?")

empty_str=""

#Validate IP address
try:
 ipaddress.ip_address(IPAddress)

except ValueError:
	IPAddress=input("Sorry, wrong input. Please input correct location(IP) of the server you wish to access?")

# connect to server
c=rypc.connect(IPAddress,12345) 


num =int( input("What number would you like to check if prime?))

print(c.root.is_prime(num))

print(c.root.get_primes(num))

