# Plotting the map  

import turtle

def setUpAxises(window,darty):
    window.bgcolor("white")
    darty.penup()
    darty.pensize(3)
    darty.pendown()
    darty.goto(0,100)
    darty.goto(0,-100)
    darty.goto(0,0)
    darty.goto(-100,0)
    darty.goto(100,0)
    darty.goto(0,0)
    #darty.goto(42.08687349,-75.96634084)

def movingTurtleThroughPoints(darty,x_cordinate,y_cordinate):
    print(float(x_cordinate),float(y_cordinate))

def plottingPoints(darty,lines):
    for line in lines:
        if("lat" in line):  # Data Cleaning
            continue
        line=line.rstrip('\n')
        line=line.split(',')
        x_cordinate,y_cordinate=line[0],line[1]
        movingTurtleThroughPoints(darty,x_cordinate,y_cordinate)

def main():
    window=turtle.Screen()
    darty=turtle.Turtle()
    darty.speed(0) # 0 is maximum speed
    setUpAxises(window,darty)
    darty.pensize(1)
    
    fileref=open("data.csv","r")  # Reading Lines from data
    lines=fileref.readlines()
    fileref.close()

    plottingPoints(darty,lines)
    window.exitonclick() # exits on clicking on screen

main()
