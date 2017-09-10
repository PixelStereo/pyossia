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

pandoc --from=markdown --to=rst --output=README README.md

echo ''
echo ''
echo '-------------------------------------'
echo ' ----- MAKE THE WHEEL !!!!!!!! ------'
echo ''
echo ''

case "${TOXENV}" in
    py27)
        python setup.py sdist
        ;;
    py34)
        python3 setup.py sdist
        ;;
    py35)
        python3 setup.py sdist
        ;;
    py36)
        python3 setup.py sdist
esac


ls -lisah ./dist

mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz

ls -lisah ./dist
