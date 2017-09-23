#!/bin/bash

echo ''
echo '-------------------------------------'
echo ' ----- MAKE THE WHEEL !!!!!!!! ------'
echo ''

case "${TOXENV}" in
    py2)
        pip install -e .
        python setup.py sdist
        ;;
    py3)
        pip3 install -e .
        python3 setup.py sdist
        ;;
esac


ls -lisah ./dist

mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz

ls -lisah ./dist
