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


    def set_callback(self, a_func):
        self.callback = a_func


#--------------------------------------#
class MyFrame(tk.Frame):
#--------------------------------------#
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack()
        self.myLabel1 = tk.Label(parent, fg='DARKRED',bg='YELLOW', text='Python Log Open, Parse & Extract utility (PYlope)')
        self.myLabel1.pack()
        self.mySubmitButton1 = tk.Button(parent, anchor=W, fg='BLUE',bg='LIGHTGREEN',relief=RAISED, text='Click to ENTER a search string', command=self.get_group_name)
        separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
        separator.pack(fill=X, padx=5, pady=5)
        self.mySubmitButton1.pack()
        self.var_case = IntVar()
        self.var_whole = IntVar()
        self.var_clear = IntVar()
        c = Checkbutton(root, text="Any Case", variable=self.var_case, command=self.cb_case, activebackground = 'GREEN')
        c.config(relief=GROOVE, bd=5, bg='LIGHTGREEN', fg='DARKBLUE', selectcolor='WHITE', width=10, height=-1)
        c.pack(side=LEFT, padx=5, pady=5)
        e = Checkbutton(root, text="Bypass search", variable=self.var_clear, command=self.cb_clear, activebackground = 'GREEN')
        e.config(relief=GROOVE, bd=5, bg='LIGHTGREEN', fg='DARKBLUE', selectcolor='WHITE', width=10, height=0)
        e.pack( padx=5, pady=5,side=RIGHT)
        


#--------------------------------------#
    def cb_case(self): 
#--------------------------------------#
        global p_case
        p_case = self.var_case.get()

#--------------------------------------#
    def cb_whole(self):
#--------------------------------------#
        global p_whole
        p_whole = self.var_whole.get()

#--------------------------------------#
    def cb_clear(self):
#--------------------------------------#
        global p_clear
        p_clear = self.var_clear.get()
        if p_clear == 1:
            p = " "
            p_case = 0
  
#--------------------------------------#
    def get_group_name(self):
#--------------------------------------#
        mw = MainWindow(None)

        # provide callback to MainWindow so that it can return results to MyFrame
        mw.set_callback(self.set_label)


#--------------------------------------#
    def set_label(self, astr = ''):
#--------------------------------------#
        self.myLabel1['text'] = astr

#--------------------------------------#
def call_subr_search():
#--------------------------------------#

 
    if p_clear == 1:
        subprocess.call(["python", dir_path + "/" + "subr_search.py"])
    elif (p > " ") & (p_case == 1) & (p_whole == 1):
        subprocess.call(["python", dir_path + "/" + "subr_search.py", p, str(p_case), str(p_whole)])
    elif (p > " ") & (p_case == 1):
        subprocess.call(["python", dir_path + "/" + "subr_search.py", p, str(p_case)])
    elif p > " ":
       subprocess.call(["python", dir_path + "/" + "subr_search.py", p])
    else:
        subprocess.call(["python", dir_path + "/" + "subr_search.py"])
#--------------------------------------#
def extract_gz(file):
#--------------------------------------#
    dir = os.path.dirname(file) # get directory where file is stored
    
    filename = os.path.basename(file) # get filename
    
    file_tar, file_tar_ext = os.path.splitext(file) # split into file.tar and .gz
    
    file_untar, file_untar_ext = os.path.splitext(file_tar) #split into file and .tar
    
    os.chdir(dir)

    if file_tar_ext == ".gz" and file_untar_ext == ".tar":
        if not os.path.exists(file_untar):
            os.mkdir(file_untar) 
        tar = tarfile.open(filename)

        for i in tar.getmembers():
            try:
                tar.extract(i, path=file_untar)
                
            except:
                print("Unable to extract:", i)
        tar.close()
        
        os.chdir(file_untar)
        
        call_subr_search()
#--------------------------------------#
def extract_tgz(f):
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
        
                call_subr_search()
    tar.close()
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

    if (f.endswith("tgz")):
        directory = os.path.split(f)[0]
        os.chdir(directory)
        extract_tgz(f)
 
    if (f.endswith("gz")):
        directory = os.path.split(f)[0]
        tail = os.path.split(f)[1]
        os.chdir(directory)
        extract_gz(f)
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


#####################################
# M A I N   L O G I C
#####################################

mf = MyFrame(root)
b_dir = tkinter.Button(root, text='Open Directory to search', command=main_logic_directory)
b_gz = tkinter.Button(root, text='Open & Extract tar.gz to search', command=main_logic_tar_gz)
    


separator = Frame(height=5, bd=10, bg='WHITE',relief=RAISED)
separator.pack(fill=X, padx=5, pady=5)

b_dir.pack(fill='x')
b_gz.pack(fill='x')


root.mainloop()