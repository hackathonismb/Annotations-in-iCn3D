## Combining all individual PTM csv files
## Usage combine_ptmsfiles.py
import os
import sys
import glob
import pandas as pd
os.chdir("/home/k3sachin/PTM/PTMs")
ptm = 'csv'
all_ptms = [p for p in glob.glob('*.csv'.format(ptm))]
combined_ptms = pd.concat([pd.read_csv(q) for q in all_ptms ])
#combined all ptms
combined_ptms.to_csv( "Combined_PTMs.csv", index=False, encoding='utf-8-sig')
