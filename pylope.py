import os

try:

    import platform

except:

    os.system('pip install platform')

    import platform

try:

    from datetime import datetime

except:

    os.system('pip install datetime')

    from datetime import datetime

try:

    import gzip

except:

    os.system('pip install gzip')

    import gzip

try:

    import tkinter as tk

    from tkinter import *

    import tkinter.filedialog

except:

    os.system('pip install tkinter')

    import tkinter as tk

    from tkinter import *

    import tkinter.filedialog

from tkinter import ttk

try:

    import tarfile

except:

    os.system('pip install tarfile')

    import tarfile

try:

    import getpass

except:

    os.system('pip install getpass')

    import getpass

try:

    import subprocess

except:

    os.system("pip install subprocess")

    import subprocess

try:

    from pylope_parameters import *

except ModuleNotFoundError:

    raise ModuleNotFoundError ('Missing pylope_parameters file. Unable to pass parameters between programs')

user = getpass.getuser()

root = tkinter.Tk()

dir_path = os.path.dirname(os.path.realpath(__file__))


#======================================#
class class_main_logic_for_file_and_dir:
#======================================#
#--------------------------------------#
    def __init__(self):
#--------------------------------------#
        pass
#--------------------------------------#
    def get_file():
#--------------------------------------#
        f = tkinter.filedialog.askopenfilename(

        parent=root, initialdir='C:\\Users\\%s\\Downloads' % user,

        title='Choose file',

        filetypes=[('tar zip', '.tar.gz .tgz'),
                   ('tar', '.tar'),
                   ('gunzip', '.gz'),
                   ('7zip', '.7z')]

        )

        return f
#--------------------------------------#
    def get_directory():
#--------------------------------------#
        f = tk.filedialog.askdirectory(

            parent=root, initialdir='C:\\Users\\%s\\Downloads' % user,

            title='Choose directory'

            )
        return f

#======================================#
# End Class
#======================================#

#======================================#
class MainWindow():
#======================================#
    def __init__(self, parent):

        top = self.top = tk.Toplevel(parent)

        self.myLabel = tk.Label(top, text='Click OK to enter search string')

        self.myLabel.pack()

        self.myEntryBox = tk.Entry(top)

        self.myEntryBox.focus_set()

        self.myEntryBox.pack()

        self.mySubmitButton = tk.Button(top, text='OK', command=self.DestWin)

        self.mySubmitButton.pack()

    #--------------------------------------#
    def DestWin(self):
    #--------------------------------------#
        # call callback function setting value in MyFrame
        global p
        
        p = self.myEntryBox.get()
        
        self.top.destroy()
        
        global p_clear
        
        p_clear = 0
        
        if len(p) > 0:
        
            x = "Searching >> " + str(p)
        
            mf.mySubmitButton1.config(text = x)
        
            if p != [] and p != " " and p != "" and p != None:
        
                b_gz.config(state=NORMAL, bg='LIGHTGREEN', fg='DARKBLUE')
        
                b_dir.config(state=NORMAL, bg='LIGHTGREEN', fg='DARKBLUE')
        
                b_rs.config(state=NORMAL, bg='LIGHTGREEN', fg='DARKBLUE')

    #--------------------------------------#
    def set_callback(self, a_func):
    #--------------------------------------#
        self.callback = a_func


#======================================#
class MyFrame(tk.Frame):
#======================================#
    def __init__(self, parent, **kwargs):
        
        super().__init__(parent, **kwargs)
        
        self.grid(row=0, column=0)
        
        self.myLabel1 = tk.Label(parent, fg='DARKBLUE',bg='LIGHTYELLOW', text='Python Log Toolkit: Open, Extract & Search utility',font='Arial 12 bold')
        
        self.myLabel1.grid(row=1,column=0, sticky=N)
        
        if platform.system() == 'Windows':

            root.wm_iconbitmap("./py.ico") 
        
        self.separator = Frame(height=15, bd=3, bg='DARKBLUE',relief=RAISED)
        
        self.separator.grid(row=2,column=0,sticky=W, ipadx=250, ipady=5)
        
        self.mySubmitButton1 = tk.Button(parent, anchor=N, bd=5, fg='DARKBLUE',bg='LIGHTGREEN',relief=RAISED, text='Click to ENTER a search string', command=self.get_group_name ,font='TkDefaultFont 11 bold')
        
        self.mySubmitButton1.grid(row=5, padx=5, pady=5)
        
        separator = Frame(height=5, bd=10, bg='DARKBLUE',relief=RAISED)
        
        separator.grid(row=7,ipadx=250,ipady=5,sticky=N,padx=5, pady=1)
        
        self.var_case = IntVar()
        
        self.var_whole = IntVar()
 
        self.var_clear = IntVar()
 
        global c
 
        self.c = Checkbutton(root, text="Any Case", variable=self.var_case, command=self.cb_case, activebackground = 'GREEN',state=DISABLED)
 
        self.c.config(relief=GROOVE, bd=5, bg='LIGHTGRAY', fg='DARKBLUE', selectcolor='WHITE', width=10, height=-1)
 
        self.c.grid(row=6, column=0,sticky=W, padx=5, pady=5)
        
        self.e = Checkbutton(root, text="Clear search; start over", variable=self.var_clear, command=self.cb_clear, activebackground = 'GREEN')
 
        self.e.config(relief=GROOVE, bd=5, bg='LIGHTGREEN', fg='DARKBLUE', selectcolor='WHITE', width=25, height=0)
 
        self.e.grid(row=6,column=0, padx=5, pady=5,sticky=N)

        self.d = Checkbutton(root, text="Whole word", variable=self.var_whole, command=self.cb_whole, activebackground = 'GREEN',state=DISABLED)
 
        self.d.config(relief=GROOVE, bd=5, bg='LIGHTGRAY', fg='DARKBLUE', selectcolor='WHITE', width=10, height=-1)
 
        self.d.grid(row=6, column=0,sticky=E)#, padx=5, pady=5)
 
        separator = Frame(height=5, bd=10, bg='DARKBLUE',relief=RAISED)

        separator.grid(row=9,ipadx=250,ipady=5,sticky=N,padx=5, pady=1)


#--------------------------------------#
    def cb_case(self): 
#--------------------------------------#
        global p_case
        
        p_case = self.var_case.get()
        
        return p_case

#--------------------------------------#
    def cb_whole(self):
#--------------------------------------#
        global p_whole
        
        p_whole = self.var_whole.get()
       
#--------------------------------------#
    def cb_clear(self):
#--------------------------------------#
        global p_clear, p_case, p
        
        p_clear = self.var_clear.get()
        
        if p_clear == 1:
        
            p = []
        
            p_case = 0
        
            b_gz.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')
        
            b_dir.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')
        
            b_rs.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')
        
            mf.mySubmitButton1.config(fg='DARKBLUE',bg='LIGHTGREEN',relief=RAISED, text='Click to ENTER a search string')
        
            self.c.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')
        
            self.d.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')


        if  (p == [] or p == None or p == " " or p == '') and p_clear == 0:
        
            b_gz.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')
        
            b_dir.config(state=DISABLED, bg='LIGHTGRAY', fg='DARKBLUE')
  
#--------------------------------------#
    def get_group_name(self):
#--------------------------------------#
        mw = MainWindow(None)
        
        mw.set_callback(self.set_label)
        
        self.c.config(state=NORMAL, bg='LIGHTGREEN', fg='DARKBLUE')
        
#--------------------------------------#
    def set_label(self, astr = ''):
#--------------------------------------#
        self.myLabel1['text'] = astr

#======================================#
# End Class
#======================================#

#--------------------------------------#
def call_subr_search(p , p_case, p_whole, p_clear, call, p_recur_search, p_file):
#--------------------------------------#

    subprocess.call(["python", dir_path + "/" + "subr_call_search.py",  str(p), str(p_case), str(p_whole), str(p_clear), str(call), str(p_recur_search) , p_file])

#--------------------------------------#
def process_tar_gz(f, call=1):
#--------------------------------------#

    if (f.endswith("tar")):
   
        extract_tar(f, call)

    if (f.endswith("tgz")):
   
        extract_tgz(f, call)
 
    if (f.endswith("gz")):
   
        extract_gz(f, call)


#--------------------------------------#
def extract_gz(file, call = 1):
#--------------------------------------#
    print("pylope.py:extract_gz: file:", file, "call:", call)
    
    dir = os.path.dirname(file) # get directory where file is stored
    
    filename = os.path.basename(file) # get filename
    
    print("pylope.py:extract_gz: filename:", filename)
    
    file_tar, file_tar_ext = os.path.splitext(file) # split into file.tar and .gz
    
    file_untar, file_untar_ext = os.path.splitext(file_tar) #split into file and .tar
    
    if file_tar_ext == ".gz" and file_untar_ext == ".tar":
    
        if not os.path.exists(file_untar):
    
            os.mkdir(file_untar) 

        tar = tarfile.open(filename, encoding='utf-8')

        for i in tar.getmembers():
    
            try:
    
                tar.extract(i, path=file_untar)
    
            except:
    
                print("Unable to extract:", i ,"to:", file_untar)
    
        tar.close()
     
        os.chdir(file_untar)

        if call:
    
            call_subr_search(p , p_case, p_whole, p_clear, call, p_recur_search, p_file)

#--------------------------------------#
def extract_tgz(f, call =  1):
#--------------------------------------#
    tar = gzip.open(f, 'rb')
    
    tar = tarfile.open(f, "r:gz")
    
    tar.extractall()
    
    cnt = 0
    
    for filename in tar.getnames():
        
        if cnt == 0:
    
            if os.path.isdir(filename):
    
                os.chdir(filename)
    
                cnt +=1
    
                if call:
    
                    call_subr_search(p , p_case, p_whole, p_clear, call, p_recur_search, p_file)
    tar.close()
#--------------------------------------#
def extract_tar(file, call = 1):
#--------------------------------------#
    dir = os.path.dirname(file) # get directory where file is stored
    
    filename = os.path.basename(file) # get filename
    
    file_base, file_suffix = filename.split('.')
    
    file_tar, file_tar_ext = os.path.splitext(file) # split into file.tar and .gz
    
    file_untar, file_untar_ext = os.path.splitext(file_tar) #split into file and .tar
    
    os.chdir(dir)
    
    tar = tarfile.open(file, mode = 'r')
    
    for i in tar.getnames():
    
        try:
    
            if i.startswith(file_base):
    
                tar.extract(i, path=dir)
    
            else:
    
                tar.extract(i, path=file_untar)
    
        except:
    
            print("extract_tar function unable to extract", i, "...skipping on.")
    
    tar.close()
    
    os.chdir(file_untar)
    
    if call:
    
        call_subr_search(p , p_case, p_whole, p_clear, call, p_recur_search, p_file)

#--------------------------------------#
def main_logic_tar_gz():
#--------------------------------------#
    b_gz.config(state=NORMAL, bg='RED', fg='WHITE', text = 'Currently Extracting a single tar.gz',font='Arial 8 bold')

    b_dir.config(state=DISABLED)

    b_xp.config(state=DISABLED)

    b_xpg.config(state=DISABLED)

    b_rs.config(state=DISABLED)

    f = class_main_logic_for_file_and_dir.get_file()

    directory = os.path.split(f)[0]

    try:

        os.chdir(directory)

        process_tar_gz(f)

    except:

        print("PYlope function: main_logic_tar_gz unable to change directory", directory)

    b_gz.config(state=NORMAL, bg='LIGHTGREEN', fg='DARKBLUE', text='Open, extract and search single tar.gz', font='TkDefaultFont')

    b_dir.config(state=NORMAL)

    b_xp.config(state=NORMAL)

    b_xpg.config(state=NORMAL)

    b_rs.config(state=NORMAL)

#--------------------------------------#
def main_logic_directory():
#--------------------------------------#
    b_dir.config(state=NORMAL, bg='RED', fg='WHITE', text='Currently searching directory ', font='Arial 8 bold', highlightcolor='ORANGE')

    f = class_main_logic_for_file_and_dir.get_directory()
 
    if os.path.exists(f):

        os.chdir(f)

        call_subr_search(p , p_case, p_whole, p_clear, call, p_recur_search, p_file)

    b_dir.config(state=NORMAL, bg='LIGHTGREEN', fg='DARKBLUE', text='Open and search single directory containing logs', font='TkDefaultFont')

#--------------------------------------#
def main_logic_xp():
#--------------------------------------#
    b_xp.configure(bg='RED', fg='WHITE', text='Currently Extracting >> ALL << gz', font='Arial 8 bold')

    f = class_main_logic_for_file_and_dir.get_directory()

    if os.path.exists(f):

        os.chdir(f)

        for dirName, subdirList, fileList in os.walk(f):

            for fname in fileList:

                if fname.endswith("gz"):

                    print("xploding {} gz file: {}".format(dirName, fname))

                    b_xp.configure(bg='RED', fg='WHITE', text="exploding {} gz file: {}".format(dirName, fname), font='Arial 8 bold')

                    curr_dir = os.getcwd()

                    os.chdir(dirName)

                    call = 0

                    process_tar_gz(fname, call)

                    os.chdir(curr_dir)

    b_xp.configure(text='Extract >> ALL << gz in Directory', font='TkDefaultFont', bg='DARKGREEN', fg='BEIGE')

#--------------------------------------#
def main_logic_xpg():
#--------------------------------------#
    b_xpg.configure(bg='RED', fg='WHITE', text='Currently Extracting >> ALL << in tar.gz', font='Arial 8 bold')

    f = class_main_logic_for_file_and_dir.get_file()
    
    directory = os.path.split(f)[0]
    
    try:

        os.chdir(directory)

    except:

        print("PYlope function: main_logic_xpg unable to change directory", directory)

        sys.exit(0)

    try:

        extract_gz(f, call = 0)

    except:

        print("PYlope: main_logic_xpd: unable to perform extract_gz(f) using f:", f)

        sys.exit(0)
    for dirName, subdirList, fileList in os.walk(os.getcwd()):

        for fname in fileList:

            if fname.endswith("gz"):

                print("expanding {} gz file: {}".format(dirName, fname))

                b_xpg.configure(bg='RED', fg='WHITE', text="exploding {} gz file: {}".format(dirName, fname), font='Arial 8 bold')

                curr_dir = os.getcwd()

                os.chdir(dirName)

                call = 0

                process_tar_gz(fname, call)


                os.chdir(curr_dir)

    b_xpg.configure(text='Extract >> ALL << in tar.gz', font='TkDefaultFont', bg='DARKGREEN', fg='BEIGE')

#--------------------------------------#
def main_logic_recur_search(p_recur_search = 1, call=1):
#--------------------------------------#
    b_rs.configure(bg='RED', fg='WHITE', text='Recursively searching directories for search string', font='Arial 8 bold')

    directory = class_main_logic_for_file_and_dir.get_directory()

    os.chdir(directory)

    loopDirList = []

    try:
       
        for dirName, subdirList, fileList in os.walk(directory):

            if len(dirName) > 0 and len(fileList) > 0 and len(subdirList) == 0:

                loopDirList.append(dirName)

                os.chdir(dirName)

                print("New dir. to make call is", os.getcwd())

                try:

                    if call == 1:

                        call_subr_search(p , str(p_case), str(p_whole), str(p_clear), str(call), str(p_recur_search), str(p_file))

                except Exception as e:

                    print("PYLope:main_logic_recur_search: Died trying to call_subr_search().")

                    print(e)

                    sys.exit(0)


    except Exception as e:

        print("PYLope : main_logic_recur_search --> Error in parsing the directory", directory)

        print(e)

    b_rs.config(bg='LIGHTGREEN', fg='DARKBLUE', text = 'Recursively search a directory for a search string', font='TkDefaultFont')

#--------------------------------------#
def help_reatz_focus(event=None):
#--------------------------------------#
    help_reatz_focus_label.config(text="Extract\nEVERYTHING")

#--------------------------------------#
def help_reatz_unfocus(event=None):
#--------------------------------------#
    help_reatz_focus_label.config(text="")

#--------------------------------------#
def help_readtz_focus(event=None):
#--------------------------------------#
    help_reatz_focus_label.config(text="Extract all\nin directory")

#--------------------------------------#
def help_readtz_unfocus(event=None):
#--------------------------------------#
    help_reatz_focus_label.config(text="")

#####################################
# M A I N   L O G I C
#####################################

mf = MyFrame(root)

b_dir = tkinter.Button(root,state=DISABLED, text='Open and search SINGLE directory containing logs', command=main_logic_directory, width=40)

b_gz = tkinter.Button(root, state=DISABLED, text='Open, extract and search a SINGLE tar.gz', command=main_logic_tar_gz, width=40)

b_rs = tkinter.Button(root, state=DISABLED, text = 'Recursively search a directory for a search string', command=main_logic_recur_search, width=40)

b_xp = tkinter.Button(root, text='Recursively extract >> ALL Tar.GZIP Files<< within a Directory', command=main_logic_xp, bg='DARKGREEN', fg='WHITE',width=47)

b_xpg = tkinter.Button(root, text='Recursively extract ALL Tar.GZIP Children within a tar.gz file', command=main_logic_xpg, bg='DARKGREEN', fg='WHITE', width=47,highlightcolor='DARKRED')

ttk.Label(root, text='Search Utilities for Singleton Directory or GZIP File ',font='Arial 12 bold', background='LIGHTYELLOW', foreground='DARKBLUE').grid(row=8,column=0,sticky=N)

look=PhotoImage(file = r"look.png").subsample(1,1) 

ttk.Label(root, image=look,background='LIGHTGREEN').grid(row=8,column=0, sticky=W)

b_dir.grid(row=11,column=0,sticky=N)

b_gz.grid(row=12,column=0,sticky=N)

separator = Frame(height=15, bd=10, bg='DARKBLUE',relief=RAISED)

separator.grid(row=13,column=0,ipadx=250, ipady=0)

ttk.Label(root, text='Recursive Searches for Multiple Directories and GZIP Files',font='Arial 12 bold',  background='LIGHTYELLOW',foreground='DARKBLUE').grid(row=14, column=0, sticky=NE)

separator = Frame(height=15, bd=10, bg='DARKBLUE',relief=RAISED)

separator.grid(row=15,column=0,ipadx=250,ipady=0)

search=PhotoImage(file = r"search.png",).subsample(6,6) 

ttk.Label(root, image=search, background = 'LIGHTGREEN').grid(row=14,sticky=W)

b_rs.grid(row=16,column=0,sticky=N)

separator = Frame(height=15, bd=10, bg='DARKBLUE',relief=RAISED)

separator.grid(row=17,column=0,sticky=N,ipadx=250, ipady=1)

ttk.Label(root, text='Heavy Lifting Utilities (Click and go for coffee)' ,font='Arial 12 bold' , background='LIGHTYELLOW', foreground='DARKBLUE').grid(row=18,column=0,sticky=N)

coffee=PhotoImage(file = r"coffee.png").subsample(9,12) 

ttk.Label(root, image=coffee, background='LIGHTGREEN').grid(row=18,column=0,sticky=W)

separator = Frame(height=15, bd=10,bg='DARKBLUE',relief=RAISED)

separator.grid(row=19,column=0,ipadx=250,ipady=0,sticky=N)

b_xp.grid(row=20)

b_xpg.grid(row=21)

help_readtz_focus_label = tk.Label(text="", width=10, height=2)

help_readtz_focus_label.grid(row=19,column=0,rowspan=3,sticky=W)

b_xp.bind("<Enter>", help_readtz_focus)

b_xp.bind("<Leave>", help_readtz_unfocus)

help_reatz_focus_label = tk.Label(text="", width=10, height=2)

help_reatz_focus_label.grid(row=19,column=0,rowspan=3,sticky=W)

b_xpg.bind("<Enter>", help_reatz_focus)

b_xpg.bind("<Leave>", help_reatz_unfocus)

root.mainloop()