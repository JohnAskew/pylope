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

    subprocess.call(["python", dir_path + "/" + "subr_search.py",p , str(p_case), str(p_whole), str(p_clear), str(call), str(p_recur_search), str(p_file)])


#####################################
# M A I N   L O G I C
#####################################
dir_path = os.path.dirname(os.path.realpath(__file__))

call_subr_search(p, str(p_case), str(p_whole), str(p_clear), str(call), str(p_recur_search), str(p_file))