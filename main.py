""""
    The goal here is to demonstrate and practice the use of event listeners.

    Will be creating multiple games in which I will apply the concept.

    Key Take aways.
        1. When using a function as an argument you do not add parentheses.
        2. It is recommended to use keyword arguments eg my_function(c = 3, a = 1, b = 2)
           instead of positional arguments eg my_function(1, 2, 3) when working with functions
           you did not create.
"""

import turtle as t

tim = t.Turtle()


def move_forward():
    tim.forward(20)


screen = t.Screen()
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
