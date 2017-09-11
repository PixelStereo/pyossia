#!/bin/sh

set -v

case "$TRAVIS_OS_NAME" in
  linux)
    case "${TOXENV}" in
        py27)
          sudo apt-get -y install python python-setuptools
          pip install coverage
          # install codacy tools
          pip install codacy-coverage
          # install to publish documentation from push or tag
          pip install travis-sphinx
            ;;
        py34)
          sudo apt-get -y install python3 python3-setuptools
            ;;
        py35)
          sudo apt-get -y install python3 python3-setuptools
            ;;
        py36)
          sudo apt-get -y install python3 python3-setuptools
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

case "${TOXENV}" in
    py27)
		pip install -ve .
		;;
	py34)
		pip3 install -ve .
		;;
	py35)
		pip3 install -ve .
		;;
	py36)
		pip3 install -ve .
    ;;
esac