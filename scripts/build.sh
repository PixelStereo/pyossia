#!/bin/bash

echo ''
echo ' ----- MAKE THE WHEEL, PLEASE ! ------'
echo ''

pip3 wheel -ve .

echo '------- WHERE IS THE WHEEL ?? ------'
ls
echo ''

if [ -n "$TRAVIS_TAG" ]
then
	pip3 install ${REPO}-${TRAVIS_TAG}
	mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz
fi
