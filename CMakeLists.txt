project(minipcl)
cmake_minimum_required(VERSION 2.8)
aux_source_directory(. SRC_LIST)


file  (GLOB_RECURSE SRCS "minipcl/*.cpp")
file  (GLOB_RECURSE HEADS "minipcl/*.h")
file  (GLOB_RECURSE IMPLS "minipcl/*.hpp")

#file(GLOB PLY_SRCS "minipcl/ply/*.cpp")
#file(GLOB PLY_HEADS "minipcl/ply/*.h")

find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})

find_package(Boost COMPONENTS system filesystem iostreams REQUIRED)
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIR})


include_directories(${CMAKE_CURRENT_SOURCE_DIR}/minipcl)


add_library(minipcl ${SRCS} ${HEADS} ${IMPLS})


export(TARGETS minipcl FILE minipcl_exports.cmake)


#################### tools and examples, off by default ###########
option (MINIPCL_BUILD_EXAMPLE "build an example" OFF )

    if (MINIPCL_BUILD_EXAMPLE)
    add_executable(use_minipcl use_minipcl.cpp)
    target_link_libraries(use_minipcl
      ${Boost_FILESYSTEM_LIBRARY}
      ${Boost_SYSTEM_LIBRARY}
      ${Boost_IOSTREAMS_LIBRARY}
        minipcl
    )

endif()









