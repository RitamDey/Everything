cmake_minimum_required(VERSION 3.5)
project(single_linked)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -O3 -Ofast")

set(SOURCE_FILES lib/linked.h lib/linkedlist.c lib/pointer_sample.c lib/struct_sample.c main.c)
add_executable(single_linked ${SOURCE_FILES})