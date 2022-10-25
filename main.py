from wwwserver import main_webserver
from threading import Thread        #https://stackoverflow.com/questions/2957116/make-2-functions-run-at-the-same-time
from serverconfig import main_config

def main_menu():
    print(""""
    Python Simple Webserver
    console.v.2022.10.25
    by lucabln05
    
    """)
    print('Software intended for development only, no regular security updates.')

    def main_loop():
        user_input = input('# ')

        if user_input == "start":
            Thread(target=main_webserver).start()
        elif user_input == 'help':
            print("""
            To start the server enter "start", then you will get the port and host. 
            Html files folder is: htdocs, main page should be named index.html, otherwise it can come to errors. 
            To set the server config (port, host) enter "config"
            Enter "close" to stop the software
            
            """)

            main_loop()
        elif user_input == 'config':
            main_config()
            main_loop()
        elif user_input == 'close':
            exit()
        else:
            print("Unknown command")
            main_loop()
    main_loop()



Thread( target=main_menu ).start()
