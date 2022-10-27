#this client can start a test webserver with gui and full consol output for developers
#https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842

import socket   #https://docs.python.org/3/library/socket.html
from log_creater import log_file_write

def main_webserver():
    try:
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
            #save server request in config file
            log_file_write(request)

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



