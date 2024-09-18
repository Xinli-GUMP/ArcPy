import arcpy
import os


# overwrite permitted
arcpy.env.overwriteOutput = True

path = "./datas/first"
if not os.path.exists(path):
    os.makedirs(path)

# create a geoddatabase
gdb = arcpy.CreateFileGDB_management(path, "first", out_version="10.0")

# create a featureclass
# 可以使用 EPSG 代码直接创建空间参考。例如，如果您想使用 WGS 84（EPSG:4326）
pnt = arcpy.CreateFeatureclass_management(
    gdb, "pnt", geometry_type="POINT", spatial_reference=arcpy.SpatialReference(4326)
)


# add fields
def add_or_update_field(ftc, f_name: str, f_type: str):
    fields = arcpy.ListFields(ftc, f_name, f_type)
    if fields:
        arcpy.DeleteField_management(ftc, f_name)
        arcpy.AddField_management(ftc, f_name, f_type)
    else:
        arcpy.AddField_management(ftc, f_name, f_type)


f_name = ["id", "lon", "lat"]
f_type = ["SHORT", "DOUBLE", "DOUBLE"]

for i, name in enumerate(f_name):
    add_or_update_field(pnt, name, f_type[i])
