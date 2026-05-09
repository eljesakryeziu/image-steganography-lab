from PIL import Image
import random

key = 2026
colour_plane = 1
bit_position = 7

stego_image = "stego-image.bmp"


image = Image.open(stego_image).convert("RGB")
width, height = image.size
pixels = image.load()


total_pixels = width * height

shuffled_indices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffled_indices)


extracted_bits = []

for pixel_index in shuffled_indices:
    x = pixel_index % width
    y = pixel_index // width

    channel_value = pixels[x, y][colour_plane]
    channel_bits = format(channel_value, "08b")

    extracted_bits.append(channel_bits[bit_position])


length_bits = extracted_bits[:14]
secret_length = int("".join(length_bits), 2)


secret_characters = []

for i in range(secret_length):
    start = 14 + i * 7
    end = start + 7

    character_bits = extracted_bits[start:end]
    ascii_value = int("".join(character_bits), 2)

    secret_characters.append(chr(ascii_value))


secret = "".join(secret_characters)

print("Recovered secret message:")
print(secret)
