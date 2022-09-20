import socket
import threading
import os

def cls():
    os.system('clear')

welcome_on_the_server_msg = """
Welcome on the X-Mail WW!

This server is an Server made by the programmers of X-Mail!
It is public and everyone with wifi and an working X-Mail Version can enter

Rules:
Don't be mean to somebody
No bullying 
Everyone is welcome!
No sexual content!

If we see bullying or something get's reported, the person who send the Mail gets BANNED for a lifetime!

Please follow the rules and everything will be fine!

Thank you!
Luis Schuimer (Head Programmer)
"""
already_registered_users_only = False
port = 8081
users = 0
h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)
print("Host Computer is: " + h_name)
print("Server IP Address is: " + IP_address)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_address, port))
server_socket.listen(1)

def functions(client_socket, addr, server_socket, users):
    print("Connection excepted...")
    action = ""
    while action == "":
        action = str(client_socket.recv(2081), "utf8")
    if action == "Data_list":
        print("Data list...")
        client_socket.send(bytes(str(users), "utf8"))
    if action == "Login":
        print("Login...")
        print("Getting Username")
        username = str(client_socket.recv(2081), "utf8")
        print("Getting Pass")
        password = str(client_socket.recv(2081), "utf8")
        print("Getting Email_addr")
        email_addr = str(client_socket.recv(2081), "utf8")
        print("Finished!")
        print(username)
        print(password)
        print(email_addr)
        try:
            index = 0
            err = False
            while err == False:
                with open(f"Server_DATA/USERS/{index}_user.txt", "r") as user_data_read:
                    user_in_file = user_data_read.read()
                    if user_in_file == username:
                        err = True
                        username = user_in_file
            print("[Login] User already registered...")
        except Exception as Error:
            print(Error)
            if already_registered_users_only == True:
                client_socket.send(bytes("""
                The server has declined your Login data!
                
                This server only accepts Login data from already registered users!
                When you should be in this server and you still getting this message,
                please speak with the server admin.
                
                Thank you!
                """))
            else:
                client_socket.send(bytes(welcome_on_the_server_msg, "utf8"))
                err = False
                index = 0
                print("Login started")
                try:
                    index = 0
                    while err == False:
                        index += 1
                        print(f"[Login] {index} is registered...")
                        with open(f"Server_DATA/USERS/{index}_user.txt", "r"):
                            continue
                except:
                    err = True
                try:
                    with open(f"Server_DATA/USERS/{index}_user.txt", "w")as user_username_write:
                        user_username_write.write(username)
                    with open(f"Server_DATA/USERS/{username}_pass.txt", "w")as user_pass_write:
                        user_pass_write.write(password)
                    with open(f"Server_DATA/USERS/{username}_emailaddr.txt", "w")as user_emailaddr_write:
                        user_emailaddr_write.write(email_addr)
                except Exception as Error:
                    print(f"[Server] Error: {Error}")
        print("[Login] Login finished!")





    print("Operation ended")
    cls()

print("Server ready to listen...")
while True:
    cls()
    print("Ready...")
    print("Host Computer is: " + h_name)
    print("Server IP Address is: " + IP_address)
    (client_socket, addr) = server_socket.accept()
    t1 = threading.Thread(target=functions(client_socket, addr, server_socket, users))
    t1.start()

