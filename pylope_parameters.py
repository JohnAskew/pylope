import os, sys
p = []   #sys.argv[1] ==> poor programmming, that's why
p_case = 0  #sys.argv[2] ==> again, poor programming, that's why
p_whole = 0 #sys.argv[3] ==>
p_clear = 0 #sys.argv[4] ==>
call = 1    #sys.argv[5] ==>
p_recur_search = 0 #sys.argv[6]
p_file = [""] #sys.argv[7]
num_sysargv = 8 #Include sys.argv[0] - the calling program.

error_to_return = (os.path.basename(__file__), "has error with sys.argv. len:", len(sys.argv), "sys.argv:", sys.argv)

if __name__ != '__main__':
    if len(sys.argv) > 1: 
        p = sys.argv[1]
    if len(sys.argv) > 2:
        p_case = sys.argv[2]
    if len(sys.argv) > 3:
        p_whole = sys.argv[3]
    if len(sys.argv) > 4:
        p_clear = sys.argv[4]
    if len(sys.argv) > 5:
        call = sys.argv[5]
    if len(sys.argv) > 6:
        p_recur_search = sys.argv[6]
    if len(sys.argv) > 7:
        p_file = sys.argv[7]
    if len(sys.argv) > num_sysargv:
        print(error_to_return)