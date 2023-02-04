#server
import socket
def server():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #set ip ,set port
    s.bind(("127.0.0.1",5555))
    Rdata,address =s.recvfrom(1024)
    data =Rdata.decode("UTF-8")
    message=input("[+]Enter your message to send to client:")
    data_for_send =message
    Sdata =data_for_send.encode("UTF-8")
    print("message recived:{} from {}".format(data,address))
    s.sendto(Sdata,address)
    return Sdata,address
print("[+]Server is running....")
while True:
    
    server()
