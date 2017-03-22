# PyOssia
[![Build Status](https://travis-ci.org/PixelStereo/pyossia.svg?branch=master)](https://travis-ci.org/PixelStereo/pyossia)    
    
PyOssia is a python module for [libossia](http://github.com/OSSIA/libossia)    

It will use libossia thanks to pybind11    

# Installation

pip install will build libossia, and install it into /usr/local/lib.   
it will also build and move ossia_python.so file to /usr/local/lib, but this last operation is a bug in pyossia setup.    
You have to manually copy the ossia_python.so to the pyossia module for the moment.    

ossia_python.so => python 2.7
ossia_python.cpython-36m-darwin.so => python 3.x

## latest stable
pyossia does not have yet a stable version

## latest unstable (git master branch)
`pip install git+https://github.com/PixelStereo/pyossia.git@master`

## git repo (for pyossia contribution)
`git clone https://github.com/PixelStereo/pyossia.git && git submodule update —-init`    

`cd pyossia     `    

`pip install -ve .    `

