# Colors
COLORS = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
    "pink": (255, 0, 255),
    "yellow": (0, 255, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

# Shapes
SHAPES = ["circle", "rectangle", "square", "line"]

# Frame/Canvas settings
FRAME_WIDTH = 1280   # Default webcam frame width
FRAME_HEIGHT = 720   # Default webcam frame height
CANVAS_COLOR = COLORS["white"]  # Background color of the canvas

# Default brush/eraser sizes
BRUSH_THICKNESS = 5
ERASER_THICKNESS = 50

# Current sizes (modifiable at runtime via voice or key)
CURRENT_BRUSH_THICKNESS = BRUSH_THICKNESS
CURRENT_ERASER_THICKNESS = ERASER_THICKNESS

# Available brush sizes for voice commands
BRUSH_SIZES = {
    "thin": 2,
    "medium": 10,
    "thick": 20,
    "very thick": 40
}

# Canvas brush settings used in main drawing
BRUSH_RADIUS = CURRENT_BRUSH_THICKNESS
BRUSH_COLOR = COLORS["green"]  # Default brush color

