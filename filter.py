#! python3.6
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os
def convertImg():
    #Convert imagens manually
    cv2.imwrite("images/img1.png", cv2.imread("images/022.png"))

    img2 = Image.open("images/cameraman_sp.gif")
    img2.save("images/img2.png", 'png', optimize=True, quality=100)

    img3 = Image.open("images/medfilt2.gif")
    img3.save("images/img3.png", 'png', optimize=True, quality=100)

    cv2.imwrite("images/img4.png", cv2.imread("images/SaltAndPepperNoise.jpg"))

    return ""

def avgFilter(img, kernel, path, id):
    img_out = cv2.filter2D(img, -1, kernel) #value -1 means that the output img wiil have the same depth as the input img.
    cv2.imwrite(path+str(id)+'.png', img_out)

def medianFilter(img, kernel, path,id):
    img_out = cv2.medianBlur(img, kernel)
    cv2.imshow('Out image - Median Filter Processing', img_out)
    cv2.imwrite(path+str(id)+'.png', img_out)

def main():
    # output files folder
    path = ("images_out/1", "images_out/2", "images_out/3", "images_out/4")
    item = ("A/", "B/", "C/")
    for j in range(4):
        for i in range(3):
            os.makedirs(path[j] + item[i], exist_ok=True)

    mn_avg = ([[3,3], [5,5], [7,7]])
    mn_median = (3,5,7)
    N = (9,25,49)
    kernel_B = (np.array([[1,2,1], [2,4,2], [1,2,1]], dtype=float)*1/16)

    for i in range(4):
        # read images
        image = cv2.imread('images/img' + str(i + 1) + '.png')
        for j in range(3):
            # item A - calculate average filter (3x3, 5x5, 7x7)
            kernel_A = (np.ones(mn_avg[j], dtype=float)*1/N[j])
            id = "img_out"+str(i+1)+"-A-K"+str(j+1)
            avgFilter(image, kernel_A, path[i]+item[0], id)

            # item C - calculate median filter (3x3, 5x5, 7x7)
            id3 = "img_out"+str(i+1)+"-C-K"+str(j+1)
            medianFilter(image, mn_median[j], path[i]+item[2], id3)

        # item B - calculate average filter (3x3)
        id2 = "img_out"+str(i+1)+"-B"

        avgFilter(image, kernel_B, path[i]+item[1], id2)

    print("End of processing")
    return ""

if __name__ == '__main__':
    main()
