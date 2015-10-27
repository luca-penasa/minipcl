project(minipcl)
cmake_minimum_required(VERSION 2.8)
aux_source_directory(. SRC_LIST)
#add_executable(${PROJECT_NAME} ${SRC_LIST})

file(GLOB_RECURSE SRCS *.cpp )


find_package(Eigen3 REQUIRED)

include_directories(${EIGEN3_INCLUDE_DIR})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}
    "pcl/common/include"
    "pcl/io/include")



add_library(minipcl ${SRCS})

