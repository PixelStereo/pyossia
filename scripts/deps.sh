#!/bin/sh

set -v

case "$TRAVIS_OS_NAME" in
    linux)
        sudo apt-get -y install python3 python3-setuptools
    ;;
    osx)
        brew install python3
        brew link --overwrite python3 wget unzip
    ;;
esac

case "$BUILD_TYPE" in
    DOCS)
        pip3 install sphinx_rtd_theme
        # install to publish documentation from push or tag
        pip3 install travis-sphinx
        pip3 install coverage
        # install codacy tools
        pip3 install codacy-coverage
    ;;
esac