cmake_minimum_required(VERSION 3.18)
project(MyProject)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Add your project files here
add_executable(my_app main.cpp)
