#!/bin/bash

cd 3rdParty/libossia
ls -lisah
mkdir -p build
cd build
cmake .. -DOSSIA_PD=0 -DOSSIA_QT=0 -DOSSIA_STATIC=1 -DOSSIA_C=0 -DOSSIA_NO_QT=1

make -j4