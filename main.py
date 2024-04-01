from tkinter import Tk, filedialog, Canvas
from PIL import Image, ImageTk
import customtkinter

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")   

# App Frame
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Kerbbonize")

# App Grid
app.rowconfigure((0,1,2), weight=1)                    
app.columnconfigure((0,1,2,3), weight=1)



def select_image():
    
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        print("Selected file:", file_path)  # For testing purposes, you can replace this with image loading code
        display_image(file_path)

def display_image(file_path):
    global image, tk_image
    image = Image.open(file_path)
    image.thumbnail((600, 600))  # Resize image to fit canvas
    tk_image = ImageTk.PhotoImage(image)    
    canvas.create_image(canvas.winfo_width() //2, canvas.winfo_height() // 2, anchor="center", image=tk_image)
    canvas.image = tk_image  # Keep reference to avoid garbage collection

def get_pixel_color(event):
    x, y = event.x, event.y
    if 0 <= x < image.width and 0 <= y < image.height:
        pixel_color = image.getpixel((x, y))
        print("Pixel color at ({}, {}): {}".format(x, y, pixel_color))
        make_transparent(pixel_color)

def make_transparent(pixel_color):
    print("Changing all instances with color {} to transparent".format(pixel_color))
    transparent_color = (0, 0, 0, 0)  # RGBA Format
    target_color = pixel_color

    width, height = image.size

    # tolerance from RGB values (0-255)
    tolerance = 120

    # get RGB from RGBA
    tr, tg, tb = target_color[:3]

    for i in range(width):
        for j in range(height):
            try:
                cr, cg, cb, _ = image.getpixel((i, j))  # pixel color at (i, j) with format RGBA
            except ValueError:
                # If the image doesn't have an alpha channel, assume alpha value of 255 (fully opaque)
                cr, cg, cb = image.getpixel((i, j))[:3]

            if (abs(cr - tr) <= tolerance and abs(cg - tg) <= tolerance and abs(cb - tb) <= tolerance):
                image.putpixel((i, j), transparent_color)  # change if pixel color is within tolerance

    # Update displayed image
    canvas.delete("all")
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(canvas.winfo_width() //2, canvas.winfo_height() // 2, anchor="center", image=tk_image)
    canvas.image = tk_image

def download_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path, format="PNG")
        print("Image saved as: ", file_path)

#Control Frame
frame_control = customtkinter.CTkFrame(app, corner_radius=0)
frame_control.grid(row=0, column=0, rowspan=3, sticky="nsew")

# Image Canvas
canvas = customtkinter.CTkCanvas(app, width=600, height=600, highlightthickness=2, bg="#a3a0a9")
canvas.grid(column = 1, row = 0, rowspan=2, columnspan=3)
label_note = customtkinter.CTkLabel(app, text="Note: Ensure color of the image area to be omitted is of same color (preferably high contrast) ", fg_color = "red")
label_note.grid(row=2, column=1)

frame_transparent = customtkinter.CTkFrame(app, corner_radius=0)

# Mouse Click event
canvas.bind("<Button-1>", get_pixel_color)


# Image Button
image_button = customtkinter.CTkButton(master=frame_control, text="Select Image", command=select_image)
image_button.grid(column = 1, row = 2, padx = 50, pady = 50, )

#Download New Image Button
save_button = customtkinter.CTkButton(master=frame_control, text="Save Image as PNG", command=download_image)
save_button.grid(column = 1, row = 3)





# Run App
app.mainloop()