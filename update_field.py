import arcpy
import arcpy.da as da
import os

arcpy.env.overwriteOutput = True

gdb = "./datas/first/first.gdb"
pnt = f"{gdb}/pnt"
# 三个参数分别为要素类，字段列表， 过滤条件
with da.UpdateCursor(pnt, ["SHAPE@", 'lon', 'lat'], 'fid=2') as cur:  # type: ignore
    for row in cur:
        new_cod = [(118.8, 29.5), 111, 222]  # 要更新的字段列表
        cur.updateRow(new_cod)
