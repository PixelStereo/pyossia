#!/bin/bash

if [[ ${TRAVIS_REPO_SLUG} =~ ([^,]+).*"/"([^,]+) ]]; then
    OWNER=${BASH_REMATCH[1]}
    REPO=${BASH_REMATCH[2]}
fi
echo $OWNER; echo $REPO
export OWNER
export REPO
