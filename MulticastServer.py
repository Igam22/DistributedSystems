import socket
import struct

# defining variables 
multicast_address = '224.1.1.1' #get local address
multicast_port = 5050
IS_ALL_GROUPS = True
buffer_size=1024
listening = True


multicast_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#binding socket to the local adress
multicast_server_socket.settimeout(120)

multicast_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if IS_ALL_GROUPS:
  multicast_server_socket.bind(("", multicast_port))
else:
  multicast_server_socket.bind((multicast_address, multicast_port))
mreq = struct.pack('4sl', socket.inet_aton(multicast_address), socket.INADDR_ANY)

multicast_server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print(f"Server is listening for multicast messages on {multicast_address}:{multicast_port}")
while listening:
    try:
        data, addr = multicast_server_socket.recvfrom(buffer_size)
        print(f"Received message from {addr}: {data.decode()}")
    except socket.timeout:
        print(f"timed out")
        listening = False



