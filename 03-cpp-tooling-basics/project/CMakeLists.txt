cmake_minimum_required(VERSION 3.16)
project(cpp_tooling_basics CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(calculator src/calculator.cpp)
target_include_directories(calculator PUBLIC src)

add_executable(calculator_app src/main.cpp)
target_link_libraries(calculator_app PRIVATE calculator)

option(BUILD_TESTING "Build the test suite" ON)
if(BUILD_TESTING)
  enable_testing()
  add_subdirectory(tests)
endif()
