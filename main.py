from scripts.calculate_route import calculate_route
import geopandas as gpd
import matplotlib.pyplot as plt
from io import BytesIO


def main():

    # calculate_route(start_id="EC_1", end_id="AB_2")
    gdf = gpd.read_file("kartdata/vekt_100/hojd_ln25/hojd_ln25.gpkg")

    fig, ax = plt.subplots()
    gdf.plot(ax=ax)

    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format="png")
    plt.close(fig)
    img_bytes.seek(0)


if __name__ == "__main__":
    main()
