#!/bin/bash

ls -lisah

case "${TOXENV}" in
    py27)
        sudo apt-get install python
        pip install -ve .

        ;;
    py36)
        sudo apt-get install python3
        pip3 install -ve .
        ;;
esac
echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- Explore 3rdparty Folder ------'
echo ''
echo ''
ls -lisah ./3rdparty/
echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- Explore libossia Folder ------'
echo ''
echo ''
ls -lisah ./3rdparty/libossia
echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- Explore build Folder ------'
echo ''
echo ''
ls -lisah ./3rdparty/libossia/build

echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- END END END END END END ------'
echo ''
echo ''
python setup.py sdist

ls -lisah ./dist

echo ${REPO}-${TRAVIS_TAG}_$TRAVIS_OS_NAME
echo ${REPO}-${TRAVIS_TAG}
