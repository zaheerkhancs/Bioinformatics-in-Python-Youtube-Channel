import os

# Define a function here....
def DeleteFiles(Dir):
    for root, dirs, files in os.walk(Dir):
        for item in files:
            # delete sub files in the dir while walk...
            filespec=os.path.join(root,item)
            if filespec.endswith('.txt') or filespec.endswith('.png'):
                os.unlink(filespec)
        for item in dirs:
            DeleteFiles(os.path.join(root,item))

# Now define the Main function...

if __name__=='__main__':
    dir='../yourrootfolder/'
    #call the above function...
    DeleteFiles(dir)


    ##
    ## Thanks for watching....