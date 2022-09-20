import os
import socket as s
import time as t
from getpass import getpass

import colorama
from colorama import Back, Fore
from rich.console import Console
from rich.theme import Theme

global users_in_server, index_emails, selected_server_name, selected_server_ip

colorama.init(autoreset=True)

themes = Theme({"title": "underline yellow", "error": "bold red", "sucsess": "bold green"})
console = Console(theme=themes)


def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key ", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)


def decrypt(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)


def settings(message, after):
    cls()
    logo_popup()
    console.print(Fore.YELLOW + "Settings for X-Mail" + Back.CYAN)
    if message == "Supans":  # Set up a new server
        err = False
        counter = 0
        print()
        print("How to set up a server for X-Mail?")
        print("""
        
You need to set up a server in order to use X-Mail. Please ask the admin of the server you want to use, which ip address and port the server has. When you have the required information you can set up the server here!
One more Thing there is a X-MailWorldWide Server provided by us! IP: 194.233.174.185 Port: 8081        """)
        print("——————————————————————————————————————————————————————————————————————————————————")
        server_name = input("Name of the Server (You can name the server whatever you want): ")
        server_ip = input("Ip adress of the Server (The full server Ip Adress): ")
        server_port = input("Port of the Server: ")
        print("——————————————————————————————————————————————————————————————————————————————————")
        cls()
        logo_popup()
        print("Saving the server data on your PC...")
        while err == False:
            counter = counter + 1
            try:
                with open(f"PROGRAM_DATA/Servers/server{counter}", "r")as test:
                    test_var = test.read()
            except:
                try:
                    with open(f"PROGRAM_DATA/Servers/server{counter}.txt", "w") as name_server_open:
                        name_server_open.write(server_name)
                    encrypt(f"PROGRAM_DATA/Servers/server{counter}.txt")
                    print(f"[Info] Name in PROGRAMM_DATA/Servers/server1.txt...")
                    with open(f"PROGRAM_DATA/Servers/{server_name}_config_ip.txt", "w") as ip_server:
                        ip_server.write(server_ip)
                    encrypt(f"PROGRAM_DATA/Servers/{server_name}_config_ip.txt")
                    print(f"[Info] ip in PROGRAMM_DATA/Servers/{server_name}_config_ip.txt...")
                    with open(f"PROGRAM_DATA/Servers/{server_name}_config_port.txt", "w") as port2_server:
                        port2_server.write(server_port)
                    encrypt(f"PROGRAM_DATA/Servers/{server_name}_config_port.txt")
                    print(f"[Info] port in PROGRAMM_DATA/Servers/{server_name}_config_port.txt...")
                    print(f"[{Fore.GREEN}Status{Fore.WHITE}] Data was saved as the {counter}. Server")
                    print(f"[{Fore.GREEN}Status{Fore.WHITE}] Server Data successfully saved on your PC!")
                    print()
                    if after == False:
                        input("Press enter to start X-Mail again...")
                        cls()
                        main()
                    input("Press enter to start the next step...")
                    err = True
                    cls()
                except:
                    error("Error: 002: Disk access denied")
                    err = True
        if after == "Caa":  # Create a Account
            settings(after, False)
    if message == "Caa":
        print("Create an account")
        print("""
        
        To register a new account you need to type in your name, your email adress you want to have and a password
        That's it! After that you can log in to servers and use our service. 100% Free!!
        """)
        print("——————————————————————————————————————————————————————————————————————————————————")
        new_name = input("Your full Name (Or your Username if you want!): ")
        new_email = input("Type in your new email for example (name.birthday): ")
        if new_email == "":
            new_email = f"{new_name}@x-mail.email"
        new_pass2 = ""
        new_pass = getpass("New Password (Your password won't be displayed!): ")
        while not new_pass == new_pass2:
            new_pass2 = getpass("Repeat Password (Your password won't be displayed!): ")

        print("——————————————————————————————————————————————————————————————————————————————————")
        try:
            with open(f"PROGRAM_DATA/User_DATA/username.txt", "w") as name_user_open:
                name_user_open.write(new_name)
            encrypt(r"PROGRAM_DATA\User_DATA\username.txt")
            print(f"[Info] Name in PROGRAMM_DATA/User_DATA/username.txt...")
            with open(f"PROGRAM_DATA/User_DATA/password.txt", "w") as pass_user_open:
                pass_user_open.write(new_pass)
            encrypt(r"PROGRAM_DATA\User_DATA\password.txt")
            print(f"[Info] ip in PROGRAMM_DATA/User_DATA/password.txt...")
            with open(f"PROGRAM_DATA/User_DATA/email_addr.txt", "w") as user_addr_open:
                user_addr_open.write(new_email)
            encrypt(r'PROGRAM_DATA\User_DATA\email_addr.txt')
            print(f"[Info] port in PROGRAMM_DATA/User_DATA/email_addr.txt...")
            print(f"[{Fore.GREEN}Status{Fore.WHITE}] Server Data successfully saved on your PC!")
            input("Press enter to start X-Mail again...")
        except:
            error("Error: 002: Disk access denied")


def cls():
    os.system('cls')


def success(message):
    console.print(f"Success: {message}", style="sucsess")


def error(message):
    cls()
    logo_popup()
    console.print(f"An error has occurred: {message}", style="error")
    if "Error: 004:" in message:
        print("If you press enter the program will restart automatically")
    input("Press enter to continue...")
    if "Error: 004:" in message:
        main()
    if "Error: 001:" in message:
        settings("Supans", False)


def logo_popup():
    # Setup start
    print("""

   _  __      __  ___      _ __
  | |/ /     /  |/  /___ _(_) /
  |   /_____/ /|_/ / __ `/ / / 
 /   /_____/ /  / / /_/ / / /  
/_/|_|    /_/  /_/\__,_/_/_/   """)


def main():
    global users_in_server, index_emails
    with open("PROGRAM_DATA/User_DATA/FIRSTOPEN.txt", "r") as fopen_r:
        FOPEN = fopen_r.read()
        print(FOPEN)
        if FOPEN == "TRUE":
            cls()
            print("Welcome to...")
            logo_popup()
            print()
            print("Thank you for choosing X-Mail!\n"
                  "Before you can start you need to register a server and register an account.\n"
                  "After that you are ready to go!")
            input("Press enter to continue...")
            with open("PROGRAM_DATA/User_DATA/FIRSTOPEN.txt", "w") as fopen_w:
                fopen_w.write("TRUE")
            settings("Supans", "Caa")
    err = False
    counter = 0
    cls()
    logo_popup()
    print("(C)2022 X-Mail Coperation")
    print("Stand with " + Fore.BLUE + "Ukra" + Fore.YELLOW + "ine")
    t.sleep(2)
    cls()
    logo_popup()
    print("----------Registered servers in X-Mail--------------")
    while err == False:
        counter = counter + 1
        try:
            client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
            decrypt(f"PROGRAM_DATA/Servers/server{counter}.txt", f"PROGRAM_DATA/Servers/server{counter}.txt.key")
            with open(f"PROGRAM_DATA/Servers/server{counter}.txt", "r") as server:
                server_name = server.read()
            encrypt(f"PROGRAM_DATA/Servers/server{counter}.txt")
            decrypt(f"PROGRAM_DATA/Servers/{server_name}_config_ip.txt", f"PROGRAM_DATA/Servers/{server_name}_config_ip.txt.key")
            with open(f"PROGRAM_DATA/Servers/{server_name}_config_ip.txt", "r") as ipaddr:
                server_ip = ipaddr.read()
            encrypt(f"PROGRAM_DATA/Servers/{server_name}_config_ip.txt")
            decrypt(f"PROGRAM_DATA/Servers/{server_name}_config_port.txt", f"PROGRAM_DATA/Servers/{server_name}_config_port.txt.key")
            with open(f"PROGRAM_DATA/Servers/{server_name}_config_port.txt", "r") as port_server:
                server_port = port_server.read()
            encrypt(f"PROGRAM_DATA/Servers/{server_name}_config_port.txt")
            client_socket.connect((server_ip, int(server_port)))
            client_socket.send(bytes("Data_list", "utf8"))
            users_in_server = str(client_socket.recv(2028), "utf8")
            client_socket.close()
            print(f"""
Server ---{server_name}--------
Name: {server_name}
Users online: {users_in_server}
-------------------------------
""")
        except Exception as erro:
            print(erro)
            input()
            if erro == 2:
                error("Error: 005: The Server couldn't be found!")
            error("Error: 001: No server registered!")
            err = True
        err = True
    counter = 0
    print("----------------------------------------------------")
    selected_server = input("Enter the server name you want to connect to: ")
    err = False
    selected_server_name = ""
    while err == False:
        try:
            counter = counter + 1
            with open(f"PROGRAM_DATA\Servers\server{counter}.txt", "r")as name_server:
                server_name = name_server.read()
                if server_name == selected_server:
                    err = True
                    selected_server_name = selected_server
                    with open(f"PROGRAM_DATA/Servers/{selected_server_name}_config_ip.txt", "r")as server_ip_read:
                        selected_server_ip = server_ip_read.read()
                    with open(f"PROGRAM_DATA/Servers/{selected_server_name}_config_port.txt", "r")as server_port_read:
                        selected_server_port = server_port_read.read()

        except Exception as Error:
            if selected_server_name == "":
                error("Error: 004: Server name couldn't be found in the registered servers. Please check your input!")
            err = True
    cls()
    print(f"Connencting to {selected_server_name}...")
    try:
        with open("PROGRAM_DATA/User_DATA/username.txt", "r") as name_user_read:
            username_login = name_user_read.read()
        with open("PROGRAM_DATA/User_DATA/password.txt", "r")as pass_user_read:
            password = pass_user_read.read()
        with open("PROGRAM_DATA/User_DATA/email_addr.txt", "r")as email_addr_read:
            email_addr = email_addr_read.read()

        client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        client_socket.connect((selected_server_ip, int(selected_server_port)))
        print("Logging in...")
        client_socket.send(bytes("Login", "utf8"))
        t.sleep(0.2)
        client_socket.send(bytes(username_login, "utf8"))
        client_socket.send(bytes(password, "utf8"))
        t.sleep(0.2)
        client_socket.send(bytes(email_addr, "utf8"))
        message_back_login = str(client_socket.recv(2081), "utf8")
        print(message_back_login)
        client_socket.close()
        input("Press enter to continue...")
        main_menu(users_in_server, selected_server_ip, selected_server_port)
    except Exception as Error:
        print(Error)


def main_menu(users_in_server, selected_server_ip, selected_server_port):
    # Main program
    print("Loading data...")

    cls()
    logo_popup()
    print(selected_server_ip)
    print("——————————————————————————Main Menu———————————————————————————————————————————————————")


main()
