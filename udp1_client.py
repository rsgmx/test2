import socket, time

 

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

 

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(2)
 
# Send to server using created UDP socket
for x in range(20):
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    time.sleep(0.250)



msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(str(msgFromServer[0], 'utf-8'))
print(msg)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(str(msgFromServer[0], 'utf-8'))
print(msg)