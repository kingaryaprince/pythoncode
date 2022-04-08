from tkinter import *
import socket
import atexit
import threading


msgrecv = ""
root = Tk()
root.title("server")
def send():
    msg = entry.get()
    t.insert(END, "Server: "+ msg + "\n")
    conn.sendall(msg.encode())

def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()

atexit.register(handle_exit)

#Tkinter Labels/Text
t = Text(root, bg = "black", fg = "red", height=20, width=40)
t.pack()

entry = Entry(root, width = 53)
entry.pack()

send_button = Button(root, text = "Send", height=1, width=45, command=send)
send_button.pack()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345

s.bind((host, port))

s.listen(5)
print('Socket is listening')
conn, addr = s.accept()
print('Got a connection from ', addr)
def get_data():
    global msgrecv
    while True:
        data = conn.recv(1024)
        msgrecv = data.decode()
        print(addr, ":", msgrecv)
        t.insert(END, "Client: "+ msgrecv + "\n")

recp = threading.Thread(target = get_data)
recp.start()
root.mainloop()























#Start Server then Client
#Close Client then Server 