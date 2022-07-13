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

PTM=[]
for i in fh:
    a=i.strip().split(",")
    #print(a[0:10])
    UniId=a[2]
    UniSite=a[5]
    PTMsite=list(split_text(a[4]))
    PTM.append([UniId,PTMsite[0:2], UniSite])
    
print(df.shape)
print(PTM[0:100])
print(len(PTM))

output=[]
num=1 #In the original downloaded file the sites are offset by -1, for example 1868286063 instead of 1868286064
for j in PTM:
    #out=j[0],','.join(j[1]),"http://www.phosphosite.org/uniprotAccAction?id{}=".format(j[0])
    #input()
    k=int(j[2])+num
    output.append([j[0],','.join(j[1])[0],','.join(j[1])[2:],"https://www.phosphosite.org/siteAction.action?id="+str(k)])

print(len(output))
df2 = pd.DataFrame(output, columns=["UniprotId", "PTMaa","PTMpos", "Metadata"])
df2.to_csv('output_ptms.csv', index=False)

## corresponding FASTA file processing
UniP=[]
counter=0
for t,k in enumerate(fh2):
    if k.startswith(">"):
        l=k.strip().split("|")[-1]
        UniP.append(l)
        counter=counter+1
print(UniP)