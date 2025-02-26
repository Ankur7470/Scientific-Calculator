cmake_minimum_required(VERSION 3.10)
project(ScientificCalculator)

# Set C standard
set(CMAKE_C_STANDARD 99)

# Add executable
add_executable(calculator calculator.c)

# Link math library
target_link_libraries(calculator m)