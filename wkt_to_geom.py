import arcpy
import os
import arcpy.da as da


def wkt_to_geom(file: str, gdb: str, wkid: int):
    """convert wkt text to a new feature class
    Args:
        file (str): wkt file path
        gdb (str): the gdb which store new feature class
        WIKD (str): spatital_reference
    """
    # 映射字典，将 WKT 类型映射到 ArcGIS 的要素类类型
    wkt_to_feature_class_type = {
        # "POINT": "POINT",
        "MULTIPOINT": "MULTIPOINT",
        "MULTILINESTRING": "POLYLINE",
        "LINESTRING": "POLYLINE",
        "POLYGON": "POLYGON",
        "MULTIPOLYGON": "POLYGON",
    }
    # get feature calss type and wtk info
    with open(file, "r")      as f:
        lines = f.readlines()
        ftc_type = wkt_to_feature_class_type[lines[0][0: lines[0].find(" ")]]

    # create new feature class
    ftc = arcpy.CreateFeatureclass_management(
        out_path=gdb,
        out_name=f"my_{ftc_type}",
        geometry_type=ftc_type,
        spatial_reference=arcpy.SpatialReference(wkid))

    # fill geomtry info fom wkt
    with da.InsertCursor(ftc, ["SHAPE@"]) as cur:  # type: ignore
        for line in lines:
            geom = arcpy.FromWKT(line)
            cur.insertRow([geom])


if __name__ == "__main__":
    folder = "./datas/first"
    gdb = f"{folder}/second.gdb"
    if not arcpy.Exists(gdb):
        arcpy.CreateFileGDB_management(f"{folder}", "second")
    wkt_list = [
        f"{folder}/{file}" for file in os.listdir(folder) if file.endswith(".txt")]
    wkid = 4326

    for file in wkt_list:
        wkt_to_geom(file, gdb, wkid)
