import cv2
import config

# To keep track of drawing actions
draw_history = []
redo_stack = []

def draw_shape(img, shape, color, start, end, thickness=None):
    if thickness is None:
        thickness = config.BRUSH_THICKNESS

    if shape == "line":
        cv2.line(img, start, end, color, thickness)
    elif shape == "rectangle":
        cv2.rectangle(img, start, end, color, thickness)
    elif shape == "square":
        side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        end = (start[0] + side, start[1] + side)
        cv2.rectangle(img, start, end, color, thickness)
    elif shape == "circle":
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        cv2.circle(img, start, radius, color, thickness)

def add_to_history(shape, color, start, end, thickness=None):
    draw_history.append((shape, color, start, end, thickness))
    redo_stack.clear()

def undo(canvas):
    if draw_history:
        redo_stack.append(draw_history.pop())
        redraw(canvas)

def redo(canvas):
    if redo_stack:
        draw_history.append(redo_stack.pop())
        redraw(canvas)

def redraw(canvas):
    canvas[:] = config.COLORS["white"]
    for shape, color, start, end, thickness in draw_history:
        draw_shape(canvas, shape, color, start, end, thickness)
