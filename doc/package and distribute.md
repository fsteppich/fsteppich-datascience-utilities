# How to Package and Distribute this Package
_internal notes_

These internal note serve the sole purpose of reminding me how to build, upload and 
install this package on (test.)pypi.org.  

## Build the package
~~~~
# Build the package
C:\fsteppich-datascience-utilities>  python setup.py sdist
~~~~

## Installation

### Local (installation only)
~~~~
# Install the package from current folder
C:\fsteppich-datascience-utilities> pip install --user .
~~~~

### test.pypi.org (upload and installation)
~~~~
# Upload via twine to test.pypi.org (twine @ 
# C:\Users\fsteppich\AppData\Roaming\Python\Python38\Scripts\twine)
C:\fsteppich-datascience-utilities> twine upload --repository-url https://test.pypi.org/legacy/ .\dist\*

# Install the package from test.pypi.org
C:\fsteppich-datascience-utilities> pip install --user --index-url https://test.pypi.org/simple/ fs-ds-util
~~~~

## Verification
~~~~
# Verify the package installation
C:\fsteppich-datascience-utilities> python
>>> from fs_ds_util import sysout as s
>>> s.error("foobar")
[X] <stdin>:1 - foobar
>>> exit()

# Remove the package installation
C:\fsteppich-datascience-utilities>  pip uninstall fs-ds-util
~~~~
