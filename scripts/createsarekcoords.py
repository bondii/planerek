import numpy as np
import os

import csv


def read_xyz_data(path):
    """
    Read an xyz file and extract the molecule's geometry.

    The file should be in the format::

        num_atoms
        comment
        ele0 x0 y0 z0
        ele1 x1 y1 z1
        ...

    Parameters
    ----------
    path : str
        A path to a file to read

    Returns
    -------
    val : LazyValues
        An object storing all the data
    """
    coords = []
    with open(path, "r") as f:
        for i, line in enumerate(f):
            east, north, ele = line.strip().split()
            point = [
                float(east.replace(",", ".")),
                float(north.replace(",", ".")),
                float(ele.replace(",", ".")),
            ]  # kanske int??
            if (593088 < point[0] < 651840) and (7426848 < point[1] < 7503584):
                coords.append([east, north, ele])

    return coords


hojdpath = r"C:\Users\jesbr8\Desktop\Ny mapp\sarekplaneringsmjukvara\höjddata"
hojddata = ["74_5", "74_6", "75_5", "75_6"]
coords = []
for h in hojddata:
    c = read_xyz_data(os.path.join(hojdpath, h, h + ".xyz"))

    coords.extend(c)


with open("sarekcoords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for i in range(0, np.shape(coords)[0]):
        writer.writerow(coords[i])

    f.close()
