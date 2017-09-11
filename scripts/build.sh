#!/bin/bash

case "${TOXENV}" in
    py2)
        sudo apt-get install python
        pip install -ve .
        pandoc --from=markdown --to=rst --output=README README.md
        ;;
    py3)
        sudo apt-get install python3
        pip3 install -ve .
        pandoc --from=markdown --to=rst --output=README README.md
esac



echo ''
echo ''
echo '-------------------------------------'
echo ' ----- MAKE THE WHEEL !!!!!!!! ------'
echo ''
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
