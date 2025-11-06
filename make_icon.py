from PIL import Image, ImageDraw, ImageFont

# Create a blank image
img = Image.new("RGBA", (256, 256), (255, 255, 255, 0))

# Load a font that has the emoji (Segoe UI Emoji is built into Windows)
font = ImageFont.truetype("seguiemj.ttf", 200)

# Draw the emoji 🐊 onto the image
draw = ImageDraw.Draw(img)
draw.text((10, 10), "🐊", font=font, embedded_color=True)

# Save as .ico
img.save("gator.ico", sizes=[(256, 256)])
print("Icon saved as gator.ico")