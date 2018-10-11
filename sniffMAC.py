import socket
from parse import *
from getmac import get_mac_address

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_addr = s.getsockname()[0]
s.close()

ip_field = parse("{}.{}.{}.{}", ip_addr)
ip_router = "{}.{}.{}.1".format(ip_field[0], ip_field[1], ip_field[2])
print(ip_router)

ip_mac = get_mac_address(ip=ip_router)
print(ip_mac)