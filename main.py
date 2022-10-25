from wwwserver import main_webserver       #Import server start script
import threading            #https://docs.python.org/3/library/threading.html
from serverconfig import main_config        #Import config change script
from main_gui import main_gui_start         #Import gui script



def main_menu():
    print(""""
    Python Simple Webserver
    console.v.2022.10.27
    by lucabln05
    
    """)
    print('Software intended for development only, no regular security updates.')

    def main_loop():
        user_input = input('# ')

        if user_input == "start":
            main_webserver()
        elif user_input == 'help':
            print("""
            To start the server enter "start", then you will get the port and host. 
            Html files folder is: htdocs, main page should be named index.html, otherwise it can come to errors. 
            To set the server config (port, host) enter "config"
            Enter "close" to stop the software
            
            !BETA!
            Type 'gui' to start the gui mode
            
            """)

            main_loop()
        elif user_input == 'config':
            main_config()
            main_loop()
        elif user_input == 'gui':
            threading.Thread(target=main_gui_start).start()
        elif user_input == 'close':
            exit()
        else:
            print("Unknown command")
            main_loop()
    main_loop()



threading.Thread(target=main_menu).start()
