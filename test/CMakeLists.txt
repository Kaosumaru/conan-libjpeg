PROJECT(test)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(test test.cpp)

TARGET_LINK_LIBRARIES(test ${CONAN_LIBS})
