#!/bin/bash

echo ''
echo '-------------------------------------'
echo ' ----- MAKE THE WHEEL !!!!!!!! ------'
echo ''

case "${TOXENV}" in
    py2)
        python setup.py sdist
        ;;
    py3)
        python3 setup.py sdist
        ;;
esac


ls -lisah ./dist

mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz

ls -lisah ./dist
