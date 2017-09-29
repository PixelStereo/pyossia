#!/bin/bash

echo ''
echo '-------------------------------------'
echo ' ----- MAKE THE WHEEL !!!!!!!! ------'
echo ''


echo ' WHO IS THERE NOW ??????'
echo ''
ls
echo ''
ls pyossia
echo ''

case "${TOXENV}" in
    py2)
        pip install -ve .
        python setup.py sdist
        ;;
    py3)
        pip3 install -ve .
        python3 setup.py sdist
        ;;
esac

if [ -n "$TRAVIS_TAG" ];
	mv ./dist/${REPO}-${TRAVIS_TAG}.tar.gz ./dist/${REPO}-${TRAVIS_TAG}_${TOXENV}_${TRAVIS_OS_NAME}.tar.gz;
fi
