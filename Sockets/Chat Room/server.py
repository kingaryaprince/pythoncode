from tkinter import *
import socket
import atexit
import threading
msgrecv = ""
connections = {}



root = Tk()
root.title("server")
def send():
    msg = entry.get()
    conn.sendall(msg.encode())

def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()

atexit.register(handle_exit)

#Tkinter Labels/Text


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345

s.bind((host, port))

def get_data(username, conn):
    while True:
        try:
            data = conn.recv(1024)
            msgrecv = data.decode()
            msgrecv = username + ": " + msgrecv
            send_everyone(msgrecv)
        except:
            del connections[username]
            send_everyone(username + " has left the chat")


def send_everyone(message):
    message = message.encode()
    for x in connections:
        connections[x].send(message)

while True:
    s.listen(5)
    print('Socket is listening')
    conn, addr = s.accept()
    print('Got a connection from ', addr)

    data = conn.recv(1024)
    msgrecv = data.decode()
    connections[msgrecv] = conn
    send_everyone(msgrecv + " has joined the chat")
    print(connections)
    recp = threading.Thread(target = get_data, args=(msgrecv, conn))
    recp.start()



























#Start Server then Client
#Close Client then Server 