def detect_undo_gesture(landmarks):
    """
    Detects Undo Gesture: Thumb + Pinky finger up, others down.
    Returns True if the gesture is detected.
    """
    if not landmarks or len(landmarks) < 21:
        return False

    # Thumb (tip 4), Pinky (tip 20)
    thumb_up = landmarks[4][1] < landmarks[3][1]  # x-axis for thumb
    pinky_up = landmarks[20][2] < landmarks[18][2]  # y-axis

    # Other fingers (Index, Middle, Ring) down
    index_down = landmarks[8][2] > landmarks[6][2]
    middle_down = landmarks[12][2] > landmarks[10][2]
    ring_down = landmarks[16][2] > landmarks[14][2]

    return thumb_up and pinky_up and index_down and middle_down and ring_down


def detect_redo_gesture(landmarks):
    """
    Detects Redo Gesture: Index, Middle, and Ring fingers up, others down.
    Returns True if the gesture is detected.
    """
    if not landmarks or len(landmarks) < 21:
        return False

    index_up = landmarks[8][2] < landmarks[6][2]
    middle_up = landmarks[12][2] < landmarks[10][2]
    ring_up = landmarks[16][2] < landmarks[14][2]

    # Thumb and Pinky down
    thumb_down = landmarks[4][1] > landmarks[3][1]  # x-axis for thumb
    pinky_down = landmarks[20][2] > landmarks[18][2]

    return index_up and middle_up and ring_up and thumb_down and pinky_down
