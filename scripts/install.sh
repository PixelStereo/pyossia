#!/bin/bash

case "$TRAVIS_OS_NAME" in
  linux)
    sudo wget https://github.com/OSSIA/iscore-sdk/releases/download/6.0-osx/boost_1_63_0.tar.bz2 -O /opt/boost.tar.bz2 &
    
    wget https://cmake.org/files/v3.8/cmake-3.8.0-rc1-Linux-x86_64.tar.gz -O cmake-linux.tgz &
    
    echo 'deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty-4.0 main' | sudo tee /etc/apt/sources.list.d/llvm.list
    sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 1397BC53640DB551
    sudo add-apt-repository --yes ppa:ubuntu-toolchain-r/test
    sudo add-apt-repository --yes ppa:beineri/opt-qt58-trusty
#    sudo add-apt-repository --yes ppa:jonathonf/gcc-6.3
    sudo apt-get update -qq
    sudo apt-get install -qq --yes --force-yes g++-6 binutils ninja-build gcovr lcov qt58-meta-minimal libasound2-dev clang-4.0 lld-4.0

    wait wget || true
    
    (cd /opt; sudo tar xaf boost.tar.bz2; sudo mv boost_* boost ; sudo chmod -R a+rwx boost)

    tar xaf cmake-linux.tgz
    mv cmake-*-x86_64 cmake
  ;;
  osx)
    # work around a homebrew bug
    set +e
    brew install gnu-tar xz
    ARCHIVE=homebrew-cache.tar.xz
    wget "https://github.com/OSSIA/iscore-sdk/releases/download/6.0-osx/$ARCHIVE" -O "$ARCHIVE"
    gtar xhzf "$ARCHIVE" --directory /usr/local/Cellar
    brew link --force boost cmake ninja qt5

    set -e
  ;;
esac
