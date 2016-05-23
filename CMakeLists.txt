project(Gumbo)
cmake_minimum_required(VERSION 2.8.12)

file(GLOB GUMBO_SOURCES ${GUMBO_PRJ_DIR}/src/*.c)
add_library(gumbo ${GUMBO_SOURCES})
