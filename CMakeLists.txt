project(minipcl)
cmake_minimum_required(VERSION 2.8)
aux_source_directory(. SRC_LIST)
add_executable(use_minipcl use_minipcl.cpp)

#file(GLOB_RECURSE SRCS *.cpp )
set (SRCS "pcl/io/src/pcd_io.cpp"
            "pcl/common/src/print.cpp"
"pcl/io/src/lzf.cpp")

find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})




find_package(Boost COMPONENTS system filesystem REQUIRED)
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIR})


include_directories(${CMAKE_CURRENT_SOURCE_DIR}
    "pcl/common/include"
    "pcl/io/include")



add_library(minipcl ${SRCS})

target_link_libraries(use_minipcl
  ${Boost_FILESYSTEM_LIBRARY}
  ${Boost_SYSTEM_LIBRARY}
    minipcl
)






