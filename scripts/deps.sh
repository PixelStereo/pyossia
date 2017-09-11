#!/bin/sh

set -v

case "$TRAVIS_OS_NAME" in
  linux)
    case "${TOXENV}" in
        py2)
          sudo apt-get -y install python python-setuptools
            ;;
        py3)
          sudo apt-get -y install python3 python3-setuptools
            ;;
    esac
  ;;
  osx)
    case "${TOXENV}" in
        py2)
          brew install python
          brew link --overwrite python
            ;;
        py3)
          brew install python3
          brew link --overwrite python3
            ;;
    esac
  ;;
esac

case "${TOXENV}" in
    py2)
        pip install sphinx_rtd_theme
        pip install coverage
        # install codacy tools
        pip install codacy-coverage
        # install to publish documentation from push or tag
        pip install travis-sphinx
        pip install -ve .
        ;;
    py3)
        pip3 install sphinx_rtd_theme
        pip3 install coverage
        # install codacy tools
        pip3 install codacy-coverage
        # install to publish documentation from push or tag
        pip3 install travis-sphinx
        pip3 install -ve .
    ;;
esac
