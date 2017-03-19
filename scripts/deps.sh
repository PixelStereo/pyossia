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

case "${TOXENV}" in
    py27)
      python --version
      pip --version
        ;;
    py36)
      python3 --version
      pip3 --version
        ;;
esac


case "$TRAVIS_OS_NAME" in
  linux)
  CMAKE_URL="http://www.cmake.org/files/v3.5/cmake-3.5.0-Linux-x86_64.tar.gz"
  wget ${CMAKE_URL} --no-check-certificate
  mkdir cmake
  tar -xzf cmake-3.5.0-Linux-x86_64.tar.gz -C cmake --strip-components=1
  cd cmake
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