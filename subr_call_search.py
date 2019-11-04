# name: subr_call_search.py
# desc: Handles call to subr_search.py
import os, sys
try:
    import subprocess
except:
    os.system("pip install subprocess")
    import subprocess
try:
    from pylope_parameters import *
except ModuleNotFoundError:
    raise ModuleNotFoundError ('Missing pylope_parameters file. Unable to pass parameters between programs')

#--------------------------------------#
def call_subr_search(p, p_case, p_whole, p_clear, call, p_recur_search, p_file):
#--------------------------------------#
     
    if p_clear == '1':
        subprocess.call(["python", dir_path + "/" + "subr_search.py"])
    elif (p != []) & (p_case == '1') & (p_whole == '1'):
        subprocess.call(["python", dir_path + "/" + "subr_search.py", p, str(p_case), str(p_whole)])
    elif (p != []) & (p_case == '1'):
         subprocess.call(["python", dir_path + "/" + "subr_search.py", p, str(p_case)])
    elif p != []:
         subprocess.call(["python", dir_path + "/" + "subr_search.py", p])
    else:
        subprocess.call(["python", dir_path + "/" + "subr_search.py"])


#####################################
# M A I N   L O G I C
#####################################
dir_path = os.path.dirname(os.path.realpath(__file__))
call_subr_search(p, p_case, p_whole, p_clear, call, p_recur_search, p_file)