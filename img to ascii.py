from PIL import Image

max_size = 175
symbols = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
filename = r'img to ascii/under.jpg'
img = Image.open(filename)  # type: Image.Image
img = img.convert(mode='L')
img.thumbnail((max_size, max_size))

def map_val(val, a, b, c, d):
    val2 = (val - a) / (b - a) * (d - c) + c
    return val2


def generate_ascii():
    img_width = img.width
    string = ""
    x = 0
    y = 0
    min_grey, max_grey = img.getextrema()
    for pixel in range(len(list(img.getdata()))):
        if (pixel + 1) % img_width == 0 and pixel > 10:
            string += "\n"
            x = 0
            y += 1
            continue
        grey_value = img.getpixel((x, y))
        string += symbols[int(map_val(grey_value, min_grey, max_grey, 0, len(symbols) - 1))]
        x += 1
    with open(f'{filename.split(".")[0]}.txt', 'w') as file:
        file.write(string)
    # print(string)
generate_ascii()
