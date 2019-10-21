# name: subr_search.py
# desc: Handles call to subr_search.py
import os, sys
try:
    import subprocess
except:
    os.system("pip install subprocess")
    import subprocess

#--------------------------------------#
def call_subr_search(p, p_case, p_whole, p_clear):
#--------------------------------------#
     
    if p_clear == '1':
        subprocess.call(["python", dir_path + "/" + "subr_search.py"])
    elif (p > " ") & (p_case == '1') & (p_whole == '1'):
        subprocess.call(["python", dir_path + "/" + "subr_search.py", p, str(p_case), str(p_whole)])
    elif (p > " ") & (p_case == '1'):
         subprocess.call(["python", dir_path + "/" + "subr_search.py", p, str(p_case)])
    elif p > " ":
         subprocess.call(["python", dir_path + "/" + "subr_search.py", p])
    else:
        subprocess.call(["python", dir_path + "/" + "subr_search.py"])


#####################################
# M A I N   L O G I C
#####################################
dir_path = os.path.dirname(os.path.realpath(__file__))
num_sysargv = 5
p = " "
p_case = 0
p_whole = 0
p_clear = 0

error_to_return = ("subr_call_search.py has error with sys.argv. len:", len(sys.argv), "sys.argv:", sys.argv)
if len(sys.argv) > 1: #== num_sysargv:
    p = sys.argv[1]
if len(sys.argv) > 2:
    p_case = sys.argv[2]
if len(sys.argv) > 3:
    p_whole = sys.argv[3]
if len(sys.argv) > 4:
    p_clear = sys.argv[4]
if len(sys.argv) > num_sysargv:
    print(error_to_return)

call_subr_search(p, p_case, p_whole, p_clear)