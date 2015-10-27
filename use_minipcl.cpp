#include "pcl/io/pcd_io.h"

int main(int argc, char ** argv)

{
    std::string fname = argv[1];

    pcl::PCDReader r;

    pcl::PCLPointCloud2 cloud;
    r.read(fname, cloud);

    std::cout << cloud << std::endl;

    // save the cloud again
    pcl::PCDWriter w;
    w.writeBinaryCompressed("out.pcd", cloud);


    return 1;
}
