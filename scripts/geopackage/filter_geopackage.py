import geopandas as gpd
from shapely.geometry import box


def filter_geopackage(
    fname: str,
    min_longitude: int,
    max_longitude: int,
    min_latitude: int,
    max_latitude: int,
    output_name: str,
) -> None:

    gdf = gpd.read_file(fname)
    # Create a bounding box polygon
    bbox = box(min_longitude, min_latitude, max_longitude, max_latitude)

    # Filter the GeoDataFrame using the bounding box
    filtered_gdf = gdf[gdf.intersects(bbox)]

    filtered_gdf.to_file(output_name, driver="GPKG")
