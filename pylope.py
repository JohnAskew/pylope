import os
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

#-----------------
sysarg_len = 4 #Number of arguments I can pass
#-----------------
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
            x = "Searching >> " + p
            mf.mySubmitButton1.config(text = x)
            b_gz.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')
            b_dir.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')
            b_rs.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')

    #--------------------------------------#
    def set_callback(self, a_func):
    #--------------------------------------#
        self.callback = a_func


#======================================#
class MyFrame(tk.Frame):
#======================================#
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack()
        self.myLabel1 = tk.Label(parent, fg='DARKRED',bg='YELLOW', text='Python Log Toolkit: Open, Parse & Extract utility',font='Arial 10 bold')
        self.myLabel1.pack()
        self.mySubmitButton1 = tk.Button(parent, anchor=N, fg='BLUE',bg='LIGHTGREEN',relief=RAISED, text='Click to ENTER a search string', command=self.get_group_name)
        separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
        separator.pack(fill=X, padx=5, pady=5)
        self.mySubmitButton1.pack()
        self.var_case = IntVar()
        self.var_whole = IntVar()
        self.var_clear = IntVar()
        global c
        self.c = Checkbutton(root, text="Any Case", variable=self.var_case, command=self.cb_case, activebackground = 'GREEN',state=DISABLED)
        self.c.config(relief=GROOVE, bd=5, bg='LIGHTGREEN', fg='DARKBLUE', selectcolor='WHITE', width=10, height=-1)
        self.c.pack(side=TOP, padx=5, pady=5)
        self.d = Checkbutton(root, text="Whole word", variable=self.var_whole, command=self.cb_whole, activebackground = 'GREEN',state=DISABLED)
        self.d.config(relief=GROOVE, bd=5, bg='LIGHTGREEN', fg='DARKBLUE', selectcolor='WHITE', width=10, height=-1)
        self.d.pack(side=TOP, padx=5, pady=5)
        self.e = Checkbutton(root, text="Clear search; Just list contents", variable=self.var_clear, command=self.cb_clear, activebackground = 'GREEN')
        self.e.config(relief=GROOVE, bd=5, bg='LIGHTGREEN', fg='DARKBLUE', selectcolor='WHITE', width=25, height=0)
        self.e.pack( padx=5, pady=5,side=TOP)
        


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
        print("cb_whole: type", type(p_whole), "p_whole:", p_whole)

#--------------------------------------#
    def cb_clear(self):
#--------------------------------------#
        global p_clear, p_case, p
        p_clear = self.var_clear.get()
        if p_clear == 1:
            p = " "
            p_case = 0
            b_gz.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')
            b_dir.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')
            b_rs.config(state=DISABLED)
            mf.mySubmitButton1.config(fg='BLUE',bg='LIGHTGREEN',relief=RAISED, text='Click to ENTER a search string')

        if  (p == None or p == " ") and p_clear == 0:
            b_gz.config(state=DISABLED, bg='LIGHTGRAY', fg='BLACK')
            b_dir.config(state=DISABLED, bg='LIGHTGRAY', fg='BLACK')
  
#--------------------------------------#
    def get_group_name(self):
#--------------------------------------#
        mw = MainWindow(None)

        # provide callback to MainWindow so that it can return results to MyFrame
        mw.set_callback(self.set_label)
        self.c.config(state=NORMAL)
        self.d.config(state=NORMAL)


#--------------------------------------#
    def set_label(self, astr = ''):
#--------------------------------------#
        self.myLabel1['text'] = astr

#======================================#
# End Class
#======================================#

#--------------------------------------#
def call_subr_search():
#--------------------------------------#
    subprocess.call(["python", dir_path + "/" + "subr_call_search.py",  p, str(p_case), str(p_whole), str(p_clear), str(call), str(p_recur_search) , str(p_file)])

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
    dir = os.path.dirname(file) # get directory where file is stored
    filename = os.path.basename(file) # get filename
    
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
            call_subr_search()

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
                    call_subr_search()
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
        call_subr_search()
    #DEBUG else:
        #DEBUG print("extract_tar bypassing call_subr_search with call:", call)

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
    b_gz.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE', text='Open, extract and search single tar.gz', font='TkDefaultFont')
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
        call_subr_search()
    b_dir.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE', text='Open and search single directory containing logs', font='TkDefaultFont')

#--------------------------------------#
def main_logic_xp():
#--------------------------------------#
    b_xp.configure(bg='RED', fg='WHITE', text='Currently Extracting >> ALL << gz', font='Arial 8 bold')

    f = class_main_logic_for_file_and_dir.get_directory()
    if os.path.exists(f):
        os.chdir(f)
        for dirName, subdirList, fileList in os.walk(f):
            #print('Found directory %s ' % dirName)
            for fname in fileList:
                if fname.endswith("gz"):
                    print("xploding {} gz file: {}".format(dirName, fname))
                    b_xp.configure(bg='RED', fg='WHITE', text="exploding {} gz file: {}".format(dirName, fname), font='Arial 8 bold')
                    curr_dir = os.getcwd()
                    os.chdir(dirName)
                    call = 0
                    process_tar_gz(fname, call)

                    os.chdir(curr_dir)
    b_xp.configure(text='Extract >> ALL << gz in Directory', font='TkDefaultFont', bg='LIGHTGREEN', fg='DARKRED')

#--------------------------------------#
def main_logic_xpg():
#--------------------------------------#
    b_xpg.configure(bg='RED', fg='WHITE', text='Currently Extracting >> ALL << in tar.gz', font='Arial 8 bold')
    f = class_main_logic_for_file_and_dir.get_file()
    
    directory = os.path.split(f)[0]
    
    try:
        os.chdir(directory)
        extract_gz(f)
    except:
        print("PYlope function: main_logic_xpg unable to change directory", directory)
    
    for dirName, subdirList, fileList in os.walk(os.getcwd()):
            #print('Found directory %s ' % dirName)
        for fname in fileList:
            if fname.endswith("gz"):
                print("expanding {} gz file: {}".format(dirName, fname))
                b_xpg.configure(bg='RED', fg='WHITE', text="exploding {} gz file: {}".format(dirName, fname), font='Arial 8 bold')
                curr_dir = os.getcwd()
                os.chdir(dirName)
                call = 0
                process_tar_gz(fname, call)
                os.chdir(curr_dir)
    b_xpg.configure(text='Extract >> ALL << in tar.gz', font='TkDefaultFont', bg='LIGHTGREEN', fg='DARKRED')

#--------------------------------------#
def main_logic_recur_search():
#--------------------------------------#
    b_rs.configure(bg='RED', fg='WHITE', text='Recursively searching directories for search string', font='Arial 8 bold')
    directory = class_main_logic_for_file_and_dir.get_directory()
    if os.path.exists(directory):
        try:
            os.chdir(directory)
        except:
            print("PYLope error in main_logic_recur_search. Unable to change to directory:", directory)

    b_rs.config(bg='LIGHTGREEN', fg='BLUE', text = 'Recursively search a directory for a search string', font='TkDefaultFont')

#####################################
# M A I N   L O G I C
#####################################

mf = MyFrame(root)
b_dir = tkinter.Button(root,state=DISABLED, text='Open and search single directory containing logs', command=main_logic_directory)
b_gz = tkinter.Button(root, state=DISABLED, text='Open, extract and search single tar.gz', command=main_logic_tar_gz)
b_rs = tkinter.Button(root, state=DISABLED, text = 'Recursively search a directory for a search string', command=main_logic_recur_search)
b_xp = tkinter.Button(root, text='Recursively extract >> ALL << within a Directory', command=main_logic_xp, bg='LIGHTGREEN', fg='DARKRED')
b_xpg = tkinter.Button(root, text='Recursively extract all tar.gz children within a tar.gz file', command=main_logic_xpg, bg='LIGHTGREEN', fg='DARKRED')
separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
separator.pack(fill=X, padx=5, pady=5)
ttk.Label(root, text='Search Utilities for Singleton Directory or GZIP File ',font='Arial 8 bold', background='YELLOW', foreground='DARKRED').pack()
ttk.Separator(root,orient=HORIZONTAL).pack(fill=X)
b_dir.pack(fill='x')
b_gz.pack(fill='x')

separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
separator.pack(fill=X, padx=5, pady=5)
ttk.Label(root, text='Heavy Lifting Utilities (Click and go for coffee)',font='Arial 8 bold', background='DARKRED', foreground='BEIGE').pack()
ttk.Separator(root,orient=HORIZONTAL).pack(fill=X)
b_rs.pack(fill=X)
b_xp.pack(fill='x')
b_xpg.pack(fill = X)
root.mainloop()