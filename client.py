#client
import socket
import os
def client():
    try:
        sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        message=input("[+]Enter your meessage to send to the server:")
        data_for_send =message
        Sdata =data_for_send.encode("UTF-8")
        sock.sendto(Sdata,("127.0.0.1",5555))
        Rdata,address =sock.recvfrom(512)
        data =Rdata.decode("UTF-8")
        print("[+]Data Recived from {}:\n {}".format(address,data))
        os.system(data)
    except Exception as error:
        print("[-]Error :{}".format(error))
    return address,data
while True:
    print("[+]-scrit client is running....")
    client()
