from tkinter import *
import socket
import atexit
import threading
msgrecv = ""

    
def connect():
    global entry, t, s, username
    host = 'localhost' #IP Address, do ipconfig, get IPV4
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("connected")
    username = userentry.get()
    s.sendall(username.encode())

    

    #unpack
    label.pack_forget()
    userentry.pack_forget()
    userentry.pack_forget()
    connect_button.pack_forget()

    #Chat interface
    t = Text(root, bg = "black", fg = "white", height=20, width=40)
    t.pack()

    entry = Entry(root, width = 53)
    entry.pack()

    send_button = Button(root, text = "Send", height=1, width=45, command=send)
    send_button.pack()

    recp = threading.Thread(target = get_data)
    recp.start()

def send():
    global t, s, entry, username
    msg = entry.get()
    s.sendall(msg.encode())

root = Tk()
root.title("Client")
label = Label(root, text = "Enter your username")
label.pack()
userentry = Entry(root)
userentry.pack()
connect_button = Button(root, text="Login", command=connect)
connect_button.pack()


def get_data():
    global msgrecv, s, t
    while True:
        data = s.recv(1024)
        msgrecv = data.decode()
        t.insert(END, msgrecv + "\n")


# msgrecv = ""
# root = Tk()
# root.title("client")
# def send():
#     msg = entry.get()
#     t.insert(END, "Client: " +msg + "\n")
#     s.sendall(msg.encode())
# def handle_exit():
#     print("This runs after keyboard interrupt")
#     s.close()
# atexit.register(handle_exit)


# host = 'localhost' #IP Address, do ipconfig, get IPV4
# port = 12345
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host, port))

# print("connected")




# t = Text(root, bg = "black", fg = "red", height=20, width=40)
# t.pack()

# entry = Entry(root, width = 53)
# entry.pack()

# send_button = Button(root, text = "Send", height=1, width=45, command=send)
# send_button.pack()
# 
root.mainloop()














#Start Server then Client
#Close Client then Server
