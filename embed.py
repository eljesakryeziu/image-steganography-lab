from PIL import Image
import random

key = 2026
colour_plane = 1
bit_position = 7

cover_image = "img/flowers.bmp"
secret_file = "secret.txt"
output_image = "stego-image.bmp"


def modify_pixel(pixel, plane, bit_position, direction):
    change = direction * (2 ** (7 - bit_position))

    red = pixel[0] + change if plane == 0 else pixel[0]
    green = pixel[1] + change if plane == 1 else pixel[1]
    blue = pixel[2] + change if plane == 2 else pixel[2]

    return (max(0, min(255, red)), max(0, min(255, green)), max(0, min(255, blue)))


image = Image.open(cover_image).convert("RGB")
width, height = image.size
pixels = image.load()

with open(secret_file, "r", encoding="utf-8") as file:
    secret = file.read()

message_bits = "".join(format(ord(character), "07b") for character in secret)
length_bits = format(len(secret), "014b")
all_bits = length_bits + message_bits

total_pixels = width * height

if len(all_bits) > total_pixels:
    raise ValueError("The cover image does not have enough capacity for this message.")

shuffled_indices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffled_indices)

for bit_index, secret_bit in enumerate(all_bits):
    pixel_index = shuffled_indices[bit_index]

    x = pixel_index % width
    y = pixel_index // width

    current_pixel = pixels[x, y]
    channel_value = current_pixel[colour_plane]
    channel_bits = format(channel_value, "08b")

    current_bit = channel_bits[bit_position]

    if current_bit != secret_bit:
        direction = -1 if channel_value == 255 else 1
        pixels[x, y] = modify_pixel(
            current_pixel, colour_plane, bit_position, direction
        )

image.save(output_image)

print("Embedding completed successfully.")
print("Stego image saved as:", output_image)
