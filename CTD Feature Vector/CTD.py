import re, sys, os

#Reading a Fasta file,
def ReadFasta(FileName):
    if not os.path.exists(FileName):
        print('Error: "' + FileName + '" does not exist.')
        sys.exit(1)
    with open(FileName) as f:
        records = f.read()
    if re.search('>', records) is None:
        print('The input file seems not in fasta format.')
        sys.exit(1)
    records = records.split('>')[1:]
    myFasta = []
    for fasta in records:
        array = fasta.split('\n')
        name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())
        myFasta.append([name, sequence])
    return myFasta

# create function to count the amino acid in a sequence
def Count(seq1, seq2):
    sum=0
    for count_ in seq1:
        sum=sum+seq2.count(count_)
    return sum

def CTD(FastaFile):
    """
    CTD: Composition Transition and Distribution....
    A feature extraction Algorithm which generate feature vector over three groups based on different physiochemical properties.
    :param FastaFile:
    :return:
    """
    group1 = {
        'hydrophobicity_PRAM900101': 'RKEDQN',
        'hydrophobicity_ARGP820101': 'QSTNGDE',
        'hydrophobicity_ZIMJ680101': 'QNGSWTDERA',
        'hydrophobicity_PONP930101': 'KPDESNQT',
        'hydrophobicity_CASG920101': 'KDEQPSRNTG',
        'hydrophobicity_ENGD860101': 'RDKENQHYP',
        'hydrophobicity_FASG890101': 'KERSQD',
        'normwaalsvolume': 'GASTPDC',
        'polarity': 'LIFWCMVY',
        'polarizability': 'GASDT',
        'charge': 'KR',
        'secondarystruct': 'EALMQKRH',
        'solventaccess': 'ALFCGIVW'
    }
    group2 = {
        'hydrophobicity_PRAM900101': 'GASTPHY',
        'hydrophobicity_ARGP820101': 'RAHCKMV',
        'hydrophobicity_ZIMJ680101': 'HMCKV',
        'hydrophobicity_PONP930101': 'GRHA',
        'hydrophobicity_CASG920101': 'AHYMLV',
        'hydrophobicity_ENGD860101': 'SGTAW',
        'hydrophobicity_FASG890101': 'NTPG',
        'normwaalsvolume': 'NVEQIL',
        'polarity': 'PATGS',
        'polarizability': 'CPNVEQIL',
        'charge': 'ANCQGHILMFPSTWYV',
        'secondarystruct': 'VIYCWFT',
        'solventaccess': 'RKQEND'
    }
    group3 = {
        'hydrophobicity_PRAM900101': 'CLVIMFW',
        'hydrophobicity_ARGP820101': 'LYPFIW',
        'hydrophobicity_ZIMJ680101': 'LPFYI',
        'hydrophobicity_PONP930101': 'YMFWLCVI',
        'hydrophobicity_CASG920101': 'FIWC',
        'hydrophobicity_ENGD860101': 'CVLIMF',
        'hydrophobicity_FASG890101': 'AYHWVMFLIC',
        'normwaalsvolume': 'MHKFRYW',
        'polarity': 'HQRKNED',
        'polarizability': 'KMHFRYW',
        'charge': 'DE',
        'secondarystruct': 'GNPSD',
        'solventaccess': 'MSPTHY'
    }
    # created three groups dictionary with corresponding key values , these values are sub sequence peptides of different amino acids
    groups=[group1,group2, group3] # create a list of groups (1,2,3) dictionaries
    # Now put all these properties in each groups in a groups list variable
    property = (
        'hydrophobicity_PRAM900101', 'hydrophobicity_ARGP820101', 'hydrophobicity_ZIMJ680101', 'hydrophobicity_PONP930101',
        'hydrophobicity_CASG920101', 'hydrophobicity_ENGD860101', 'hydrophobicity_FASG890101', 'normwaalsvolume',
        'polarity', 'polarizability', 'charge', 'secondarystruct', 'solventaccess')
    encodings=[] # create a encoding list variable to hold the header and features
    header=['#']
    for Counter_ in FastaFile:
        name, sequence=Counter_[0], re.sub('-','',Counter_[1])
        """
        name variable is assigned the header, while the sequence is assigned the rest of the sequence 
        """
        code=[name] # variable to hold the name (header)
        for pcount in property:
            c1=Count(group1[pcount],sequence)/len(sequence)
            c2=Count(group2[pcount],sequence)/len(sequence)
            c3=1-c1-c2
            code=code+[c1,c2,c3]
            rfcode = re.sub(r'[^#0-9.,a-zA-Z]', "", str(code))  # Obtain only header Info and respective three values of c1, c2 &c3
        encodings.append(rfcode) # append lastly, the generated feature vector to the list
    return encodings

# create a main function to call the above function

if __name__=='__main__':
    FastaFileName='datacnc.fasta'
    Fasta=ReadFasta(FastaFileName)
    encodings=CTD(Fasta)

    # save to desk the generated feature vector
    with open('CTF.txt','w+') as F:
        for item in encodings:
            F.write(item)
            F.write('\n')
        F.close()
    #
    #Thanks for watching....





