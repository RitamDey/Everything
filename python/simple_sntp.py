import socket
import struct
import time


# NTP Server for India and seconds till epoch
NTP_SERVER = "0.in.pool.ntp.org"
TIME1970 = 2208988800


def sntp_client():
    # Create a UDP socket 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # The magic data that needs to be sent to get the time.
    data = b'\x1b' + 47*b'\0'
    # Use .sendto to sent the data to the server
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)

    if data:
        print("Response recieved from {0}".format(address))

    # Unpack the data and get the 11th element 
    t = struct.unpack('!12I', data)[10]
    # Since its in seconds substract i from epoch
    t -= TIME1970

    # time.ctime converts the seconds into 24 Hrs clock
    print('\tTime %s' %time.ctime(t))


if __name__ == '__main__':
    sntp_client()
