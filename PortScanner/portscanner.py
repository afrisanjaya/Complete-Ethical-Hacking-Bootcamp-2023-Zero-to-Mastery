import socket
import termcolor

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        spck.connect((ipaddress,port))
        print("[+] Port Opened " + str(port))
        sock.close
    except:
        print("[-] Port Closed "+ str(port))

