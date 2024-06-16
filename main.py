import geopandas as gpd
import folium


def convert_timestamps_to_string(df, column: str):
    df["skapad"] = df["skapad"].astype(str)
    return df


def main():
    gdf = gpd.read_file("kartdata/vekt_100/mark_ln25/filtered_mark.gpkg")
    gdf = convert_timestamps_to_string(gdf, "skapad")
    m = folium.Map(location=(67.2236, 17.3254))
    folium.GeoJson(gdf).add_to(m)
    m.save("mark.html")


if __name__ == "__main__":
    main()
