""" 
    File name: graphicsWindow.py
    Author: Ali Ravaee
    Date created: Jan 22, 2020
    Python: 3.9.1

"""
import operator
from PIL import Image

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    def drawLine(self,point1,point2,color): 
        """ draws a line using Bresenham's line algorithm in the image from point p1 to point p2 with color.

        Args:
            point1 (matrix): This is a 2x1 matrix (column vector)
            point2 (matrix): This is a 2x1 matrix (column vector)
            color (tuple): This tuple contains three values (0,255) that represent RGB

        Returns:
            None
        """
        # getting x,y coordinates of point1 and point2
        x0 = point1.get(0, 0)
        y0 = point1.get(1, 0)

        x1 = point2.get(0, 0)
        y1 = point2.get(1, 0)

        # compare abs delta-y to abs delta-x
        # if dy < dx, the line is x-axis is dominant
        # if dy > dx, the line is y-axis is dominant
        if abs(y1 - y0) < abs(x1 - x0):
            # if the condition is met reverse the input coordinates before drawing
            if x0 > x1:
                x1, y1, x0, y0 = x0, y0, x1, y1

            # calculate delta, store sign in yi
            dx = x1 - x0
            dy = y1 - y0
            yi = 1

            # draw line from top to bottom, else bottom to top
            if dy < 0:
                yi = -1
                dy = -dy

            # Calculate the line equation based on deltas
            # after deriving the algorithm, we can get rid of the 1/2 factor by multiplying everthing by 2
            D = (2 * dy) - dx
            # update y value
            y = y0

            # loop through x values
            for x in range(int(x0), int(x1)):
                # Draw pixel at this location
                self.drawPoint((x, y), color)
                # deal with octants
                if D > 0:
                    y = y + yi
                    D = D + (2 * (dy - dx))
                else:
                    D = D + 2*dy
        else:
            # if the condition is met reverse the input coordinates before drawing
            if y0 > y1:
                x1, y1, x0, y0 = x0, y0, x1, y1

            # calculate delta, store sign in xi
            dx = x1 - x0
            dy = y1 - y0
            xi = 1

            # draw line from right to left, else left to right
            if dx < 0:
                xi = -1
                dx = -dx

            D = (2 * dx) - dy
            x = x0
            # loop through y values
            for y in range(int(y0), int(y1)):
                # Draw pixel at this location
                self.drawPoint((x, y), color)
                # deal with octants
                if D > 0:
                    x = x + xi
                    D = D + (2 * (dx - dy))
                else:
                    D = D + 2*dx


    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height