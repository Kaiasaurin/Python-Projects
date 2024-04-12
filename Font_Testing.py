import os
import tkinter as tk
from tkinter import filedialog, StringVar, OptionMenu
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageChops

# List to keep references to images
image_references = []

# Variable to store the selected directory
selected_directory = ""

# Variable to store the frame containing the images
image_frame = None

# Declare optionMenu as a global variable
optionMenu = None

# Declare text_entry as a global variable
text_entry = None

def initialize_ui(root):
    global selected_font, optionMenu, text_entry
    # Initialize selected_font after the root window is created
    selected_font = StringVar(value="Display All")

    frame = tk.Frame(root)
    frame.pack()

    # Text entry field
    text_entry = tk.Entry(frame)
    text_entry.pack(side=tk.LEFT)

    # Button to select directory
    select_dir_button = tk.Button(frame, text="Select Directory", command=select_directory)
    select_dir_button.pack(side=tk.LEFT)

    # Dropdown menu for selecting a font
    optionMenu = OptionMenu(frame, selected_font, *["Display All"])
    optionMenu.pack(side=tk.LEFT)

    # Button to submit and display fonts
    submit_button = tk.Button(frame, text="Submit", command=display_fonts)
    submit_button.pack(side=tk.LEFT)

def select_directory():
    global selected_directory
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        print("Directory selected:", selected_directory)
        update_font_options()
    else:
        print("No directory selected.")

def update_font_options():
    global selected_font
    # Clear the current options
    selected_font.set("Display All")
    # Populate the dropdown menu with the fonts found in the selected directory
    fonts = [f for f in os.listdir(selected_directory) if f.endswith(('.ttf', '.otf'))]
    fonts.insert(0, "Display All")
    optionMenu['menu'].delete(0, 'end')
    for font in fonts:
        optionMenu['menu'].add_command(label=font, command=tk._setit(selected_font, font))

def display_fonts():
    global image_frame
    if not selected_directory:
        print("Please select a directory first.")
        return
    text = text_entry.get()
    images = []
    if selected_font.get() == "Display All":
        # Display all fonts
        for filename in os.listdir(selected_directory):
            if filename.endswith(('.ttf', '.otf')):
                font_path = os.path.join(selected_directory, filename)
                try:
                    font = ImageFont.truetype(font_path, 30)
                    image = Image.new('RGB', (200, 200), color=(255, 255, 255))
                    draw = ImageDraw.Draw(image)
                    draw.text((10,10), text, font=font, fill=(0, 0, 0))
                    # Load Arial font for drawing the font name
                    arial_font = ImageFont.truetype("arial.ttf", 14)
                    # Draw the font name under the text in Arial
                    draw.text((10, 50), filename, font=arial_font, fill=(0, 0, 0))
                    # Trim the white space
                    bg = Image.new(image.mode, image.size, (255, 255, 255))
                    diff = ImageChops.difference(image, bg)
                    bbox = diff.getbbox()
                    if bbox:
                        image = image.crop(bbox)
                    photo = ImageTk.PhotoImage(image)
                    images.append(photo)
                    image_references.append(photo) # Keep a reference to the image
                except Exception as e:
                    print(f"Error with {filename}: {e}")
    else:
        # Display only the selected font
        font_path = os.path.join(selected_directory, selected_font.get())
        try:
            font = ImageFont.truetype(font_path, 30)
            image = Image.new('RGB', (200, 200), color=(255, 255, 255))
            draw = ImageDraw.Draw(image)
            draw.text((10,10), text, font=font, fill=(0, 0, 0))
            # Trim the white space
            bg = Image.new(image.mode, image.size, (255, 255, 255))
            diff = ImageChops.difference(image, bg)
            bbox = diff.getbbox()
            if bbox:
                image = image.crop(bbox)
            photo = ImageTk.PhotoImage(image)
            images.append(photo)
            image_references.append(photo) # Keep a reference to the image
        except Exception as e:
            print(f"Error with {selected_font.get()}: {e}")
    # Clear the previous images
    if image_frame is not None:
        for widget in image_frame.winfo_children():
            widget.destroy()
    # Create a new frame for the images if it doesn't exist
    if image_frame is None:
        image_frame = tk.Frame(root)
        image_frame.pack()
    # Display the new images
    for i, image in enumerate(images):
        label = tk.Label(image_frame, image=image)
        label.grid(row=i//3, column=i%3) # Use grid within the new frame

root = tk.Tk()
root.title("Font Viewer")

initialize_ui(root)

root.mainloop()
