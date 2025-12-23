from PIL import Image

# Load image
img = Image.open("image.jpg")
pixels = img.load()

width, height = img.size
key = 50   # secret key

# Encrypt image
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[x, y] = (r, g, b)

# Save encrypted image
img.save("encrypted.png")
print("Image encrypted successfully!")
