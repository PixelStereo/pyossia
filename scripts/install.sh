#!/bin/bash

source ../scripts/split_repo_slug.sh

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv
    brew update
    brew install wget boost

    case "${TOXENV}" in
        py27)
			brew install python
            ;;
        py35)
            brew install python3
            ;;
    esac
else
    sudo apt-get update
    sudo apt-get -o Dpkg::Options::='--force-confdef' --force-yes -fuy upgrade
    sudo apt-get install boost python



