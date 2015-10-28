#include "minipcl.h"

#include <minipcl/PCLPointCloud2.h>
#include <minipcl/point_cloud.h>

#include <minipcl/auto_io.h>
#include <minipcl/auto_io.hpp>

int main(int argc, char ** argv)

{
    std::string fname = argv[1];

    pcl::PointCloud<pcl::PointXYZ> c1;


    pcl::PCLPointCloud2 cloud;

    pcl::io::load(fname, c1);

//    minipcl::loadPCDFile(fname, cloud);



    std::cout << cloud << std::endl;

    // save the cloud again
    pcl::io::save("out.pcd", c1, 6);



    return 1;
}
