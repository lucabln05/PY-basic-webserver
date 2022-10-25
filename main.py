from wwwserver import main_webserver

def main_menu():
    print(""""
    Python Simple Webserver
    console.v.2022.10.25
    by lucabln05
    
    """)
    print('Software intended for development only, no regular security updates.')

    def main_():
        user_input = input('# ')

        if user_input == "start":
            main_webserver()
        elif user_input == 'help':
            print("""
            To start the server enter "start", then you will get the port and host. 
            Html files folder is: htdocs, main page should be named index.html, otherwise it can come to errors. 
            To set the server config (port, host) enter "config"
            Enter "close" to stop the software
            
            """)

            main_()
        elif user_input == 'config':
            try:
                # configurate webserver host and port and save it in config file
                webserver_host =  input("Hostname: ")
                webserver_port = input("Hostport: ")
                nl = "\n"
                lines = webserver_host, nl, webserver_port
                with open('config/config.txt', 'r+') as server_config_add:
                    server_config_add.writelines(lines)
                    server_config_add.close()
                print("New Server data saved ")
                main_()
            except Exception as err:
                print(err)
                main_()
        elif user_input == 'close':
            exit()
        else:
            print("Unknown command")
            main_()
    main_()



main_menu()
