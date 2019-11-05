# name: subr_search.py
# desc: Search and list findings, pass to viewpad.py
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from os import access, R_OK
try:
    from datetime import datetime
except:
    os.system('pip install datetime')
    from datetime import datetime
try:
    import subprocess
except:
    os.system('pip install subprocess')
    import subprocess
try:
    import webbrowser
except:
    os.system('pip install webbrowser')
    import webbrowser
try:
    from pylope_parameters import *
except ModuleNotFoundError:
    raise ModuleNotFoundError ('Missing pylope_parameters file. Unable to pass parameters between programs')

#--------------------------------------#
def onselect(evt):
#--------------------------------------#
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    global index_start
    index_start = int(w.curselection()[0])
    global curr_sel
    curr_sel = w.curselection()
    value = w.get(index_start)
    global next_value
    next_value = w.get(index_start+ 1)

#--------------------------------------#
def openfile(event):
#--------------------------------------#
    global str_path
    if str_path != None:
        if os.path.isdir(str_path):
            os.chdir(str_path)
    else:
        str_path = '.'
    x = index_start
    p_file = l.get(x).split()[0]
    global p
    if p == []:
        p = ""
    else:
        p = str(p).split("+")
        p = p[0]
    try:
        subprocess.Popen(["python", dir_path + "/" + "viewpad.py",  str(p), str(p_case), str(p_whole), str(p_clear), str(call), str(p_recur_search), str(p_file)])#p_file , p])
    except:
        try:
            os.system(r'notepad.exe ' + p_file)
        except:
            try:
                webbrowser.open(p_file)
            except:
                os.system(l.get(x))

    
#--------------------------------------#
def ondelete():
#--------------------------------------#
    for i in curr_sel[::-1]:  #w.curselection()[::-1]:
        try:
            l.delete(i)
        except:
            print("PYLope Sub Routine subr_search.py function ondelete unable to determine cursor position. Try setting cursor and retrying")

#--------------------------------------#
def onsaveas():
#--------------------------------------#
    import tkinter.filedialog
    files = [('Text Document', '*.txt'),
             ('All Files', '*.*'),  
             ('Python Files', '*.py')] 
    f = tkinter.filedialog.asksaveasfile(filetypes = files, defaultextension = files, mode='w') 
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(l.get(1, END)).replace(",", "\n") # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()

#----------------------------------------#
def get_filenames():
#----------------------------------------#
    
    if (len(sys.argv) < 2):
        return os.listdir('.')
    else:
        if p != []:
            stringList = []
            search_cnt = 0
            for i in os.listdir('.'):
                try:
                    if os.path.isfile(i) and os.access(i, os.R_OK):
                        with open(i, encoding="utf-8") as x:
                            line = x.readline()
                            cnt = 1
                            while line:
                                ###
                                ### Process p as List of search terms.
                                ###
                                term_found = 1 # True, assumed. Loop thru p and is false, break and do next line.
                                for p_term in p.split("+"):
                                    if (len(sys.argv) > 2):
                                        if p_case == '1':
                                            z = line.lower().find(p_term.lower())
                                        else:
                                            z = line.find(p_term)
                                    else:
                                        z = line.find(p_term)
                                    if z == -1:
                                    ###
                                    ### IF any p_term is false, break and do next line.
                                    ###
                                        term_found = 0
                                        break
                                if term_found:
                                    search_cnt += 1
                                    stringList.append("{} : Line {} : offset {}:      {}".format(i, cnt, z, line.strip()))
                                line = x.readline()
                                cnt += 1
                except:
                    temp_str = "Unable to open " + i + "...SKIPPING. Maybe binary data?"
                    stringList.append(temp_str)
                    
            return stringList, search_cnt

#----------------------------------------#
def write_header(l, str_header_1,str_search_cnt, search_cnt, str_dir, str_path):
#----------------------------------------#
    if (len(sys.argv) > 2):
        if p_case == '1':
            str_search_cnt = str_tot_1 + str(p) + str_tot_2b + str_any_case + str(search_cnt)
    else:
        str_search_cnt = str_tot_1 + str(p) + str_tot_2 + str(search_cnt)
    l.insert(END, str_dir)
    l.insert(END, astr_line)
    l.insert(END, str_search_cnt)
    l.insert(END, astr_line)
    return l
#----------------------------------------#
def write_report_line(l, str_path, getfilenames ):
#----------------------------------------#

    if search_cnt != "0":
        l.config(foreground = 'BLUE',
                 background = 'WHITE',
                 selectbackground = 'ORANGE',
                 selectforeground = 'DARKBLUE',
                 selectmode='multiple')
        l.insert(END, dash_line)
        l.insert(END, str_details)
        l.insert(END, dash_line)
        l.insert(END, spacer_line)
        for filename in getfilenames:
            if p_recur_search == '1':
                filename = str_path + "/" + filename
            l.insert(END, filename)
            l.insert(END, spacer_line)
    return l

#----------------------------------------#
def write_null_report():
#----------------------------------------#
    l = Listbox(root, height=25, width=85, bg='WHITE', fg='RED')
    root.wm_iconbitmap("./py.ico") 
    l.grid(column=0, row=0, sticky=(N,E,W,S))
    s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
    s.grid(column=1, row=0, sticky=(N,S))
    l['yscrollcommand'] = s.set
    l['xscrollcommand'] = s.set
    ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    l.insert(END, str1)
    l.insert(END, str2)
    l.insert(END, str3)
    l.insert(END, str4)
    l.insert(END, str1)
    l.config(foreground = 'RED',
             background = 'WHITE',
             selectbackground = 'ORANGE',
             selectforeground = 'DARKBLUE',
             selectmode='multiple')
    for filename in get_filenames():
        l.insert(END, filename)
    return l

#----------------------------------------#
def create_listbox_and_write(str_header_1,str_search_cnt, search_cnt, str_dir, str_path):
#----------------------------------------#
    l = Listbox(root, height=25, width=150, bg='YELLOW', fg='BLUE', selectmode='multiple')
    root.wm_iconbitmap(dir_path + "/" + "./py.ico") 
    l.master.title(">>> PYLope search results <<<")
    l.grid(column=0, row=0, sticky=(N,E,W,S))
    r = ttk.Scrollbar(root, orient=HORIZONTAL, command=l.xview)
    r.grid(column=0, row=1, sticky=(E,W))
    s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
    s.grid(column=1, row=0, sticky=(N,S))
    l['xscrollcommand'] = r.set
    l['yscrollcommand'] = s.set
    ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

 
    str_header_1 = str(str_header_1)
    global now
    str_header_1 = str_header_1 + now
    str_search_cnt = str(str_search_cnt)
    search_cnt = str(search_cnt)
   
    l.insert(END, dash_line)
    l.insert(END, str_header_1)
    l.insert(END, dash_line)
    l.insert(END, astr_line)
    return l

########################################
# S T A R T  H E R E
########################################
#--------------------------------------#
# H O U S E  K E E P I N G
#--------------------------------------#
dir_path = os.path.dirname(os.path.realpath(__file__))
index =0
search_cnt = 0
now = datetime.now()
now = str(now.strftime("%A %d. %B %Y %I:%M%p"))
#dir_path = os.getcwd()
str1 = "***********************************************************"
str2 = "* NO Search string supplied"
str3 = "* OR no Log file was supplied."
str4 = "* Printing contents of current directory."
spacer_line = " "
astr_line = "*"
dash_line =    "*----------------------------------------------------------------------------------------------------------------------"
str_header_1 = "* PYLOPE Search Report                                                        as of:    "
str_search_cnt = "Total of search items found "
str_tot_1      = "Total search cnt for  ["
str_tot_2      = "] : "
str_tot_2b     = "] "
str_any_case   = "( any case ) : "
str_dir        = "Path : "
str_details =  "*-------------------------------------------------- D E T A I L S ------------------------------------------------------"
root = Tk()
global str_path
str_path = os.getcwd()
str_dir = str_dir + str_path
if p != []:
    getfilenames, search_cnt = get_filenames()
l = create_listbox_and_write(str_header_1,str_search_cnt, search_cnt, str_dir, str_path)
########################################
# M A I N   L O G I C
########################################
if p != []:
    l = write_header(l, str_header_1,str_search_cnt, search_cnt, str_dir, str_path)
    l = write_report_line(l, str_path,getfilenames)
else:
    l = write_null_report()

l.bind('<<ListboxSelect>>', onselect)
l.bind('<FocusOut>', lambda e: l.selection_clear(0, END))
l.bind("<Button-3>", openfile)
root.bind("deleteButton", ondelete)
root.bind("saveasButton", onsaveas)  
deleteButton = Button(root, text='Delete', underline = 0, command=ondelete)
deleteButton.grid(column=1, row=1, sticky="e", padx=10, pady=10)
saveasButton = Button(root, text='Save As', underline = 0, command=onsaveas)
saveasButton.grid(column=0, row=1, sticky="e", padx=10, pady=10)


root.mainloop()