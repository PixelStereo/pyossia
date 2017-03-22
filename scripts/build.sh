#!/bin/bash

# This is where all cmake variables are set
# This is where you can 

echo $OSTYPE
case OSTYPE in 
	darwin*)
	TRAVIS_OS_NAME=osx;;
	linux-gnu)
	TRAVIS_OS_NAME=linux;;
esac
echo $TRAVIS_OS_NAME
BUILD_TYPE=Debug
OSSIA_STATIC=1
TOXENV=py36
TRAVIS_OS_NAME=osx
TRAVIS_REPO_SLUG='PixelStereo/pyossia'
source travis/split_repo_slug.sh
export TOXENV
sh -x travis/build.sh
