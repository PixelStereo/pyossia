#!/bin/bash

echo '------'
echo $TOXENV
echo '------'
case ${TOXENV} in
    py27)
        echo 'python 2.7'
        sudo apt-get install python
        pip install -ve .

        ;;
    py34)
        echo 'python 3.4'
        sudo apt-get install python3
        pip3 install -ve .
        ;;
    py35)
        echo 'python 3.5'
        sudo apt-get install python3
        pip3 install -ve .
        ;;
    py36)
        echo 'python 3.6'
        sudo apt-get install python3
        pip3 install -ve .
        ;;
esac

python setup.py sdist


#ls -lisah dist

#mv dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz

#ls -lisah dist
