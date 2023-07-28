import cv2
import os
import argparse

# parse arguments
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-i", "--imagedir", required=True, help="Path to the input directory containingimages")
PARSER.add_argument("-o", "--outputdir", required=True, help="Path to the output directory where processed images will be placed")
PARSER.add_argument("-x", "--xdimension", required=True, help="The y dimension")
PARSER.add_argument("-y", "--ydimension", required=True, help="The y dimension")

ARGS = vars(PARSER.parse_args())

image_dir = ARGS["imagedir"]
out_dir = ARGS["outputdir"]
xdim = int(ARGS["xdimension"])
ydim = int(ARGS["ydimension"])

images = os.listdir(image_dir)

count = 0

for image in images:
    imagePath = os.path.join(image_dir, image)

    try:
        # brute force resizing
        img = cv2.imread(imagePath)
        img = cv2.resize(img, (xdim, ydim))
        outPath = os.path.join(out_dir, image)
        cv2.imwrite(outPath, img)
        count += 1

    except Exception as e:
        print("Error: {} <{}>".format(str(e), imagePath))

print("Done. {} images resized.".format(count))