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


case "$BUILD_TYPE" in
    DOCS)
		# build the documentation
		travis-sphinx -s docs/source build
		travis-sphinx deploy
    ;;
    COVERAGE)
        cd tests
		# codacy
		coverage run --omit ../pyossia/_version.py --omit ../versioneer.py  --include ../pyossia/* test_.py
		coverage xml
		coverage report -m
		python-codacy-coverage -r coverage.xml
		cd ../
    ;;
esac



