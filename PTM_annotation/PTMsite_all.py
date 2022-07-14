##Annotation of Post-translational Modification (PTMs) such as phosphorlyation (S/T/Y), ubiquitylation (K), acetylation (K), methylation (K/R) and Sumoylation (K) in iCn3D downloaded from PhosphoSitePlus database https://www.phosphosite.org
## Usage python3 PTMs.py file1 file2
import sys
import glob
import pandas as pd
import re
file1= sys.argv[1] # Input PTMs sites file
fh = open(file1.strip(),"r")
z=fh.readline()

file2= sys.argv[2] # Input FASTA file
fh2=open(file2.strip(),"r")

pd.set_option('display.max_columns', None)
df=pd.read_csv(file1.strip(), sep=',')
print(df.head())
# function to split alpha_numberic characters example ["S119-p"] to ["S","119","-p"]
def split_text(alnumspchr):
    return filter(None, re.split(r'(\d+)', alnumspchr))

##Acetylation, Methylation, Phosphorylation, Sumoylation, and Ubiquitination
num=1
PTM=[]
for i in fh:
    a=i.strip().split(",")
    #print(a[0:10])
    UniId=a[2]
    UniSite=int(a[5])+num
    PTMsite=list(split_text(a[4]))
    PTM.append([UniId,PTMsite[0],PTMsite[1],"Ubiquitination","https://www.phosphosite.org/siteAction.action?id="+str(UniSite)])
    
print(df.shape)
print(PTM[0:100])
print(len(PTM))

df2 = pd.DataFrame(PTM, columns=["UniprotId", "PTMaa","PTMpos","PTMs","Metadata"])
df2.to_csv('PTM_Ubiquitination.csv', index=False)

## corresponding FASTA file processing
tmp=[]
counter=0
for t,k in enumerate(fh2):
    if k.startswith(">"):
        l=k.strip().split("|")[-1]
        tmp.append(l)
        counter=counter+1
print(len(tmp))

