from pprint import pprint

from phue import Bridge

from settings import ip_address

b = Bridge(ip_address)

b.connect()

pprint(b.get_api())

lights = b.lights

print()
print("Lights:")
pprint([l.name for l in lights])
