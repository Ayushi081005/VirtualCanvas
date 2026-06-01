import numpy as np

def create_canvas(width=1280, height=720):
    # Create a white canvas with the specified width and height
    return np.ones((height, width, 3), dtype=np.uint8) * 255
