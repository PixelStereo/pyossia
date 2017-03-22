# PyOssia
[![Build Status](https://travis-ci.org/PixelStereo/pyossia.svg?branch=master)](https://travis-ci.org/PixelStereo/pyossia)    
    
PyOssia is a python module for [libossia](http://github.com/OSSIA/libossia)    

It will use libossia thanks to pybind11    

# Installation
`git clone https://github.com/PixelStereo/pyossia.git && git submodule update —-init    `
Wait 2 / 15 minutes depending on your internet connection
`cd pyossia    `
#### python 2
`python setup.py install    `
#### python 3
`python3 setup.py install    `
This will take 3 / 8 minutes depending on your computer processor.
libossia will be build and install into /usr/local/lib.   
it will also build and move ossia_python.so file to the pyossia module.    

Note that ossia_python.so does not have the same name depending on the python version used to install.
for python 2.7 it is `ossia_python.so` and 
`ossia_python.cpython-36m-darwin.so` for python 3.x.    

## latest unstable (git master branch)
`pip install git+https://github.com/PixelStereo/pyossia.git@master`

## git repo (for pyossia contribution)
`git clone https://github.com/PixelStereo/pyossia.git && git submodule update —-init`    

`cd pyossia     `    

`pip install -ve .    `

You can use PyQt to display libossia params with this module : [pyossia-pyqt](https://github.com/PixelStereo/pyossia-pyqt)
