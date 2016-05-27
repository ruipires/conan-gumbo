project(ConanGumboTest)
cmake_minimum_required(VERSION 2.8.12)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/build/conanbuildinfo.cmake) #Clion, with conanbuildinfo.cmake in build folder
    include(${CMAKE_CURRENT_SOURCE_DIR}/build/conanbuildinfo.cmake)
else()
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # Not CLion
endif()

conan_basic_setup()

add_executable(gumbotest src/main.cpp)
target_include_directories(gumbotest PRIVATE ${CONAN_INCLUDE_DIRS})
link_directories(${CONAN_LIB_DIRS})
target_link_libraries(gumbotest ${CONAN_LIBS})
