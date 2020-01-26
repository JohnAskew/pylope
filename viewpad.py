import tkinter as tk
import os    
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
try:
    from pylope_parameters import *
except ModuleNotFoundError:
    raise ModuleNotFoundError ('Missing pylope_parameters file. Unable to pass parameters between programs')


# if len(sys.argv) > 1:
#     file_2_open = sys.argv[1]
if p_file:
    file_2_open = p_file
else:
    file_2_open = None

idx_table = []
curr_ptr = 0.0
curr_search  = ""
prev_search = ""


class Viewpad: 

    __root = Tk() 

    # default window width and height
    __thisLineWidth = 6 
    __thisWidth = 1200
    __thisHeight = 600
    __thisLineArea = Text(__root)
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
    
    # To add scrollbar 
    __thisScrollBar = Scrollbar(__thisTextArea)
    if file_2_open:
        __file = file_2_open
    else:  
        __file = None

    def __init__(self,**kwargs): 
        self.__file = file_2_open
        # Set icon 
        try: 
            self.__root.wm_iconbitmap("./py.ico") 
        except: 
            pass

        # Set window size (the default is 300x300) 

        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass

        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass

        # Set the window text 
 

        # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
    
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2) 
        
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2) 
        
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                            self.__thisHeight, 
                                            left, top)) 




        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1)
        

        # Add controls (widget)

        self.__thisTextArea.grid(sticky = N + E + S + W, column = 0) 

        self.__root.title("PYLope ViewPad") 
        
        
        # To open new file 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)  
        
        self.__thisMenuBar.add_command(label = "Press ME!",
                                       command = self.__openFile)
        # To open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
        
        # To save current file 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)     

        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                      
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                    menu=self.__thisFileMenu)    
        
        # To give a feature of cut 
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)          
    
        # to give a feature of copy  
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)         
        
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)        
        
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                    menu=self.__thisEditMenu)    
        
        # To create a feature of description of the viewpad 
        self.__thisHelpMenu.add_command(label="About Viewpad", 
                                        command=self.__showAbout) 

        self.__thisMenuBar.add_cascade(label="Help", 
                                    menu=self.__thisHelpMenu) 

        self.__root.config(menu=self.__thisMenuBar) 


        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
        
        # Scrollbar will adjust automatically according to the content       
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)   
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
            
        
    def __quitApplication(self): 
        self.__root.destroy() 
        # exit() 

    def __showAbout(self): 
        showinfo("Viewpad","John Askew ripped https://www.geeksforgeeks.org/make-notepad-using-tkinter/") 

    def __openFile(self): 
        if file_2_open:
            self.__file = file_2_open
            askopenfilename(defaultextension=".txt", 
                            initialfile = file_2_open,
                            initialdir=os.getcwd(),
                            filetypes=[("All Files","*.*"),
                                       ("Logs", "*.log *.1 *.2 *.3 *.4 *.5 *.6 *.7 *.8 *.9"),
                                       ("Text Documents","*.txt")]) 
        else:
            self.__file = askopenfilename(defaultextension=".txt", 
                                          initialdir=sys.path[0],
                                          filetypes=[("All Files","*.*"),
                                          ("Logs", "*.log *.1 *.2 *.3 *.4 *.5 *.6 *.7 *.8 *.9"),
                                           ("Text Documents","*.txt")]) 

        if self.__file == "": 
            
            # no file to open 
            self.__file = None
        else: 
            
            # Try to open the file 
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - ViewPad") 
            self.__thisTextArea.delete(1.0,END) 

            file = open(self.__file,"r") 
            num = 1.0
            line = file.readline()
            while line:
                #self.__thisTextArea.insert(num, (str(int(num)) + "| " + line))
                self.__thisTextArea.insert(num, "[" + (str(int(num)) + "] "))
                self.__thisTextArea.insert(END, line)
                num +=1.0
                line = file.readline()
            file.close() 

        
    def __newFile(self): 
        self.__root.title("ViewPad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 

    def __saveFile(self): 

        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 

            if self.__file == "": 
                self.__file = None
            else: 
                
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Viewpad") 
                
            
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 

    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 

    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 

    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>") 

    

    def run(self): 

        # Run main application 
        self.__root.mainloop() 

#-------------------------------------#
def get_idx_table(s,idx_table = []):
#-------------------------------------#

    idx_table = []
    cnt = 1
    idx = '1.0'
    while 1:
            idx = viewpad._Viewpad__thisTextArea.search(s, idx, nocase=1, stopindex=END)
            if not idx: break
            idx_table.append(float(idx))
            lastidx = '%s+%dc' % (idx, len(s))
            idx = lastidx
    return idx_table

#-------------------------------------#
def find():
#-------------------------------------#
    viewpad._Viewpad__thisTextArea.tag_delete('found')#, '1.0', END)
    viewpad._Viewpad__thisTextArea.tag_delete("highlight")#, '1.0', END)
    s = edit.get()
    if s:
        cnt = 1
        idx = '1.0'
        global idx_table
        idx_table = []
        idx_table = get_idx_table(s)
        if len(idx_table) > 0:
            for idx in idx_table:
                cnt += 1
                lastidx = '%s+%dc' % (idx, len(s))
                viewpad._Viewpad__thisTextArea.tag_add('found', idx, lastidx)
                idx = lastidx
                viewpad._Viewpad__thisTextArea.see(idx_table[0])
                global curr_ptr
                curr_ptr = idx_table[0]
                lastidx = '%s+%dc' % (curr_ptr, len(s))
                viewpad._Viewpad__thisTextArea.tag_add("highlight", curr_ptr, lastidx)
                viewpad._Viewpad__thisTextArea.tag_config('highlight', foreground='yellow', background='red')
        viewpad._Viewpad__thisTextArea.tag_config('found', foreground='red', background='yellow')
        
    #edit.focus_set()

#-------------------------------------#
def search():
#-------------------------------------#
    global idx_table
    if idx_table:
        s = edit.get()
        idx_len = len(idx_table)
        global curr_ptr
        curr_ptr = float(curr_ptr)
        if curr_ptr == idx_table[-1]:
            lastidx = '%s+%dc' % (curr_ptr, len(s))
            viewpad._Viewpad__thisTextArea.tag_remove("highlight", curr_ptr, lastidx)
            viewpad._Viewpad__thisTextArea.see(idx_table[0])
            curr_ptr = idx_table[0]
            lastidx = '%s+%dc' % (curr_ptr, len(s))
            viewpad._Viewpad__thisTextArea.tag_add("highlight", curr_ptr, lastidx)
            viewpad._Viewpad__thisTextArea.tag_config('highlight', foreground='yellow', background='red')
        else:
            for i in range(len(idx_table) ):#- 1 ):
                if curr_ptr == float(idx_table[i]):
                    lastidx = '%s+%dc' % (curr_ptr, len(s))
                    viewpad._Viewpad__thisTextArea.tag_remove("highlight", curr_ptr, lastidx)
                    curr_ptr = float(idx_table[i + 1])
                    viewpad._Viewpad__thisTextArea.see(idx_table[i + 1])
                    print("search: curr_ptr:", curr_ptr, "len(curr_ptr):", len(s), "s=", s)
                    lastidx = '%s+%dc' % (curr_ptr, len(s))
                    print("search: lastidx:", lastidx, "s=",s)
                    viewpad._Viewpad__thisTextArea.tag_add("highlight", curr_ptr, lastidx)
                    viewpad._Viewpad__thisTextArea.tag_config('highlight', foreground='yellow', background='red')
                    break



########################################
# M A I N   L O G I C
########################################

#--------------------------------------#
# HOUSEKEEPING
#--------------------------------------#
viewpad = Viewpad(width=1200,height=600)

idx_table = []
idx_len = 0
fram = Frame(viewpad._Viewpad__root)
Label(fram,text='Text to find:').pack(side=LEFT)
edit = Entry(fram)
if p:
    edit.delete(0, END)
    edit.insert(0, p)
edit.pack(side=LEFT, fill=BOTH, expand=1)


butt_search = Button(fram, text='Search')
butt_search.pack(side=RIGHT)
butt = Button(fram, text='<< Accept search term')
butt.pack(side=RIGHT)
butt.focus_force()
butt.config(command=find)
butt_search.config(command=search)

fram.grid(sticky=NW,padx=0,pady=0)
#--------------------------------------#
# Run main application
#--------------------------------------# 

if p_file:
    file_2_open = p_file
    __file = file_2_open
    viewpad._Viewpad__openFile()
    butt.focus_force()

viewpad.run()
