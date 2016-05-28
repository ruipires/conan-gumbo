project(Gumbo)
cmake_minimum_required(VERSION 2.8.12)

option(BUILD_SHARED_LIBS "Set to ON to build SHARED libraries, default is OFF" OFF)

file(GLOB GUMBO_SOURCES ${GUMBO_PRJ_DIR}/src/*.c)
add_library(gumbo ${GUMBO_SOURCES})

#because gumbo is a pure C 99 library
set_property(TARGET gumbo PROPERTY C_STANDARD 99)
