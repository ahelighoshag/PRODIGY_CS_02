from PIL import Image

# Load encrypted image
img = Image.open("encrypted.png")
pixels = img.load()

width, height = img.size
key = 50   # SAME key

# Decrypt image
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        pixels[x, y] = (r, g, b)

# Save decrypted image
img.save("decrypted.png")
print("Image decrypted successfully!")
