#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv
    brew update
    brew install wget boost

    case "${TOXENV}" in
        py27)
			brew install python
            pip update
            ;;
        py35)
            brew install python3
            pip3 update
            ;;
    esac
else
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install boost
fi