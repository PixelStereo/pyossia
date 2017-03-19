#!/bin/bash

case "${TOXENV}" in
    py27)
        sudo apt-get install python
        pip install -ve .

        ;;
    py34)
        sudo apt-get install python3
        pip3 install -ve .
        ;;
    py35)
        sudo apt-get install python3
        pip3 install -ve .
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

mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV_$TRAVIS_OS_NAME.tar.gz

ls -lisah ./dist
