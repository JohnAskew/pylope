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


#-----------------
sysarg_len = 4 #Number of arguments I can pass
#-----------------
user = getpass.getuser()
root = tkinter.Tk()
dir_path = os.path.dirname(os.path.realpath(__file__))
p = " " #Default placeholder = poor programmming, that's why
p_case = 0 #Default placeholder - again, poor programming, that's why
p_whole = 0 #Default placeholder
p_clear = 0
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
        b_gz.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')
        b_dir.config(state=NORMAL, bg='LIGHTGREEN', fg='BLUE')
        if len(p) > 0:
            x = "Searching >> " + p
            mf.mySubmitButton1.config(text = x)

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
        self.myLabel1 = tk.Label(parent, fg='DARKRED',bg='YELLOW', text='Python Log Open, Parse & Extract utility (PYlope)')
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
    subprocess.call(["python", dir_path + "/" + "subr_call_search.py",  p, str(p_case), str(p_whole), str(p_clear) ])

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
    #os.chdir(dir)
    filename = os.path.basename(file) # get filename
    
    file_tar, file_tar_ext = os.path.splitext(file) # split into file.tar and .gz
    
    file_untar, file_untar_ext = os.path.splitext(file_tar) #split into file and .tar
    
    #os.chdir(dir)

    if file_tar_ext == ".gz" and file_untar_ext == ".tar":
        if not os.path.exists(file_untar):
            os.mkdir(file_untar) 

        tar = tarfile.open(filename)

        for i in tar.getmembers():
            try:
                tar.extract(i, path=file_untar)

            except:
                print("Unable to extract:", i ,"to:", file_untar, "The current directory is:", os.getcwd())
        tar.close()
     
        os.chdir(file_untar)
        if call:
            call_subr_search()
        #DEBUG else:
            #DEBUG print("extract_gz bypassing call_subr_search with call", call)
#--------------------------------------#
def extract_tgz(f, call =  1):
#--------------------------------------#
    #DEBUG print("entering extract_tgz with call:", call)
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
                #DEBUG else:
                    #DEBUG print("extract_tgz bypassing call_subr_search with call:", call)
    tar.close()
#--------------------------------------#
def extract_tar(file, call = 1):
#--------------------------------------#
    #DEBUG print("entering extract_tar with call:", call)
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
    f = tkinter.filedialog.askopenfilename(

        parent=root, initialdir='C:\\Users\\%s\\Downloads' % user,

        title='Choose file',

        filetypes=[('tar zip', '.tar.gz .tgz'),
                   ('tar', '.tar'),
                   ('gunzip', '.gz'),
                   ('7zip', '.7z')]

        )
    directory = os.path.split(f)[0]

    try:
        os.chdir(directory)
        process_tar_gz(f)
    except:
        print("PYlope function: main_logic_tar_gz unable to change directory", directory)
    
#--------------------------------------#
def main_logic_directory():
#--------------------------------------#

    f = tkinter.filedialog.askdirectory(

        parent=root, initialdir='C:\\Users\\%s\\Downloads' % user,

        title='Choose directory'

        )
    if os.path.exists(f):
        os.chdir(f)
        call_subr_search()

#--------------------------------------#
def main_logic_xp():
#--------------------------------------#
    b_xp.configure(bg='RED', fg='WHITE', text='Currently Extracting >> ALL << gz', font='Arial 8 bold')
    f = tkinter.filedialog.askdirectory(

        parent=root, initialdir='C:\\Users\\%s\\Downloads' % user,

        title='Choose directory'

        )
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
                    #DEBUG print("main_logic_xp calling process_tar_gz with call:", call)
                    process_tar_gz(fname, call)

                    os.chdir(curr_dir)
    b_xp.configure(text='Extract >> ALL << gz in Directory', bg='LIGHTGRAY', fg='BLACK', font='TkDefaultFont')

#--------------------------------------#
def main_logic_xpg():
#--------------------------------------#
    b_xpg.configure(bg='RED', fg='WHITE', text='Currently Extracting >> ALL << in tar.gz', font='Arial 8 bold')

    f = tkinter.filedialog.askopenfilename(

        parent=root, initialdir='C:\\Users\\%s\\Downloads' % user,

        title='Choose file',

        filetypes=[('tar zip', '.tar.gz .tgz'),
                   ('tar', '.tar'),
                   ('gunzip', '.gz'),
                   ('7zip', '.7z')]

        )
    directory = os.path.split(f)[0]
    print("main_logic_xpg before call with directory:", directory, "file:", f)
    try:
        os.chdir(directory)
        process_tar_gz(f)
    except:
        print("PYlope function: main_logic_xpg unable to change directory", directory)
    print("main_logic_xpg using directory:", directory, "for Treewalk of main_logic_xp")
    if os.path.exists(directory):
        os.chdir(directory)
        for dirName, subdirList, fileList in os.walk(directory):
            #print('Found directory %s ' % dirName)
            for fname in fileList:
                if fname.endswith("gz"):
                    print("xploding {} gz file: {}".format(dirName, fname))
                    b_xpg.configure(bg='RED', fg='WHITE', text="exploding {} gz file: {}".format(dirName, fname), font='Arial 8 bold')
                    curr_dir = os.getcwd()
                    os.chdir(dirName)
                    call = 0
                    #DEBUG print("main_logic_xp calling process_tar_gz with call:", call)
                    process_tar_gz(fname, call)

                    os.chdir(curr_dir)
    b_xpg.configure(text='Extract >> ALL << in tar.gz', bg='LIGHTGRAY', fg='BLACK', font='TkDefaultFont')

#####################################
# M A I N   L O G I C
#####################################

mf = MyFrame(root)
b_dir = tkinter.Button(root, state=DISABLED, text='Open Directory to search', command=main_logic_directory)
b_gz = tkinter.Button(root, state=DISABLED, text='Open & Extract tar.gz to search', command=main_logic_tar_gz)
b_xp = tkinter.Button(root,  text='Extract >> ALL << gz in Directory', command=main_logic_xp, bg='LIGHTGRAY')
b_xpg = tkinter.Button(root,  text='Extract >> ALL << tar.gz', command=main_logic_xpg, bg='LIGHTGRAY')
separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
separator.pack(fill=X, padx=5, pady=5)
ttk.Label(root, text='Search Utilities').pack()
ttk.Separator(root,orient=HORIZONTAL).pack(fill=X)
b_dir.pack(fill='x')
b_gz.pack(fill='x')
separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
separator.pack(fill=X, padx=5, pady=5)
ttk.Label(root, text='Extract Utilities').pack()
ttk.Separator(root,orient=HORIZONTAL).pack(fill=X)
b_xp.pack(fill='x')
b_xpg.pack(fill = X)
root.mainloop()