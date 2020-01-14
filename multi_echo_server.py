import socket
import time 
from multiprocessing import Process

HOST = ""   # localhost
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2) # can only server 2 clients

        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started Process", p)

def handle_echo(addr, conn):
    full_data = conn.recv(BUFFER_SIZE)
    print("Connected by", addr)
    time.sleep(0.5)
    print("Sending", full_data)
    conn.sendall(full_data)
    conn.close()
        
main()

