# https://visualtk.com/

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Python Webserver Version 2022.10 by lucabln05")
        #setting window size
        width=615
        height=525
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
        GLabel_108["text"] = "Version 2022.10 by lucabln05"
        GLabel_108.place(x=20,y=420,width=214,height=112)

        GLabel_94=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_94["font"] = ft
        GLabel_94["fg"] = "#333333"
        GLabel_94["justify"] = "center"
        GLabel_94["text"] = "Settings"
        GLabel_94.place(x=440,y=460,width=95,height=41)

        GLabel_320=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_320["font"] = ft
        GLabel_320["fg"] = "#5fb878"
        GLabel_320["justify"] = "center"
        GLabel_320["text"] = "Start Webserver"
        GLabel_320.place(x=20,y=380,width=224,height=39)

        GLabel_63=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_63["font"] = ft
        GLabel_63["fg"] = "#cc0000"
        GLabel_63["justify"] = "center"
        GLabel_63["text"] = "Stop Webserver"
        GLabel_63.place(x=230,y=380,width=275,height=43)

        GLabel_66=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_66["font"] = ft
        GLabel_66["fg"] = "#333333"
        GLabel_66["justify"] = "center"
        GLabel_66["text"] = "Console"
        GLabel_66.place(x=330,y=460,width=118,height=40)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
