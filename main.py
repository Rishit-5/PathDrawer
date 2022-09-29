import cv2
import numpy as np
import math

# method used to calculate the best-fit line
def linear_regression(x, y):
    x_mean = x.mean()
    y_mean = y.mean()

    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean) ** 2).sum()
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    return (B0, B1)

def print_hi():
    # Load image
    im = cv2.imread('image.png')
    height, width, channels = im.shape

    # Define the blue colour we want to find - remember OpenCV uses BGR ordering
    lower_red = np.array([0,0,139])  # BGR-code of your lowest red
    upper_red = np.array([35,30,188])  # BGR-code of your highest red

    mask = cv2.inRange(im, lower_red, upper_red)

    # get all non zero values
    coord = cv2.findNonZero(mask)
    # coord2 stores coordinates with x-values to the left of the middle
    coord2 = []
    # coord3 stores coordinates with x-values to the right of the middle
    coord3 = []
    # middleArray stores coordinates in an easier 2D array format
    middleArray = []
    for i in coord:
        middleArray.append(coord[i][0][0][0][0])
    max = np.max(middleArray)
    min = np.min(middleArray)
    middle = min+((min+max)/2)
    # sorts the arrays based on x-value
    for i in coord:
        if coord[i][0][0][0][0] < middle:
            coord2.append(coord[i][0][0][0])
        else:
            coord3.append(coord[i][0][0][0])
    # x and y store the respective x and y values of each coordinate
    x = []
    y = []
    for i in range(0,len(coord2)):
        x.append(coord2[i][0])
        y.append(coord2[i][1])
    #turns x and y into np arrays to be easily used in the linear regression method
    x2 = np.array(x)
    y2 = np.array(y)

    b = linear_regression(x2, y2)

    # inputs into the y=mx+b line starting at x=0 and ending at the width of the image
    startpoint = (0,math.floor(b[0] + b[1]*0))
    endpoint = (width,math.floor(b[0] + b[1]*width))

    #draws the line
    im = cv2.line(im, startpoint, endpoint, (215, 147, 205), 10)

    #following code repeats the same process for the other line
    x = []
    y = []
    for i in range(0, len(coord3)):
        x.append(coord3[i][0])
        y.append(coord3[i][1])
    x2 = np.array(x)
    y2 = np.array(y)
    b = linear_regression(x2, y2)
    startpoint = (0, math.floor(b[0] + b[1] * 0))
    endpoint = (width, math.floor(b[0] + b[1] * width))

    im = cv2.line(im, startpoint, endpoint, (215, 147, 205), 10)


    cv2.startWindowThread()
    cv2.imshow("Display window", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print_hi()
