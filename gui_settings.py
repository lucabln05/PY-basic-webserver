import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Settings")
        #setting window size
        width=419
        height=203
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_108=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_108["font"] = ft
        GLabel_108["fg"] = "#333333"
        GLabel_108["justify"] = "center"
        GLabel_108["text"] = "  Version 2022.10.27 by lucabln05"
        GLabel_108.place(x=0,y=110,width=223,height=118)

        GLabel_66=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_66["font"] = ft
        GLabel_66["fg"] = "#333333"
        GLabel_66["justify"] = "center"
        GLabel_66["text"] = "Console"
        GLabel_66.place(x=310,y=460,width=118,height=40)

        GLabel_441=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_441["font"] = ft
        GLabel_441["fg"] = "#333333"
        GLabel_441["justify"] = "center"
        GLabel_441["text"] = "Hostname:"
        GLabel_441.place(x=20,y=30,width=89,height=32)

        GLineEdit_621=tk.Entry(root)
        GLineEdit_621["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_621["font"] = ft
        GLineEdit_621["fg"] = "#333333"
        GLineEdit_621["justify"] = "center"
        GLineEdit_621["text"] = "0.0.0.0"
        GLineEdit_621.place(x=130,y=30,width=182,height=34)

        GLabel_694=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_694["font"] = ft
        GLabel_694["fg"] = "#333333"
        GLabel_694["justify"] = "center"
        GLabel_694["text"] = "Port:"
        GLabel_694.place(x=10,y=70,width=99,height=52)

        GLineEdit_83=tk.Entry(root)
        GLineEdit_83["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_83["font"] = ft
        GLineEdit_83["fg"] = "#333333"
        GLineEdit_83["justify"] = "center"
        GLineEdit_83["text"] = "80"
        GLineEdit_83.place(x=130,y=80,width=181,height=34)

        output_host = GLineEdit_621.get()
        output_hostname = print(output_host)


        GButton_337=tk.Button(root)
        GButton_337["bg"] = "#4cd26b"
        ft = tkFont.Font(family='Times',size=10)
        GButton_337["font"] = ft
        GButton_337["fg"] = "#000000"
        GButton_337["justify"] = "center"
        GButton_337["text"] = "Save"
        GButton_337.place(x=320,y=160,width=70,height=25)
        GButton_337["command"] = self.GButton_337_command


        GButton_42=tk.Button(root)
        GButton_42["bg"] = "#dc6666"
        ft = tkFont.Font(family='Times',size=10)
        GButton_42["font"] = ft
        GButton_42["fg"] = "#000000"
        GButton_42["justify"] = "center"
        GButton_42["text"] = "Close"
        GButton_42["relief"] = "flat"
        GButton_42.place(x=230,y=160,width=70,height=25)
        GButton_42["command"] = output_hostname

    #save button
    def GButton_337_command(self):
        print("command")

    #close button
    def GButton_42_command(self):
        exit()



def gui_settings_window():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
