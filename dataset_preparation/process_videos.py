from shutil import copyfile
import sys
import os
import os.path

copyfile(src, dst)

if __name__=='__main__':
    old_dir = sys.argv[1] #clevrer, not clevrer/annotations
    new_dir = sys.argv[2] #dcl_clevrer, not dcl_clevrer/annotations
    #Create new_dir/annotations 
    os.path.join(new_dir, #"")
    os.mkdir()
    #List all files in old_dir, then copy all of them to new_dir

