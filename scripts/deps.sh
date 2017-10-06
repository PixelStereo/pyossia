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

pip3 install sphinx_rtd_theme
pip3 install coverage
# install codacy tools
pip3 install codacy-coverage
# install to publish documentation from push or tag
pip3 install travis-sphinx

# TODO : DO IT IN SETUP.PY
wget "https://github.com/OSSIA/libossia/releases/download/v1.0.0-b3/ossia-python-macos.zip"
unzip "ossia-python-macos.zip"
mv "ossia-python/ossia_python.cpython-36m-darwin.so" "pyossia/"
