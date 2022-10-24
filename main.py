#this client can start a test webserver with gui and full consol output for developers
#https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842

import socket   #https://docs.python.org/3/library/socket.html


def main_webserver():
    try
        # define the host and port for the webserver by reading config file
        server_config = open('config/config.txt','r+')

        server_host = server_config.readline().rstrip("\r\n")
        server_port = int(server_config.readline().rstrip("\r\n"))  #int that the webserver dont have an error
        server_config.close()
    except Exception as err:
        print(err)
    try:
        #configurate webserver
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #AF_INET (IPv4 address family) and SOCK_STREAM (TCP, basically)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((server_host, server_port))      #set hostname and port
        server_socket.listen(1)
        print(f'Webserver start on {server_host}:{server_port}')

        #process userquestions over http
        while True:
            # accept client user and wait for connection
            client_connection, client_address = server_socket.accept()

            # read and show information from user client
            request = client_connection.recv(1024).decode()
            print(request)


            # Read user request on with underside the user want to go localhost/-->main.html<--
            headers = request.split('\n')
            request_file = headers[0].split()[1]

            # request only / go on main file
            if request_file == '/':
                request_file = '/index.html'

            try:
                # read content from .html file
                html_file = open('htdocs' + request_file)
                file_content = html_file.read()
                html_file.close()
            except Exception as err:
                print(err)


            try:
                # content from the website
                response = 'HTTP/5.0 200 OK\n\n' + file_content
            except Exception as err:
                response = f"HTTP/5.0 404 OK\n\nInternal error: {err}. --> Contact your admin. Check Console Output"
                print(err)

            # send html data to requestet user
            client_connection.sendall(response.encode())
            client_connection.close()

        server_socket.close()

    except Exception as err:
        print(err)




def main_menu():
    print(""""
    Python Simple Webserver
    console.v.2022.10.24
    by lucabln05
    
    """)
    print('Software intended for development only, no regular security updates.')

    def main_():
        user_input = input('# ')

        if user_input == "start":
            main_webserver()
        elif user_input == 'help':
            print("""
            To start the server enter start, then you will get the port and host. 
            Html files folder is: htdocs, main page should be named index.html, otherwise it can come to errors. 
            
            """)
            main_()
        elif user_input == 'config':
            try:
                # configurate webserver host and port and save it in config file
                webserver_host =  input("Hostname: ")
                webserver_port = input("Hostport: ")
                nl = "\n"
                lines = webserver_host, nl, webserver_port
                with open('config/config.txt', 'r+') as mysql_login:
                    mysql_login.writelines(lines)
                    mysql_login.close()  # schliesst datei wieder
                print("New Server data saved ")
                main_()
            except Exception as err:
                print(err)
                main_()
    main_()


main_menu()