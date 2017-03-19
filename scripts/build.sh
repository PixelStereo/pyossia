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

ls -lisah
ls -lisah ./3rdparty/
ls -lisah ./3rdparty/libossia
ls -lisah ./3rdparty/libossia/build

python setup.py sdist

ls -lisah ./dist

echo ${REPO}-${TRAVIS_TAG}_$TRAVIS_OS_NAME
echo ${REPO}-${TRAVIS_TAG}
