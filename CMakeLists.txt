cmake_minimum_required(VERSION 3.13.0)
project(py_libsudoku)

add_subdirectory(pybind11)
add_subdirectory(libsudoku)

include_directories(libsudoku/src)

# https://pybind11.readthedocs.io/en/stable/compiling.html#building-with-cmake
pybind11_add_module(py_libsudoku src/py_libsudoku.cpp)
target_link_libraries(py_libsudoku PRIVATE libsudoku_objs)
set_target_properties(py_libsudoku 
    PROPERTIES 
      OUTPUT_NAME "py_libsudoku"
)

