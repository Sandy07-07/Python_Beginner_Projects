from PIL import Image

# Open the Image File
image = Image.open("Image_Compressor_Original.jpg")

# To set max width and max height of compressed image
max_width = int(input("Enter the Max Width of the Compressed Image :- "))
max_height = int(input("Enter the Max Height of the Compressed Image :- "))
max_size = (max_width, max_height)

# Resize the Image
print("Resizing the Image according to Max Width and Max Height")
image.thumbnail(max_size)

# Save the Compressed image
print("Resizing the Image completed")
image.save("Image_Compressor_Reduced.jpg")
