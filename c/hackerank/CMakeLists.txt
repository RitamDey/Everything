cmake_minimum_required(VERSION 3.6)
project(hackerank)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11 -l pthread -Wall")


set(SOURCE_FILES ds/list.c sorted_list_insert.c)
add_executable(pthreads ${SOURCE_FILES})