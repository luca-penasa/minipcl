#include "minipcl.h"

#include <pcl/PCLPointCloud2.h>
#include <pcl/point_cloud.h>
#include <pcl/conversions.h>

#include <pcl/io/auto_io.h>
#include <pcl/io/impl/auto_io.hpp>

int main(int argc, char ** argv)

{
    std::string fname = argv[1];

    pcl::PointCloud<pcl::PointXYZ> c1;

    pcl::io::load(fname, c1);

//    std::cout << cloud << std::endl;
    pcl::PCLPointCloud2 cloud;

    pcl::toPCLPointCloud2(c1, cloud);
    // save the cloud again
    pcl::io::save("out.pcd", cloud, 6);



    return 1;
}
