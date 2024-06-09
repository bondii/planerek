from io import BytesIO
from matplotlib import pyplot as plt
from scripts.filter_geopackage import filter_geopackage
import geopandas as gpd


def main():
    # Load the GeoDataFrame

    gdf = gpd.read_file("kartdata/vekt_100/hojd_ln25/filtered_hojd.gpkg")

    fig, ax = plt.subplots()
    gdf.plot(ax=ax)

    plt.savefig("test.png", format="png")


if __name__ == "__main__":
    main()
