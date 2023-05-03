from PIL import ImageGrab

# Take Screenshot of the entire screen
image = ImageGrab.grab()

print("Taking Screenshot of the whole screen")
# To save the screenshot
image.save("Take_Screenshot_Screen.png")
print("Screenshot of the Screen taken and saved")

# Define the region to capture as Screenshot
left = 0
top = 0
width = 500
height = 500

# Take a Screenshot of the specified region
region = (left, top, left + width, top + height)
image = ImageGrab.grab(bbox=region)

print("Taking Screenshot of the Specified Region")
# To save the Screenshot
image.save("Take_Screenshot_Box.png")
print("Screenshot of the Specified Region taken and saved")
