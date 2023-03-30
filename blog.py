from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title('Blogs')
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

# Define the list of image file paths
image_files = [
    './blogs/image1.jpg',
    './blogs/image2.jpg',
    './blogs/image3.jpg',
    './blogs/image4.jpg',
    './blogs/image5.jpg'
]

# Load a random image from the list
image_path = random.choice(image_files)
image = Image.open(image_path)

# Resize the image to fit the window
# width, height = root.winfo_width(), root.winfo_height()
# image = image.resize((width, height))

# Convert the image to a Tkinter PhotoImage object
photo = ImageTk.PhotoImage(image)

# Add a label to display the image
image_label = Label(root, image=photo)
image_label.pack()

# Run the main event loop
root.mainloop()
