import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("✅ Command received:", command)
        return command
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition service.")
        return ""

def parse(command):
    colors = ["red", "green", "blue", "pink", "yellow", "black", "white"]
    shapes = ["circle", "rectangle", "square", "line"]

    # Check for control commands
    if "erase" in command or "eraser" in command:
        return "eraser", None
    elif "clear" in command:
        return "clear", None
    elif "undo" in command:
        return "undo", None
    elif "redo" in command:
        return "redo", None

    # Check for shape and color
    selected_color = next((c for c in colors if c in command), None)
    selected_shape = next((s for s in shapes if s in command), None)

    if selected_shape:
        print(f"🟢 Shape: {selected_shape}, Color: {selected_color or 'default'}")
    elif selected_color:
        print(f"🎨 Color change: {selected_color}")

    return selected_shape, selected_color
