import arcpy
import arcpy.management
import arcpy.sa

arcpy.env.overwriteOutput = True
dem = arcpy.Raster('./datas/jj25w/dem_prj.tif')
# 处理 NoData 值
arcpy.management.SetRasterProperties(dem, nodata="1 0")
# 重加载一下
dem = arcpy.Raster(dem)
dem.save('./datas/jj25w/dem_prj.tif')
arr = arcpy.RasterToNumPyArray(dem, nodata_to_value=0)
print(arr.min())
print(arr.max())
# 将每个像元值都扩大5倍
new_arr = arr * 5
new_dem = arcpy.NumPyArrayToRaster(new_arr, arcpy.Point(
    dem.extent.XMin, dem.extent.YMin), dem.meanCellWidth, dem.meanCellHeight)
new_dem = arcpy.Raster(arcpy.DefineProjection_management(new_dem, 3827))
arcpy.management.SetRasterProperties(new_dem, nodata="1 0")
new_dem = arcpy.Raster(new_dem)
new_dem.save('./datas/jj25w/streth_dem.tif')
