# Question: Please concatenate this file with this one to a single text file. The content of the output file should look like below.

# Expected output: 

# x,y
# 3,5
# 4,9
# 6,10
# 7,11
# 8,12
# 6,10
# 8,18
# 12,20
# 14,22
# 16,24

import pandas as pd

sampletext = pd.read_csv("sampledata.txt")
sampletext2 = pd.read_csv("sampledata_x_2.txt")

sampletext3 = pd.concat([sampletext, sampletext2])

sampletext3.to_csv('sampletext3.txt',index=None) 




