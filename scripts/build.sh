#!/bin/bash

echo ''
echo ' ----- MAKE THE WHEEL, PLEASE ! ------'
echo ''

pip3 install -ve .
python3 setup.py sdist

if [ -n "$TRAVIS_TAG" ]
then
	mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz
fi
