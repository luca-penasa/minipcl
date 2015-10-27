set(SUBSYS_NAME io)
set(SUBSYS_DESC "Point cloud IO library")
set(SUBSYS_DEPS common)

set(build TRUE)
PCL_SUBSYS_OPTION(build "${SUBSYS_NAME}" "${SUBSYS_DESC}" ON)

PCL_SUBSYS_DEPEND(build "${SUBSYS_NAME}" DEPS ${SUBSYS_DEPS} )


PCL_ADD_DOC("${SUBSYS_NAME}")

if(build)

    source_group("Image Headers" FILES ${IMAGE_INCLUDES})
    source_group("Image Sources" FILES ${IMAGE_SOURCES})

    set(PLY_SOURCES src/ply/ply_parser.cpp)
    set(PLY_INCLUDES
        "include/pcl/${SUBSYS_NAME}/ply/byte_order.h"
        "include/pcl/${SUBSYS_NAME}/ply/io_operators.h"
        "include/pcl/${SUBSYS_NAME}/ply/ply.h"
        "include/pcl/${SUBSYS_NAME}/ply/ply_parser.h"
       )
    PCL_ADD_LIBRARY(pcl_io_ply "${SUBSYS_NAME}" ${PLY_SOURCES} ${PLY_INCLUDES})
    PCL_ADD_INCLUDES("${SUBSYS_NAME}" "${SUBSYS_NAME}/ply" ${PLY_INCLUDES})

    set(srcs
        src/debayer.cpp
#        src/pcd_grabber.cpp
        src/pcd_io.cpp
        src/vtk_io.cpp
        src/ply_io.cpp
        src/ascii_io.cpp
#        src/compression.cpp
        src/lzf.cpp
        src/lzf_image_io.cpp
        src/obj_io.cpp
        src/ifs_io.cpp
#        src/image_grabber.cpp
#        src/hdl_grabber.cpp
#        src/robot_eye_grabber.cpp
        src/file_io.cpp
        src/auto_io.cpp
        src/io_exception.cpp

        )



    set(incs
        "include/pcl/${SUBSYS_NAME}/boost.h"
        "include/pcl/${SUBSYS_NAME}/eigen.h"
        "include/pcl/${SUBSYS_NAME}/debayer.h"
        "include/pcl/${SUBSYS_NAME}/file_io.h"
        "include/pcl/${SUBSYS_NAME}/auto_io.h"
        "include/pcl/${SUBSYS_NAME}/lzf.h"
        "include/pcl/${SUBSYS_NAME}/lzf_image_io.h"
        "include/pcl/${SUBSYS_NAME}/io.h"
        "include/pcl/${SUBSYS_NAME}/grabber.h"
        "include/pcl/${SUBSYS_NAME}/file_grabber.h"
#        "include/pcl/${SUBSYS_NAME}/pcd_grabber.h"
        "include/pcl/${SUBSYS_NAME}/pcd_io.h"
        "include/pcl/${SUBSYS_NAME}/vtk_io.h"
        "include/pcl/${SUBSYS_NAME}/ply_io.h"
        "include/pcl/${SUBSYS_NAME}/tar.h"
        "include/pcl/${SUBSYS_NAME}/obj_io.h"
        "include/pcl/${SUBSYS_NAME}/ascii_io.h"
        "include/pcl/${SUBSYS_NAME}/ifs_io.h"
        "include/pcl/${SUBSYS_NAME}/point_cloud_image_extractors.h"
        "include/pcl/${SUBSYS_NAME}/io_exception.h"

        )



    set(impl_incs
        "include/pcl/${SUBSYS_NAME}/impl/pcd_io.hpp"
        "include/pcl/${SUBSYS_NAME}/impl/auto_io.hpp"
        "include/pcl/${SUBSYS_NAME}/impl/lzf_image_io.hpp"
        "include/pcl/${SUBSYS_NAME}/impl/synchronized_queue.hpp"
        "include/pcl/${SUBSYS_NAME}/impl/point_cloud_image_extractors.hpp"
        include/pcl/compression/impl/entropy_range_coder.hpp
        include/pcl/compression/impl/octree_pointcloud_compression.hpp
       )
    if(PNG_FOUND AND (WITH_OPENNI OR WITH_OPENNI2))
     list(APPEND impl_incs
         include/pcl/compression/impl/organized_pointcloud_compression.hpp
        )
    endif()

    set(LIB_NAME "pcl_${SUBSYS_NAME}")

    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/include")
    add_definitions(${VTK_DEFINES})
    PCL_ADD_LIBRARY("${LIB_NAME}" "${SUBSYS_NAME}" ${srcs} ${incs} ${compression_incs} ${impl_incs})
#    link_directories(${VTK_LINK_DIRECTORIES})
    target_link_libraries("${LIB_NAME}" pcl_common pcl_io_ply )


    PCL_MAKE_PKGCONFIG("${LIB_NAME}" "${SUBSYS_NAME}" "${SUBSYS_DESC}"
      "${SUBSYS_DEPS}" "${EXT_DEPS}" "" "" "")

    # Install include files
    PCL_ADD_INCLUDES("${SUBSYS_NAME}" "${SUBSYS_NAME}" ${incs})
    PCL_ADD_INCLUDES("${SUBSYS_NAME}" compression ${compression_incs})
    PCL_ADD_INCLUDES("${SUBSYS_NAME}" "${SUBSYS_NAME}/openni_camera" ${OPENNI_INCLUDES})
    PCL_ADD_INCLUDES("${SUBSYS_NAME}" "${SUBSYS_NAME}/openni2" ${OPENNI2_INCLUDES})
    PCL_ADD_INCLUDES("${SUBSYS_NAME}" "${SUBSYS_NAME}/impl" ${impl_incs})

    if(BUILD_tools)
        add_subdirectory(tools)
    endif(BUILD_tools)

endif(build)
