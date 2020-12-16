from turtle import*
import random

speed(speed='fast')
#you can give any speed command like - slow, fastest.

def  draw(m, y, angle):
    #loop for number of star
    for i in range(m):
        colormode(255)
        #choosing random integers between 0 and 255 to generate random rbg values
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        #setting the outline and fill colour
        #pensize(3)
        pencolor(a, b, c)
        fillcolor(a, b, c)

        #begins filling the star
        begin_fill()

        #loop for drawing each start
        for j in range(5):
            forward(5 * m-5 * i)
            right(y)
            forward(5 * m-5 * i)
            right(72-y)

        #color filling complete
        end_fill()

        #rotating for the next star
        rt(angle)

#setting the parameters
m = 35      #numbers of stars
y = 150     #exterior angle of each star
angle = 20  #angle of rotation for the spiral

draw(m, y, angle)