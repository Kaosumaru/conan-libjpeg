PROJECT(testproj)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(testproj test.cpp)

TARGET_LINK_LIBRARIES(testproj ${CONAN_LIBS})
