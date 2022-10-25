

def main_config():
    try:
    # configurate webserver host and port and save it in config file

        webserver_host = input("Hostname: ")
        webserver_port = input("Hostport: ")
        nl = "\n"
        lines = webserver_host, nl, webserver_port
        with open('config/config.txt', 'r+') as server_config_add:
            server_config_add.writelines(lines)
            server_config_add.close()
        print("New Server data saved ")



    except Exception as err:
        print(err)
