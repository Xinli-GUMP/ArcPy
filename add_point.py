import arcpy
import random
import arcpy.da

# 定义地理数据库的路径
gdb = "./datas/first/first.gdb"
# 创建要素类的逻辑路径,在操作系统中，不需要寻找名为 pnt 的文件夹: 这些要素类的逻辑名称仅可以通过 ArcGIS 的 API 进行引用，并在需要时进行读取或编辑。
ftc_class = f"{gdb}/pnt"

if arcpy.Exists(ftc_class):
    print("feature class exists")
    # 使用Arcpy.da 可以搭配 with 关键字自动管理对象生命周期，并且性能更好
    with arcpy.da.InsertCursor(ftc_class, ["SHAPE@XY", "id", "lon", "lat"]) as cur:  # type: ignore
        for i in range(30):
            lon, lat = random.uniform(119, 121), random.uniform(29, 31)
            cod = arcpy.Point(lon, lat)
            # 这里cod本身已经包含了坐标信息，所以后续的字段可以存储坐标之外的字段信息，也剋额外存储坐标信息方便查询
            cur.insertRow([cod, i, lon, lat])

else:
    print("feature class not exists")
