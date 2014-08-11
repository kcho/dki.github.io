
# In[1]:

import os
import re
import sys


# In[2]:

os.chdir('/Volumes/CCNC_3T/KangIk/2014_05_DKI_project/CHR27_JTM/DKI')


# In[4]:

imageList = [x for x in os.listdir(os.getcwd()) if 'nii' in x]


# In[5]:

imageList


# Out[5]:

#     ['20110211_192402DKI30DbvalueNB063s004a001.nii.gz',
#      'dax.nii',
#      'dax_dti.nii',
#      'dmean.nii',
#      'dmean_dti.nii',
#      'drad.nii',
#      'drad_dti.nii',
#      'fa.nii',
#      'fa_dti.nii',
#      'kax.nii',
#      'kmean.nii',
#      'krad.nii',
#      'nodif.nii.gz',
#      'nodif_brain.nii.gz',
#      'nodif_brain_mask.nii.gz']

# In[10]:

for i in imageList:
    print i
    output = os.popen('fslinfo {image}'.format(image=i)).readlines()
    print output[1:4]


# Out[10]:

#     20110211_192402DKI30DbvalueNB063s004a001.nii.gz
#     ['dim1           128\n', 'dim2           128\n', 'dim3           40\n']
#     dax.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     dax_dti.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     dmean.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     dmean_dti.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     drad.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     drad_dti.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     fa.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     fa_dti.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     kax.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     kmean.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     krad.nii
#     ['dim1           240\n', 'dim2           256\n', 'dim3           170\n']
#     nodif.nii.gz
#     ['dim1           128\n', 'dim2           128\n', 'dim3           40\n']
#     nodif_brain.nii.gz
#     ['dim1           128\n', 'dim2           128\n', 'dim3           40\n']
#     nodif_brain_mask.nii.gz
#     ['dim1           128\n', 'dim2           128\n', 'dim3           40\n']
# 

# In[ ]:



