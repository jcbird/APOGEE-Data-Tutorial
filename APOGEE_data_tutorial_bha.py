#----- Section 6.1 -----

from __future__ import print_function
import numpy as np
import os
import sys
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_context('talk', font_scale=1.25)
 
### Functions for automatic downloading of catalog
import urllib  
### Checking for python 2 or 3
if sys.version_info > (3,0): # If python3
    geturl_func = urllib.request.urlretrieve
else: #python2
    geturl_func = urllib.urlretrieve

#Progress bar function for automatic download (You can ignore this)
try:
    from IPython.html.widgets import FloatProgress
    from IPython.display import display
    from time import sleep
    progbar = FloatProgress(min=0, max=100, description='Download Progress...')
    html_widget = True
    def report(count, blockSize, totalSize):   #function to report download percentage
        percent = count*blockSize*100/float(totalSize)
        progbar.value = percent

except ImportError:
    html_widget = False
    from IPython.display import clear_output   #function to clear cell output
    def report(count, blockSize, totalSize):   #function to report download percentage
        percent = count*blockSize*100/float(totalSize)
        if (count % 100) ==0: #only update every 40 blocks 
            print('{0:.2f}'.format(percent), end=' ')

print('Preamble successful!')
#-----



#----- Section 6.2 -----

data_directory = "/Users/andrews/apogee/data/"  #### CHANGE THIS PATH

if not os.path.exists(data_directory):
    print("\nMake sure the data_directory path exists!\n")
else:
    print("Your APOGEE data directory is: {}\nWoohoo! Let's get started!".format(data_directory))

#-----



#----- Section 6.3 -----

try:
    import astropy.io.fits as pyfits
except ImportError:
    import pyfits

allStar_file = 'allStar-v603.fits'
allStar_localpath = os.path.join(data_directory,allStar_file)

allStar_file_link = "http://data.sdss3.org/sas/dr12/apogee/spectro/redux/r5/allStar-v603.fits"

#Download allStar file if it does not exist (This will take a while!)
if not os.path.exists(allStar_localpath):
    print ('% Complete: ', end=' ' )
    if html_widget:
        display(progbar)
    geturl_func(allStar_file_link, filename=allStar_localpath, reporthook=report)

try:
    allStar_fits = pyfits.open(allStar_localpath)
    allStar = allStar_fits[1].data #Takes data is HDU 1 and assigns it to allStar
    print('allStar file loaded and ready to rock')
except ValueError:
    print('FITS reader error: The catalog file is likely not complete.')
    print('Use the direct download link in Section 5 and copy file into the data_directory path.')

#-----



#----- Section 6.4 -----
print('Number of stars: {0}'.format(allStar.shape[0]))

allStar_keys = list(allStar.dtype.fields.keys())
for it in np.sort(allStar_keys):
    print(it)

#-----



#----- Section 7.1 -----

fig =plt.figure()
ax = plt.subplot(111) ## Ask Gail how she does the box around the projection, projection='mollweide') # set up projection
# For pretty plotting, make longitude negative relative to Galactic center.␣
l_corr_inds = allStar['GLON']>180 #indices for GLON correction
l_corr = allStar['GLON'].copy() # just to be safe,
l_corr[l_corr_inds] -=360
ax.scatter(l_corr, allStar['GLAT'], edgecolor='none', alpha=0.3)
ax.set_xlim(180,-180)
ax.set_xlabel('Galactic Longitude')
ax.set_ylabel('Galactic Latitude')
#-----

