#!/bin/sh

set -v

case "$TRAVIS_OS_NAME" in
  linux)
    case "${TOXENV}" in
        py27)
          sudo apt-get -y install python python-setuptools libpython2.7
          pip install coverage
          # install codacy tools
          pip install codacy-coverage
          # install to publish documentation from push or tag
          pip install travis-sphinx
            ;;
        py34)
          sudo apt-get -y install python3 python3-setuptools libpython3.4 
            ;;
        py35)
          sudo apt-get -y install python3 python3-setuptools libpython3.5
            ;;
        py36)
          sudo apt-get -y install python3 python3-setuptools libpython3.6
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
