project(Gumbo)
cmake_minimum_required(VERSION 2.8.12)

option(BUILD_SHARED_LIBS "Set to ON to build SHARED libraries, default is OFF" OFF)

include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

file(GLOB GUMBO_SOURCES ${GUMBO_PRJ_DIR}/src/*.c)
add_library(gumbo ${GUMBO_SOURCES})
if(WIN32)
	target_include_directories(gumbo PRIVATE "${GUMBO_PRJ_DIR}/visualc/include")
endif()

#because gumbo is a pure C 99 library
set_property(TARGET gumbo PROPERTY C_STANDARD 99)
