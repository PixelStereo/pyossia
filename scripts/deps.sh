#!/bin/sh

set -v

case "$TRAVIS_OS_NAME" in
  linux)
    case "${TOXENV}" in
        py27)
          sudo apt-get -y install python python-setuptools libpython2.7-dev 
            ;;
        py34)
          sudo apt-get -y install python3 python3-setuptools libpython3.4-dev 
            ;;
        py35)
          sudo apt-get -y install python3 python3-setuptools libpython3.5-dev 
            ;;
        py36)
          sudo apt-get -y install python3 python3-setuptools libpython3.6-dev 
            ;;
    esac
    sudo apt-get -y install libboost-all-dev
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


case "$TRAVIS_OS_NAME" in
  linux)
  CMAKE_URL="https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz"
  wget ${CMAKE_URL} --no-check-certificate
  mkdir cmake
  tar -xzf cmake-3.7.2.tar.gz -C cmake --strip-components=1
  ./configure
  make
  sudo make install
  export PATH=/usr/local/bin:$PATH
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

  cmake --version



;;
  osx)
  brew upgrade cmake || brew install cmake
;;
esac

cmake --version
which cmake