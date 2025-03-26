from helper import *
from quad_tree import *
from testdata import *
import os

def main():
    # Load points from GeoJSON
    geojson_file = os.path.join("..", "gis_data", "export.geojson")
    all_points = load_points_from_geojson(geojson_file)

    boundary = calculate_boundary_from_geojson(all_points)

    print(boundary)

    qt1 = QuadTree(
        center = boundary[0], 
        width = boundary[1], 
        height = boundary[2],
        capacity = 4
    )

    inserted = 0
    for pt in all_points:
        if qt1.insert(pt):
            inserted += 1

    
    visualize(qt1, xsize = 10, ysize = 10)


if __name__ == '__main__':
    main()

