# APOGEE-Data-Tutorial
APOGEE Data: "Zero to Hero" data access tutorial

This [ipython notebook](https://ipython.org/ipython-doc/3/notebook/notebook.html) will guide you through the basics of interacting with [APOGEE](https://www.sdss3.org/surveys/apogee.php) data from [Data Release 12](http://www.sdss.org/dr12/irspec/) using *python*.  

By the end of this tutorial, you will:
 - Download the APOGEE Parameter summary catalog
 - Access the catalog on your local machine
 - Know how to access stellar radial velocities and abundances
 - Analyze stars in different spatial regions of the Galaxy
 - Access the Red Clump catalog
 - Make scientifically-interesting plots

### Running the tutorial
**If this is your first Ipython Notebook, don't panic.** The quick instructions below should work on your machine. 
Clone this repository and run `ipython notebook` by typing the following on your command line in the directory of your choice.

```
git clone https://github.com/jcbird/APOGEE-Data-Tutorial.git
cd APOGEE-Data-Tutorial
ipython notebook
```

This will load an ipython console inside your browser. Click on *APOGEE_data_tutorial.ipynb* to run the tutorial. The full output (including all plots) can be viewed without running the tutorial by viewing *APOGEE_data_tutorial.output.ipynb* in your console or clicking the link towards the top of this page. 

You may receive a message informing you that the notebook format version will be converted. If you can dismiss the warning and the notebook loads, you're set. 

**If you have any issues opening the notebook, see the following section.**

### *Ipython Notebook Issues*
The *APOGEE_data_tutorial.ipynb* is a v4 project Jupyter notebook, the latest version of the Ipython notebook. If you are not familiar with Jupyter notebooks OR you have any issues running the notebook, your first option is to run one of the back-ported notebooks included in the repository. Typing `ipython notebook` will launch the console in your browser. From there, you can run:


<dl>
  <dt>APOGEE_data_tutorial.ver3comp.ipynb</dt>
  <dd>v3 Ipython notebook. Try this first. It should work if your matplotlib/python/ipython installation is reasonably up to date.</dd>

  <dt>APOGEE_data_tutorial.ver2comp.ipynb</dt>
  <dd>v2 Ipython notebook. Use this if both <em>APOGEE_data_tutorial.ver3comp.ipynb</em> and <em>APOGEE_data_tutorial.ipynb</em> fail. This should be compatible with Ipython 0.12 and up.</dd>
</dl>

### Requirements
- `python`  2.7 or greater (python3 compatible)
- `ipython` 0.12 or greater (version >=2.1 preferred)
- `matplotlib`
- `numpy`
-  `astropy` or `pyfits` for FITS file reading

### Keeping Current
If you have already cloned the repository, simply type `git clone` in the APOGEE_DATA_TUTORIAL directory to update to the latest version.

### Contributing

Please submit all bug reports, suggestions, and questions by submitting an issue.
By all means, if you are reading this and would actually like to make pull requests, please do so!
### Thanks
Melissa, Gail, Holtz, Jo, Carlos, EVERYONE

