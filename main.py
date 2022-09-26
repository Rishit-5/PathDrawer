# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
import math
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def linear_regression(x, y):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean) ** 2).sum()
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))

    return (B0, B1)

def print_hi():
    # Load image
    im = cv2.imread('image.png')
    height, width, channels = im.shape

    # Define the blue colour we want to find - remember OpenCV uses BGR ordering
    lower_red = np.array([0,0,139])  # BGR-code of your lowest red
    upper_red = np.array([35,30,188])  # BGR-code of your highest red

    mask = cv2.inRange(im, lower_red, upper_red)
    # hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, (0, 100, 20), (25, 255, 255))

    # get all non zero values
    coord = cv2.findNonZero(mask)
    coord2 = []
    coord3 = []
    meanArray = []
    for i in coord:
        meanArray.append(coord[i][0][0][0][0])
    max = np.max(meanArray)
    min = np.min(meanArray)
    middle = min+((min+max)/2)
    print(middle)
    for i in coord:
        if coord[i][0][0][0][0] < middle:
            coord2.append(coord[i][0][0][0])
        else:
            coord3.append(coord[i][0][0][0])

    x = []
    y = []
    for i in range(0,len(coord2)):
        x.append(coord2[i][0])
        y.append(coord2[i][1])
    x2 = np.array(x)
    y2 = np.array(y)
    b = linear_regression(x2, y2)
    startpoint = (0,math.floor(b[0] + b[1]*0))
    endpoint = (width,math.floor(b[0] + b[1]*width))
    for i in coord:
        im = cv2.circle(im, (coord[i][0][0][0][0], coord[i][0][0][0][1]), radius=2, color=(0, 255, 0), thickness=-1)
    im = cv2.line(im, startpoint, endpoint, (215, 147, 205), 10)

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
    print(len(coord2))
    print(len(coord3))

    for i in coord:
        im = cv2.circle(im, (coord[i][0][0][0][0], coord[i][0][0][0][1]), radius=2, color=(0, 255, 0), thickness=-1)
    im = cv2.line(im, startpoint, endpoint, (215, 147, 205), 10)
    cv2.startWindowThread()
    cv2.imshow("Display window", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
