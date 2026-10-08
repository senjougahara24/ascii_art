import tkinter as tk
from PIL import Image


# Assigning ASCII characters based on brightness
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image_path, new_width=40):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Resizing
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.45)
    image = image.resize((new_width, new_height))

    # Converse to black and white
    image = image.convert("L")

    # Converse pixel data to ASCII character
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]

    # Add line breaks to fit the width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    lines = 0
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i+new_width] + "\n"
        lines += 1

    show_in_window(ascii_img, new_width, lines)

def show_in_window(ascii_art, window_width, window_height):
    root = tk.Tk()
    root.title("ASCII Art Viewer")

    text_widget = tk.Text(root, font=("Consolas", 8), bg = "black", fg = "white")
    text_widget.pack(expand=True, fill="both")

    text_widget.insert("1.0", ascii_art)

    text_widget.config(width=window_width, height=window_height)
    root.mainloop()

image_to_ascii("febi_chubi.png", new_width=120)