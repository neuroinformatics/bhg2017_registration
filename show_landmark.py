from PIL import Image
import sys
import csv
import matplotlib.pyplot as plt


def draw_plot(image_path, out_image_path, landmark_file):
    img = Image.open(image_path)
    print('Image Size: ', img.size)
    raw_image = img.getdata()
    cmap = plt.get_cmap('rainbow')

    pos_list = []
    out_raw_image = []
    for pix in raw_image:
        # out_raw_image.append((pix, pix, pix))
        val = int(round((pix[0]+pix[1]+pix[2])/3, 0))
        out_raw_image.append((val, val, val))

    with open(landmark_file, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        next(reader)
        next(reader)

        for row in reader:
            pos_x = round(float(row[1]), 0)
            pos_y = round(float(row[2]), 0)
            pos = int(pos_y * int(img.size[0]) + pos_x)
            pos_list.append(pos)

    print("Number of Landmarks: ", len(pos_list))
    for i, pos in enumerate(pos_list):
        color = cmap(float(i)/len(pos_list))
        out_raw_image[pos] = (int(255*color[0]), int(255*color[1]), int(255*color[2]))

    out_img = Image.new('RGB', img.size)
    out_img.putdata(out_raw_image)
    out_img.save(out_image_path)


if __name__ == '__main__':

    if len(sys.argv) < 4 :
        print("Usage: $ %s [INPUT IMAGE] [LANDMARK LIST] [OUTPUT IMAGE]" % "show_landmark.py")
        # filename = "./data/Reslice_canon_T2star_r_clipped0109.tif"
        filename = "./data/CD00016.1-Adra1b.tif"
        # landmark_file = "data/kp.txt"
        landmark_file = "data/best_testmatch_Points.txt"
        out_filename = "./landmarks.png"
        # exit()
    else:
        filename = sys.argv[1]
        landmark_file = sys.argv[2]
        out_filename = sys.argv[3]

    draw_plot(filename, out_filename, landmark_file)
