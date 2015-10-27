#ifndef MINIPCL_H
#define MINIPCL_H

#include <string>
#include <Eigen/Geometry>

namespace pcl
{
    class PCLPointCloud2;
}

namespace minipcl
{

int
loadPCDFile (const std::string &file_name, pcl::PCLPointCloud2 &cloud);

int
savePCDFile (const std::string &file_name, const pcl::PCLPointCloud2 &cloud,
             const Eigen::Vector4f &origin = Eigen::Vector4f::Zero (),
             const Eigen::Quaternionf &orientation = Eigen::Quaternionf::Identity (),
             const bool binary_mode = false);


}

#endif // MINIPCL_H

