#!/bin/py

import pandas as pd
import numpy as np
import os

# Get the pygrep script.
#dir = "/databases/mol/pdb"
dir = "/databases/mol/mmCIF"
def list_files_recursive(path):
    """
    Function that receives as a parameter a directory path
    :return list_: File List and Its Absolute Paths
    """

    files = []

    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    lst = [file for file in files]
    return lst

search_words_xray = ['ZINC','X-RAY']
def check_xray(filename):
    with open(filename, 'r') as f:
         datafile = f.read().replace('\n', '')
    if all(word in datafile for word in search_words_xray):
           return True
    return False

search_words_nmr = ['ZINC','NMR']
def check_nmr(filename):
    with open(filename, 'r') as f:
         datafile = f.read().replace('\n', '')
    if all(word in datafile for word in search_words_nmr):
            return True
    return False

nmr_list = []
xray_list = []
result = list_files_recursive(dir)
#res_base=os.path.basename(dir)
i = 0
j=0
for res in result:
    #with open(res, 'r') as f:
        # print (f.read())
    if check_xray(res):
       xray_loop = os.path.splitext(os.path.basename(res))[0].upper()
       print(xray_loop)
       xray_list.append(xray_loop)
       i += 1
       print ("seen xray", i, "number of times so far")
    if check_nmr(res):
       nmr_loop = os.path.splitext(os.path.basename(res))[0].upper()
       nmr_list.append(nmr_loop)
       j += 1
       print ("seen nmr", j, "number of times so far")


# Just for check

#nmr_1 = pd.DataFrame(nmr_list)
#xray_1 = pd.DataFrame(xray_list)

#print(nmr_1)
#print(nmr_list)

#nmr_1.to_csv("nmr_1.csv")
#xray_1.to_csv("xray_1.csv")

#    """
#    Compare the sequence
#    """



#    """
#    Get the molecular weight form the rcsb.org for final PDBs
#    """

moldata = pd.read_csv("PDBlist.csv", index_col ="structureId")

xray =[]
nmr = []

with open ("PDBlist.csv") as f:
    for line in f.readlines():
        a = line.split(',')
        if a[0] in nmr_list:
            nmr.append(float(a[2])/1000)
        if a[0] in xray_list:
            xray.append(float(a[2])/1000)

print(xray)
print(nmr)

np.save("xray.npy",np.array(xray))
np.save("nmr.npy",np.array(nmr))

