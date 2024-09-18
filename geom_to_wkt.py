import arcpy
import arcpy.da as da

arcpy.env.overwriteOutput = True
folder = "./datas/first"

gdb = f"{folder}/first.gdb"

pnt = f"{gdb}/pnt"
ply = f"{gdb}/ply"
plg = f"{gdb}/plg"
data_list = [pnt, ply, plg]


# read wkt
def geom_to_wkt(fct, file) -> None:
    with open(file, "w", encoding="utf8") as f:
        with da.SearchCursor(fct, ["SHAPE@WKT"]) as cur:  # type: ignore
            for row in cur:
                # row[index] 指的是["SHAPE@WTK"...]
                f.write(f"{row[0]}\n")


# 不使用 with
# cur = da.SearchCursor(fct, ["SHAPE@WKT"])
# try:
#     for row in cur:
#         f.write(f"{row[0]}\n")
# finally:
#     del cur  # 手动关闭游标

for data in data_list:
    geom_to_wkt(data, f"{data.replace('first.gdb/','')}.txt")
