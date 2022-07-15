from typing import *
from PIL import Image, ImageDraw, ImageFont

Status = Literal[-1, 0, 1]
def generate_image(data: list[Status]) -> Image:
    ...

color_map: dict[str, str | dict[Status, str]] = {
    'back': 'white',
    'r_back': 'purple',
    'font': 'pink',
    'circles': {
        -1: 'red',
        0: 'gray',
        1: 'green'
    }
}

cord = X, Y = (1200, 200)
im = Image.new('RGB', cord, color_map['back'])

handle = ImageDraw.Draw(im)

space = 100
incr = (X - space) / 7
r = 40

data: list[Status] = [1, 1, 0, -1, 1, 0, -1]

for n in range(1, 8):
    nX = ((2*n - 1) * incr) / 2
    handle.ellipse(
        [(nX - r, Y/2 - r), (nX + r, Y/2 + r)], 
        color_map['circles'][data[n - 1]]
    )

handle.rectangle([(X - space, 0), (X, Y)], color_map['r_back'])

fnt = ImageFont.truetype('SourceSansPro-Bold.ttf', 100)
handle.text((X - space + 27, 35), '7', color_map['font'], font=fnt)

im.show()