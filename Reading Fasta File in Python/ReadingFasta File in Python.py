import sys
import os
import re

def ReadFasta(FileName):
    if os.path.exists(FileName)==False:
        print("File not found...")
        sys.exit(1)
    with open(FileName) as f:
        records=f.read()
    if re.search('>',records)==None:
        print("File is not in Fasta Format")
        sys.exit(1)

    records=records.split('>')[1:]
    myFasta=[]
    for fasta in records:
        array=fasta.split(())
        header, sequence=array[0].split()[0],re.sub('[^ARNDCQEGHILKMFPSTWYV-]',
               '-', ''.join(array[1:]).upper())
        myFasta.append([header,sequence])
    return myFasta

if __name__=='__main__':
    FileName='Sample.fasta'
    ReadFasta(FileName)

    # Thanks for watching....
