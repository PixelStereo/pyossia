# PyOssia
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/412e49413bb248e78ba1bd55f6ec19eb)](https://www.codacy.com/app/reno-/pyossia?utm_source=github.com&utm_medium=referral&utm_content=PixelStereo/pyossia&utm_campaign=badger)
[![Build Status](https://travis-ci.org/PixelStereo/pyossia.svg?branch=master)](https://travis-ci.org/PixelStereo/pyossia)    
    
PyOssia is a python module for [libossia](http://github.com/OSSIA/libossia)    

It will use libossia thanks to pybind11    

# Installation

pip install will build libossia_python, and include it in a python module    

## latest stable
pyossia does not have yet a stable version

## latest unstable (git master branch)
`pip install git+https://github.com/PixelStereo/pyossia.git@master`

## git repo (for pyossia contribution)
`git clone https://github.com/PixelStereo/pyossia.git && git submodule update —-init`    

`cd pyossia     `    

`pip install -ve .    `

'-e' option will just add the git repo to your python path