#!/bin/sh

set -v

case "$TRAVIS_OS_NAME" in
  linux)
    case "${TOXENV}" in
        py27)
          sudo apt-get -y install python python-setuptools libpython2.7-dev 
            ;;
        py36)
          sudo apt-get -y install python3 python3-setuptools libpython3.6-dev 
            ;;
    esac
  ;;
  osx)
    case "${TOXENV}" in
        py27)
          brew install python
          brew link --overwrite python
            ;;
        py36)
          brew install python3
          brew link --overwrite python3
            ;;
    esac
  ;;
esac

echo python --version
echo python3 --version
echo pip --version
echo pip3 --version
