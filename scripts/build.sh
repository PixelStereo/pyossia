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
ls -lisah ./3rdparty/libossia/build
zip ./3rdparty/libossia/build/${REPO}_${TRAVIS_TAG}_$TRAVIS_OS_NAME.zip ${REPO}_${TRAVIS_TAG}
zip ./dist/${REPO}_${TRAVIS_TAG}_$TRAVIS_OS_NAME.zip ${REPO}_${TRAVIS_TAG}
ls -lisah
cd ../
