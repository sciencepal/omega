#   Python 3.4 code to find maximum sized file in a given directory structure
#   Tested On Linux Mint 17.3

import os

def max_size_file(startpath):
    err= getattr(__builtins__,'FileNotFoundError', IOError)
    mex = -1
    fn=''
    fs=0
    ds=0
    missed=0
    for root, dirs, files in os.walk(startpath):
        ds+=1
        for f in files:
            fs+=1
            try:
                sz = os.stat(root+'/'+f).st_size
                if (sz > mex):
                    mex = sz
                    fn = root+'/'+f
            except err:
                missed+=1
    return mex,fn,fs,ds,missed


while (True):
    x = input("\nEnter the exact path of folder whose contents you want to analyze, 0 to exit\n")
    if (x=="0"):
        exit(0)
    #ans,fname,files,dirs,missed = max_size_file('/home/aditya/Desktop/')
    ans,fname,files,dirs,missed = max_size_file(x)
    if (files == 0):
        print ("Invalid Directory")
        continue
    ans=ans/(1000*1000)
    ans = round(ans, 1)
    print ("File with maximum size : "+fname)
    print ("Size of file : "+str(ans)+" MB")
    print ("# Directories scanned : "+str(dirs))
    print ("# Files scanned : "+str(files))
    print ("# Files failed to scan : "+str(missed))
