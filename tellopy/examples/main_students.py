# Jackson Blunt, Nilansh Ghosh, Mario Handal

from tkinter import * # tkinter is a GUI library built-in to python
import tellopy # for tello drone application programmer interface (API)
import time # for sleep(t)
from es140x import * # include given code with GUI set up
#import cv2 # to enable opencv, run pip install opencv-python, then uncomment

# global variable for handling gui, initially set to nothing and instantiated 
# in the function main() below
root = None

# FINAL PROJECT INSTRUCTIONS
# for the final project submission, add your shape creation code 
# to the relevant functions, e.g., square(drone), cube(drone), etc.
# if you finish these and want to do more, please let me know during class
#
# Submit your group's code (only 1 person in the group needs to submit)
# in Brightspace under Assignments -> Group Project

# function that when called has the Tello trace a square
# this will be called like square(drone), and this function is 
# called when the "Draw square" button is pressed under 
# the GUI elements Shapes -> Square -> Draw Square
#
# the side length is optional, if you want to add it, you will also need 
# to modify the function drawSquare(self) in the file es140x.py
def square(drone):
    print('square code here')
    # TODO: add your square code here
    drone.forward(20)
    sleep(3)
    drone.forward(0)
    sleep(3)
    drone.right(20)
    sleep(3)
    drone.right(0)
    sleep(3)
    drone.backward(20)
    sleep(3)
    drone.backward(0)
    sleep(3)
    drone.left(20)
    sleep(3)
    drone.left(0)    
    sleep(3)
    drone.land()

#Tested in class on 10/25 and mostly worked

# function that when called has the Tello trace a cube
# this will be called like cube(drone), and this function is 
# called when the "Draw cube" button is pressed under 
# the GUI elements Shapes -> Cube -> Draw Cube
#
# the side length is optional, if you want to add it, you will also need 
# to modify the function drawCube(self) in the file es140x.py
def cube(drone):
    print('cube code here')
    # TODO: add your cube code here
    drone.forward(20)
    sleep(3)
    drone.forward(0)
    sleep(3)
    drone.right(20)
    sleep(3)
    drone.right(0)
    sleep(3)
    drone.backward(20)
    sleep(3)
    drone.backward(0)
    sleep(3)
    drone.left(20)
    sleep(3)
    drone.left(0)    
    sleep(3)
    drone.up(20)
    sleep(3)
    drone.up(0)
    sleep(3)
    drone.forward(20)
    sleep(3)
    drone.forward(0)
    sleep(3)
    drone.right(20)
    sleep(3)
    drone.right(0)
    sleep(3)
    drone.backward(20)
    sleep(3)
    drone.backward(0)
    sleep(3)
    drone.left(20)
    sleep(3)
    drone.left(0)    
    sleep(3)
    
    drone.land()


# function that when called has the Tello trace a triangle
# this will be called like triangle(drone), and this function is 
# called when the "Draw triangle" button is pressed under 
# the GUI elements Shapes -> Triangle -> Draw Triangle
#
# the side length is optional, if you want to add it, you will also need 
# to modify the function drawTriangle(self) in the file es140x.py
def triangle(drone):
    print('triangle code here')
    # TODO: add your triangle code here
    drone.forward(10)
    drone.right(10)
    sleep(3)
    drone.forward(0)
    drone.right(0)
    sleep(3)
    drone.backward(10)
    drone.right(10)
    sleep(3)
    drone.backward(0)
    drone.right(0)
    sleep(3)
    drone.left(14)
    sleep(3)
    drone.left(0)
    sleep(3)

    drone.land()

# function that when called has the Tello trace a circle
# this will be called like circle(drone), and this function is 
# called when the "Draw circle" button is pressed under 
# the GUI elements Shapes -> Circle -> Draw Circle
#
# the radius is optional, if you want to add it, you will also need 
# to modify the function drawCircle(self) in the file es140x.py
def circle(drone):
    print('circle code here')
    # TODO: add your circle code here

    #Untested but should make 64 course adjustments and trace somethng circular of an unknown radius. 
    for i in range(64):
        xVel = 10 * math.cos(i * ((2 * math.pi) / 64))
        yVel = 10 * math.sin(i * ((2 * math.pi) / 64))

        drone.forward(xVel)
        drone.right(yVel)

        sleep(5)

        drone.forward(0)
        drone.right(0)

    drone.land()

# main function that is called when you run "python main_students.py"
def main():
    global root # access the GUI root level interface variable
    root = Tk()
    app = Window(root)
    root.wm_title("Tello Interaction Interface")
    root.geometry("320x160")
    root.mainloop()

# define main entry point to be called when running this file
if __name__ == "__main__":
    # execute only if run as a script, e.g., when running from the console the following:
    # python main_students.py
    main()
