#!/bin/bash

# Set up Conan profile
conan profile new default --detect || conan profile update settings.compiler.libcxx=libstdc++11 default

# Install dependencies
conan install . --build=missing -e=CONAN_CMAKE_PROGRAM=$(which cmake)

# Configure and build the project
cmake -G "Ninja" .
cmake --build .
