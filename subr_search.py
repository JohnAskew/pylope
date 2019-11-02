import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
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

dir_path = os.path.dirname(os.path.realpath(__file__))
index = 0
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
    #p_file = str_path + "/" + p_file
    
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
        if p != " ":
            stringList = []
            search_cnt = 0
            for i in os.listdir('.'):
                try:
                    with open(i, encoding="utf-8") as x:
                        line = x.readline()
                        cnt = 1
                        while line:
                            if (len(sys.argv) > 2):
                                if p_case == '1':
                                    z = line.lower().find(p.lower())
                                else:
                                    z = line.find(p)
                            else:
                                z = line.find(p)
                            if z > -1:
                                search_cnt += 1
                                #DEBUG print("search_cnt:", search_cnt, "File {} : Line {} : offset {}: {}".format(i, cnt, z, line.strip()))
                                stringList.append("{} : Line {} : offset {}:      {}".format(i, cnt, z, line.strip()))
                                
                            line = x.readline()
                            cnt += 1
                except:
                    temp_str = "Unable to open " + i + "...SKIPPING. Maybe binary data?"
                    stringList.append(temp_str)
                    
            return stringList, search_cnt


########################################
# M A I N   L O G I C
########################################
root = Tk()
global str_path
str_path = None
if p != " ":
    l = Listbox(root, height=25, width=120, bg='YELLOW', fg='BLUE', selectmode='multiple')
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
    getfilenames, search_cnt = get_filenames()
    now = datetime.now()
    now = str(now.strftime("%A %d. %B %Y %I:%M%p"))
    str_header_1 = str(str_header_1)
    str_header_1 = str_header_1 + now
    str_search_cnt = str(str_search_cnt)
    search_cnt = str(search_cnt)
    if (len(sys.argv) > 2):
        if p_case == '1':
            str_search_cnt = str_tot_1 + p + str_tot_2b + str_any_case + search_cnt
    else:
        str_search_cnt = str_tot_1 + p + str_tot_2 + search_cnt
    l.insert(END, dash_line)
    l.insert(END, str_header_1)
    l.insert(END, dash_line)
    l.insert(END, astr_line)
    str_path = os.getcwd()
    str_dir = str_dir + str_path
    l.insert(END, str_dir)
    l.insert(END, astr_line)
    l.insert(END, str_search_cnt)
    l.insert(END, astr_line)
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
        #l.config(foreground = 'RED', background = 'YELLOW')

        for filename in getfilenames:
            filename = str_path + "/" + filename
            l.insert(END, filename)
            l.insert(END, spacer_line)
else:
    l = Listbox(root, height=25, width=85, bg='WHITE', fg='RED')
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