import arcpy

arcpy.env.overwriteOutput = True

dem = './datas/jj25w/dem_jxk250wgs84.tif'

dem_raster = arcpy.Raster(dem)
# print(dem_raster.spatialReference.type)  # 获取空间参考系, Geographic 代表尚未进行投影

# 处理栅格数据前最好先转换成投影坐标系，统一空间单位为米
# 'in_memory' 是ArcPy提供的一种便捷语法，可以将对象临时存储在内存中
# wkid 3857是等角切圆柱投影(web墨卡托)
if dem_raster.spatialReference.type == 'Geographic':
    dem_raster = arcpy.Raster(arcpy.ProjectRaster_management(
        dem_raster, out_raster='in_memory/dem_prj', out_coor_system=3857))

# dem_raster.save("./datas/jj25w/dem_prj.tif")

slope = arcpy.Raster(arcpy.Slope_3d(dem_raster, "in_memory/slope_t", z_unit='METER'))

# slope.save("./datas/jj25w/dem_slope.tif")

re_slope = arcpy.Raster(arcpy.Reclassify_3d(slope, 'Value', f'{slope.minimum} 2 5; 2.0001 8 4; 8.0001 15 3; 15.0001 25 2; 25.0001 {slope.maximum} 1', 'in_memory/re_slope', 'NoData'))

re_slope.save("./datas/jj25w/re_slope.tif")
