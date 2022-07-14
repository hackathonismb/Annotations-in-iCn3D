## PTMs data extractions based on the user input uniprot ids
##Usage python3 ptms_user_uniprot.py example_user_uniprot.txt Combined_PTMs.csv
import sys
import glob
import pandas as pd
file1= sys.argv[1] # list of the uniprot id such as Q8R3W2 mentioned example_user_uniprot.txt
fh = open(file1.strip(),"r")
file2= sys.argv[2] # combined ptms file
fh2 = open(file2.strip(),"r")
#z=fh.readline()

uniprotId=[]
for line in fh:
    line=line.strip()
    uniprotId.append(line)
print(uniprotId)
ptms=[]
for line in fh2:
    line=line.strip().split(",")
   # print(line)
    ptms.append(line)

Uniprot_ptms=[]
for i in uniprotId:
    #print(a)
    for j in ptms:
        b=j[0]
        #print(b)
        if i==b:
            Uniprot_ptms.append(j)
print(len(Uniprot_ptms))
df2 = pd.DataFrame(Uniprot_ptms, columns=["UniprotId", "PTMaa","PTMpos","PTMs","Metadata"])
df2.to_csv('Uniprot_ptms.csv', index=False)
