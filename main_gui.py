import tkinter as tk
import tkinter.font as tkFont
from wwwserver import main_webserver
from serverconfig import main_config
import threading            #https://docs.python.org/3/library/threading.html

class App:
    def __init__(self, root):
        #setting title
        root.title("Python Simple Webserver")
        #setting window size
        width=504
        height=213
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_321=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_321["font"] = ft
        GLabel_321["fg"] = "#333333"
        GLabel_321["justify"] = "center"
        GLabel_321["text"] = "Simple Webserver GUI"
        GLabel_321.place(x=20,y=0,width=339,height=77)

        GLabel_108=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_108["font"] = ft
        GLabel_108["fg"] = "#333333"
        GLabel_108["justify"] = "center"
        GLabel_108["text"] = "Version 2022.10.27 by lucabln05"
        GLabel_108.place(x=0,y=120,width=223,height=118)



        #Start button
        GLabel_320=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_320["font"] = ft
        GLabel_320["fg"] = "#5fb878"
        GLabel_320["justify"] = "center"
        GLabel_320["text"] = "Start Webserver"
        GLabel_320.place(x=10,y=80,width=232,height=67)
        #CLick function
        GLabel_320.bind("<Button>", start_action)


        GLabel_94=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_94["font"] = ft
        GLabel_94["fg"] = "#333333"
        GLabel_94["justify"] = "center"
        GLabel_94["text"] = "Settings (Console)"
        GLabel_94.place(x=250,y=150,width=302,height=52)
        #CLick function
        GLabel_94.bind("<Button>", settings_action)

def main_gui_start():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


#Threding used that you can use console and GUI at the same time
def start_action(event):
    try:
        threading.Thread(target=main_webserver).start()
    except Exception as err:
        print(err)

#start the config script
def settings_action(event):
    threading.Thread(target=main_config()).start()
