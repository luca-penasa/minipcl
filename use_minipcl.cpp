#include "minipcl.h"

#include <minipcl/PCLPointCloud2.h>

int main(int argc, char ** argv)

{
    std::string fname = argv[1];



    pcl::PCLPointCloud2 cloud;
    minipcl::loadPCDFile(fname, cloud);

    std::cout << cloud << std::endl;

    // save the cloud again
    minipcl::savePCDFile("out.pcd", cloud);



    return 1;
}
