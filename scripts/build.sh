#!/bin/bash

cd 3rdParty/libossia
ls -lisah
mkdir -p build
cd build
cmake ..
make -j4