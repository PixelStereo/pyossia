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

if [[ "${TRAVIS_OS_NAME}" in linux ]]; then
  CMAKE_URL="https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz"
  mkdir cmake && travis_retry wget --no-check-certificate --quiet -O - ${CMAKE_URL} | tar --strip-components=1 -xz -C cmake
  export PATH=${DEPS_DIR}/cmake/bin:${PATH}
else
  brew upgrade cmake || brew install cmake
fi
cmake --version