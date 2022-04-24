import argparse
import click
import cv2
from matplotlib.colors import cnames
from matplotlib.pyplot import text
from numpy import minimum, require
import pandas as pd


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="image Path")
args = vars(ap.parse_args())
img_path = args['image']
# reading image with opencv
img = cv2.imread(img_path)
clicked = False
r = g = b = xpos = ypos = 0
# reading csv file with pandas and giving name to each column
index = ["color", "color_name", "hex", "r", "g", "b"]
csv = pd.read_csv('colors.csv', names=index, header=None)


def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


def getColorname(r, g, b):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(r - int(csv.loc[i, "r"])) + abs(g -
                                                int(csv.loc[i, "g"])) + abs(b - int(csv.loc[i, "b"]))
        if(d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while(1):
    cv2.imshow("image", img)
    if (clicked):
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        text = getColorname(r, g, b) + ' R=' + str(r) + \
            ' G=' + str(g) + ' B=' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)
        if(r+g+b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

        # break the loop when user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27:
            break

cv2.destroyAllWindows()
