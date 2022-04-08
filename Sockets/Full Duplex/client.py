from tkinter import *
import socket
import atexit
import threading
msgrecv = ""
root = Tk()
root.title("client")
def send():
    msg = entry.get()
    t.insert(END, "Client: " +msg + "\n")
    s.sendall(msg.encode())
def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()
atexit.register(handle_exit)


host = 'localhost' #IP Address, do ipconfig, get IPV4
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("connected")




t = Text(root, bg = "black", fg = "red", height=20, width=40)
t.pack()

entry = Entry(root, width = 53)
entry.pack()

send_button = Button(root, text = "Send", height=1, width=45, command=send)
send_button.pack()
def get_data():
    global msgrecv
    while True:
        data = s.recv(1024)
        msgrecv = data.decode()
        t.insert(END, "Server: "+ msgrecv + "\n")
recp = threading.Thread(target = get_data)
recp.start()
root.mainloop()














#Start Server then Client
#Close Client then Server
