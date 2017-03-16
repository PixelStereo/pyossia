#!/bin/bash

ls -lisah

case "${TOXENV}" in
    py27)
        sudo apt-get install python
        pip install git+https://github.com/{$OWNER}/{$REPO}/tree/{$TRAVIS_BRANCH}

        ;;
    py36)
        sudo apt-get install python3
        pip3 install git+https://github.com/$OWNER/$REPO/tree/$TRAVIS_BRANCH
        ;;
esac

ls -lisah
ls -lisah ./dist

zip ./dist/${REPO}_${TRAVIS_TAG}_$TRAVIS_OS_NAME.zip ${REPO}_${TRAVIS_TAG}
ls -lisah
cd ../
