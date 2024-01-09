from PIL import Image

def overlay_qr_on_background(qr_path, background_path, output_path, replacement_color=(0, 0, 0)):
    # Open the QR code and background images
    qr_img = Image.open(qr_path)
    background = Image.open(background_path)

    # Resize the QR code to half of its original size
    new_size = (int(qr_img.width / 2), int(qr_img.height / 2))
    qr_img = qr_img.resize(new_size, Image.BICUBIC)

    # Convert white background to a specific color
    qr_img = qr_img.convert("RGBA")
    data = qr_img.getdata()
    new_data = [(r, g, b, 0) if (r, g, b) == (255, 255, 255) else replacement_color for (r, g, b, a) in data]
    qr_img.putdata(new_data)

    # Paste the QR code onto the background
    background.paste(qr_img, (740, 1200), qr_img)

    # Save the result
    background.save(output_path, format="PNG")

# Example usage
for i in range(1, 25):
    qr_path = f"../../../Desktop/ROWDAH FRIEND/Report (4)_Page_{i}.png"
    background_path = "../../../../User/Downloads/Henna Event 02.png"
    output_path = f"../../../../User/Downloads/overlay_result_{i}.png"

    # overlay_qr_on_background(qr_path, background_path, output_path, replacement_color=(248, 239, 231))  # Replace with your desired color
    overlay_qr_on_background(qr_path, background_path, output_path, replacement_color=(142 , 100, 83))  # Replace with your desired color

