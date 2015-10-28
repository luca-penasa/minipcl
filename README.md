# MINIPCL

**minipcl** is a highly reduced version of the [PCL](http::pointclouds.org) library.
It only includes code from `IO` and `COMMON` `PCL` modules, but with only a couple of depedencies:
- boost
- Eigen


**minipcl** is useful if you just use PCL for reading/saving PCD, PLY, OBJ, ... file formats. 
In fact  it allows you to load these formats into  `PCLPointCloud2` or `pcl::PointCloud<PointT>` objects. 
Then you can convert these objects to your type or to `Eigen` matrixes, or do whatever you need with the loaded data.

minipcl is generated by a really-raw python script which checkout last commis from PCL and then copy required files into the minipcl folder. 
You can run it like this (you dont really need to but...):

```bash
./generate.py
```

Notice that you will need python >= 3.2 for some specific functions to work.


