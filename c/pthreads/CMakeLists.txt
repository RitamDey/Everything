cmake_minimum_required(VERSION 3.6)
project(pthreads)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11 -l pthread -Wall")


set(SOURCE_FILES stack/stack.c stack/stack.h producer_consumer.c)
add_executable(pthreads ${SOURCE_FILES})