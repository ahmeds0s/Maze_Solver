from line import Line
from point import Point
from tkinter import Tk, Canvas

class Cell:
    def set_cell(self,top:bool,right:bool,bottom:bool,left:bool,top_left:Point,bottom_right:Point):
        self.top = top
        self.right = right
        self.left = left
        self.bottom = bottom
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.visited = False

    def draw(self, canvas:Canvas):
        self.canvas = canvas
        if self.left:
            line = Line(self.top_left, Point(self.top_left.x,self.bottom_right.y))
            line.draw(canvas, "black")
        else:
            line = Line(self.top_left, Point(self.top_left.x,self.bottom_right.y))
            line.draw(canvas, "white")
        if self.right:
            line = Line(self.bottom_right, Point(self.bottom_right.x, self.top_left.y))
            line.draw(canvas, "black")
        else:
            line = Line(self.bottom_right, Point(self.bottom_right.x, self.top_left.y))
            line.draw(canvas, "white")

        if self.top:
            line = Line(self.top_left,Point(self.bottom_right.x, self.top_left.y))
            line.draw(canvas, "black")
        else: 
            line = Line(self.top_left,Point(self.bottom_right.x, self.top_left.y))
            line.draw(canvas, "white")

        if self.bottom:
            line = Line(Point(self.top_left.x, self.bottom_right.y), self.bottom_right)
            line.draw(canvas, "black")
        else:
            line = Line(Point(self.top_left.x, self.bottom_right.y), self.bottom_right)
            line.draw(canvas, "white")

    def __rshift__(self,other):
        pass

    
    def draw_move(self, to_cell, undo = False):
        p1 = Point((self.top_left.x + self.bottom_right.x) / 2, (self.bottom_right.y + self.top_left.y) / 2)
        p2 = Point((to_cell.top_left.x + to_cell.bottom_right.x) / 2, (to_cell.bottom_right.y + to_cell.top_left.y) / 2)
        line = Line(p1, p2)
        if undo:
            line.draw(self.canvas, fill_color="light gray")
            return
        line.draw(self.canvas, fill_color="red")
    def __str__(self) -> str:
        return f"{self.top} {self.right} {self.bottom} {self.left}"

    def __repr__(self) -> str:
        return f"{self.top} {self.right} {self.bottom} {self.left}"      

        




