"""
Connecting and conversing with httpbin.org using sockets
"""
import socket


sock = socket.socket()
sock.connect(('httpbin.org', 80))
sock.sendall(
        b'GET /ip HTTP/1.1\r\n'
        b'Host: httpbin.org:80\r\n'
        b'User-Agent: connect-sock.py\r\n'
        b'Connection: close\r\n'
        b'\r\n')

reply = sock.recv(10240).decode()
reply = reply.split('\r\n')
print(reply[-1])
