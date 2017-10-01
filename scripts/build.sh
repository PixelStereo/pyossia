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
fi
