#!/bin/bash

case "$TRAVIS_OS_NAME" in
  linux)
  export CMAKE_BIN=$(readlink -f "$(find cmake/bin -name cmake -type f )")
  ;;
  osx)
  export CMAKE_BIN=$(which cmake)
  ;;
esac

echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- Explore 3rdParty Folder ------'
echo ''
echo ''
ls -lisah ./3rdParty/
echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- Explore libossia Folder ------'
echo ''
echo ''
ls -lisah ./3rdParty/libossia
echo ''
echo ''
echo ''
echo '-------------------------------------'
echo ' ----- Explore build Folder ------'
echo ''
echo ''
ls -lisah ./3rdParty/libossia/build

echo ''
echo ''
echo ''
echo '--------------------------------------'
echo ' ----- INSTALL WITH PIP locally ------'
echo ''
echo ''




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
echo ' ----- MAKE THE WHEEL !!!!!!!! ------'
echo ''
echo ''
python setup.py sdist

ls -lisah ./dist

echo ${REPO}-${TRAVIS_TAG}_$TRAVIS_OS_NAME
echo ${REPO}-${TRAVIS_TAG}
