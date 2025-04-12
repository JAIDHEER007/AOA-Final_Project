# Python Program to Visualize a Quad Tree Insertion process using Video

import make_video
from helper import generate_random_points, load_points_from_geojson
import os

# all_points = generate_random_points(
#     x = 100,
#     x_range = (-100, 100), 
#     y_range = (-100, 100)
# )

geojson_file = os.path.join("..", "gis_data", "fastfood.geojson")
all_points = load_points_from_geojson(geojson_file)
save_path = make_video.visualize_insertion(
    points = all_points, 
    capacity = 4, 
    fps = 5, 
    max_frames_in_memory = 100
)

print("Saved at", save_path)
