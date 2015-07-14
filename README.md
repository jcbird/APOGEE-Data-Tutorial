# APOGEE-Data-Tutorial
APOGEE Data: "Zero to Hero" data access tutorial

This [ipython notebook](https://ipython.org/ipython-doc/3/notebook/notebook.html) will guide you through the basics of working with [APOGEE](https://www.sdss3.org/surveys/apogee.php) data from [Data Release 12](http://www.sdss.org/dr12/irspec/).
By the end of this tutorial, you will:
 - Download the APOGEE Parameter summary catalog
 - Access the catalog on your local machine
 - Know how to access stellar radial velocities and abundances
 - Analyze stars in different spatial regions of the Galaxy
 - Access the Red Clump catalog
 - Make scientifically-interesting plots

### Running the tutorial
clone this repository and run `ipython notebook` by typing the following on your command line in the directory of your choice.

```
git clone https://github.com/jcbird/APOGEE-Data-Tutorial.git
cd APOGEE-Data-Tutorial
ipython notebook
```

This will load an ipython console inside your browser. Click on *APOGEE Data "Zero to Hero".ipynb* to run the tutorial. The full output (including all plots) can be viewed without running the tutorial by viewing *APOGEE Data "Zero to Hero" Output.ipynb*. You may receive a message informing you that the notebook format version will be converted. Ignore the warning.

### Requirements
- `python`  2.7 or later (python3 compatible)
- `ipython` 2.1 or later 
- `matplotlib`
- `numpy`
- `pyfits` or `astropy` for FITS file reading

### Contributing

Please submit all bug reports, suggestions, and questions by submitting an issue.
By all means, if you are reading this and would actually like to make pull requests, please do so!
### Thanks
Melissa, Gail, Holtz, Jo, Carlos, EVERYONE

