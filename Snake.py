from turtle import Turtle


SNAKE_COR = ((0,0), (0,-20), (0,-40))
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    def __init__(self):

        self.all_segments=[]
        self.create_snake()
        self.head=self.all_segments[0]


    def create_snake(self):
        for i in SNAKE_COR:
            self.add_segment(i)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())


    def add_segment(self,position):
        new_obj = Turtle(shape="square")
        new_obj.color("white")
        new_obj.penup()
        new_obj.goto(position)
        self.all_segments.append(new_obj)


    def move(self):
        for seg in range(len(self.all_segments) - 1, 0, -1):
            x_val = self.all_segments[seg - 1].xcor()
            y_val = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(x_val, y_val)

        self.head.forward(20)


    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000,1000)

        self.all_segments.clear()
        self.create_snake()
        self.head=self.all_segments[0]


    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)







