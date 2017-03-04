import os
# import Image, ImageDraw
from PIL import Image
import csv
# from PIL import ImageDraw
import matplotlib.pyplot as plt


def draw_plot(image_path, out_image_path, landmark_file):
    img = Image.open(image_path)
    print(img.size)
    raw_image = img.getdata()

    out_raw_image = []
    for pix in raw_image:
        out_raw_image.append((pix, pix, pix))

    with open(landmark_file, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        next(reader)

        for row in reader:
            print(row)

    out_img = Image.new('RGB', img.size)
    out_img.putdata(out_raw_image)
    out_img.save(out_image_path)


if __name__ == '__main__':

    filename = "./data/Reslice_canon_T2star_r_clipped0109.tif"
    out_filename = "./landmarks.png"
    landmark_file = "kp.txt"

    draw_plot(filename, out_filename, landmark_file)
