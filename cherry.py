from turtle import *
from random import *
from math import *

def draw_cherry_tree(savings):
    def tree(n, l):
        pd ()  # begin to paint
        # Drop Shadow
        t = cos ( radians ( heading () + 45 ) ) / 8 + 0.25
        pencolor ( t, t, t )
        pensize ( n / 3 )
        forward ( l )  # Draw a branch
    
        if n > 0:
            b = random () * 15 + 10  # Right branch deflection Angle
            c = random () * 15 + 10  # Left branch deflection Angle
            d = l * (random () * 0.25 + 0.7)  # The length of the next branch
            # Turn right at an Angle and draw the right branch
            right ( b )
            tree ( n - 1, d )
            # Turn left at an Angle and draw the left branch
            left ( b + c )
            tree ( n - 1, d )
            # Turn back
            right ( c )
        else:
            # Draw leaves
            right ( 90 )
            n = cos ( radians ( heading () - 45 ) ) / 4 + 0.5
            ran = random ()
            # Compared to the original randomly added filled circles, to make the cherry blossom leaves look a little more
            if (ran > 0.7):
                begin_fill ()
                circle ( 3 )
                fillcolor ( 'pink' )
            # The original randomly generated leaves were replaced with a uniform pink color
            pencolor ( "pink" )
            circle ( 3 )
            if (ran > 0.7):
                end_fill ()
            left ( 90 )
            # Add 0.3 times the falling leaves
            if (random () > 0.7):
                pu ()
                # Drift down
                t = heading ()
                an = -40 + random () * 40
                setheading ( an )
                dis = int ( 800 * random () * 0.5 + 400 * random () * 0.3 + 200 * random () * 0.2 )
                forward ( dis )
                setheading ( t )
                # Draw leaves
                pd ()
                right ( 90 )
                n = cos ( radians ( heading () - 45 ) ) / 4 + 0.5
                pencolor ( n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4 )
                circle ( 2 )
                left ( 90 )
                pu ()
                # Get back
                t = heading ()
                setheading ( an )
                backward ( dis )
                setheading ( t )
        pu ()
        backward ( l )  # Send back
    
    bgcolor ( 0.91, 0.9255, 0.9882 )  # Set the background color (change gray to lavender)
    ht ()  # hide turtle
    speed ( 0 )  # Speed 1-10 is gradual, with 0 being the fastest
    tracer ( 0, 0 )
    pu ()  # pen up
    backward ( 50 )
    left ( 90 )  # Left 90 degrees
    pu ()  # pen up
    backward ( 300 )  # Back 300

    l = 5
    t = 10

    multiplier = max(savings // 200, 1)
    tree(min(l * multiplier, 12), min(t * multiplier,120))
    done ()