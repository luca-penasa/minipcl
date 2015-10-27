#include "minipcl.h"
#include <minipcl/pcd_io.h>

namespace minipcl
{
int
loadPCDFile (const std::string &file_name, pcl::PCLPointCloud2 &cloud)
{
    return pcl::io::loadPCDFile(file_name, cloud);
}

int
savePCDFile (const std::string &file_name,
             const pcl::PCLPointCloud2 &cloud,
             const Eigen::Vector4f &origin,
             const Eigen::Quaternionf &orientation,
             const bool binary_mode)
{
    return pcl::io::savePCDFile(file_name, cloud, origin, orientation, binary_mode);
}


}// end nspace
