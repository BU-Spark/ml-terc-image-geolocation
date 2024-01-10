# ChatGPT-4 Prompt: 
# Write python code to derive the field of view in degrees and scene width and height in kilometers
# given lens focal length in millimeters, sensor width and height dimensions in millimeters and distance
# from camera to subject in kilometers.

# ChatGPT-4 Generated Code in Response

import math

def calculate_fov_and_scene_dimensions(focal_length, sensor_width, sensor_height, distance):
    # Calculate Field of View (FoV) in degrees
    fov_horizontal = 2 * math.degrees(math.atan(sensor_width / (2 * focal_length)))
    fov_vertical = 2 * math.degrees(math.atan(sensor_height / (2 * focal_length)))

    # Calculate scene dimensions in kilometers
    scene_width = 2 * distance * math.tan(math.radians(fov_horizontal) / 2)
    scene_height = 2 * distance * math.tan(math.radians(fov_vertical) / 2)

    return fov_horizontal, fov_vertical, scene_width, scene_height

# Example usage: These correspond to a Nikon D5
focal_length = 80  # in millimeters
sensor_width = 36  # in millimeters (for a full-frame sensor like Nikon D5)
sensor_height = 24  # in millimeters

# Distance of the ISS camera to earth
distance = 414.6891  # in kilometers

fov_horizontal, fov_vertical, scene_width, scene_height = calculate_fov_and_scene_dimensions(focal_length, sensor_width, sensor_height, distance)

print(f"FoV (horizontal): {fov_horizontal:.2f}°")
print(f"FoV (vertical): {fov_vertical:.2f}°")
print(f"Scene width: {scene_width:.2f} km")
print(f"Scene height: {scene_height:.2f} km")
