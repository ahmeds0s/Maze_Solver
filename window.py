from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width:int, height:int):
        self.__window = Tk()
        self.__window.protocol("WM_DELETE_WINDOW",self.close)
        self.__window.title("The Maze SoLver")
        self.canvas = Canvas(width=width, height=height) 
        self.canvas.pack()   # add the canvas to the window 
        self.__running = False # the state of the window

    def redraw(self):
        """updates the window with changes"""
        self.__window.update()
        self.__window.update_idletasks()


    def wait_for_close(self):
        """keeps the gui window running as long as running is true by calling redraw"""
        self.__running = True
        while self.__running:
            self.redraw()
    

    def close(self):
        """stops the window by setting the running to false"""
        self.__running = False

        
    












