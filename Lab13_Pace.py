import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()
        
class Box(Point):

    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        
class BoxFilled(Box):

    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):

    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)
        
class CircleFilled(Circle):

    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
        
