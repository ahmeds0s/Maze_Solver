from cell import Cell
from point import Point
from time import sleep
from random import choice, seed

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed_value=None
                 ):
        self.x1 = x1
        self.y1 = y1
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.solving = False
        if seed_value != None:
            self.seed_value = seed_value
        self._create_cells()
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):  
            rows = []
            for j in range(self.num_rows):
                new_cell = Cell()
                rows.append(new_cell)
                self._draw_cell(new_cell, i,j)
                self._animate(new_cell)
            self._cells.append(rows)
            sleep(0.005)
            



    

    def _draw_cell(self,cell,i, j):
        if self.seed_value != None:
            seed(self.seed_value * i + j)
        
        choices = [True]

        cell_topleft_x = self.x1 + i * self.cell_size_x
        cell_topleft_y = self.y1 + j * self.cell_size_y
        cell_bottomright_x = self.x1 + (i + 1) * self.cell_size_x
        cell_bottomright_y = self.y1 + (j + 1) * self.cell_size_y 
        cell.set_cell(choice(choices), choice(choices), choice(choices), choice(choices), Point(cell_topleft_x, cell_topleft_y), Point(cell_bottomright_x, cell_bottomright_y))


    def _animate(self, cell):
        """reveals the changes to the window"""
        if self.solving:
            sleep(0.1)
        cell.draw(self.win.canvas)
        self.win.redraw()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].left = False
        self._cells[0][0].draw(self.win.canvas)

        self._cells[0][0].right = False
        self._cells[0][0].draw(self.win.canvas)

        self._cells[0][0].top = False
        self._cells[0][0].draw(self.win.canvas)
    
        self._cells[0][0].bottom = False
        self._cells[0][0].draw(self.win.canvas)

        self._cells[-1][-1].right = False
        self._cells[-1][-1].draw(self.win.canvas)

        
        self._cells[-1][-1].left = False
        self._cells[-1][-1].draw(self.win.canvas)
    
        
        self._cells[-1][-1].top = False
        self._cells[-1][-1].draw(self.win.canvas)


        self._cells[-1][-1].bottom = False
        self._cells[-1][-1].draw(self.win.canvas)

    def _break_walls_r(self, i, j):
        """makes sure that there is an entry and exit on the maze"""
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return
        while True:
            to_visit = self.adjacent_cells(i,j)
            tmp_visit = to_visit.copy()
            for cell in tmp_visit:
                if self._cells[cell[0]][cell[1]].visited:
                    to_visit.remove(cell)
           

            if len(to_visit) == 0:
                return

            choice_c = choice(to_visit)
            if choice_c[1] == j - 1:
                self._cells[i][j].top = False
                self._cells[choice_c[0]][choice_c[1]].bottom = False 
                self._cells[i][j].draw(self.win.canvas)
                self._cells[i][j - 1].draw(self.win.canvas)

            if choice_c[1] == j + 1:
                self._cells[i][j].bottom = False
                self._cells[choice_c[0]][choice_c[1]].top = False
                self._cells[i][j].draw(self.win.canvas)
                self._cells[i][j+1].draw(self.win.canvas)

            if choice_c[0] == i + 1 :
                self._cells[i][j].right = False
                self._cells[choice_c[0]][choice_c[1]].left = False 
                self._cells[i][j].draw(self.win.canvas)
                self._cells[i+1][j].draw(self.win.canvas)

            if choice_c[0] == i - 1 : 
                self._cells[i][j].left = False
                self._cells[choice_c[0]][choice_c[1]].right = False
                self._cells[i][j].draw(self.win.canvas)
                self._cells[i-1][j].draw(self.win.canvas)
         
            self._break_walls_r(choice_c[0],choice_c[1])

    def adjacent_cells(self, i, j):
        available_paths = [(i,j - 1),(i-1,j),(i+1,j),(i,j+1)]
        if j == self.num_rows - 1:
            available_paths.remove((i,j + 1))
        if i == self.num_cols - 1:
            available_paths.remove((i+1, j))
        if i == 0:
            available_paths.remove((i-1,j))
        if j == 0:
            available_paths.remove((i, j-1))


        return available_paths
    def redraw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw(self.win.canvas)
                print(cell)
    def  _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    

    def solve(self):
        self.solving = True
        return self._solve_r(0,0)
       
        


    def _solve_r(self,i,j):
        current = self._cells[i][j]
        self._animate(current)
        self._cells[i][j].visited = True
        if current == self._cells[-1][-1]:
            return True
        neighbor_cells = self.adjacent_cells(i,j)
        tmp_neighbors = neighbor_cells.copy()
        for cell in tmp_neighbors:
            if self._cells[cell[0]][cell[1]].visited:
                neighbor_cells.remove(cell)
        for cell in neighbor_cells:
            if cell[0] == i + 1:
                if self._cells[cell[0]][cell[1]].left == False and current.right == False: 
                    current.draw_move(self._cells[cell[0]][cell[1]])
                    if self._solve_r(cell[0],cell[1]):
                        return True
                    else:
                        current.draw_move(self._cells[cell[0]][cell[1]],True)

            if cell[0] == i - 1:
                if self._cells[cell[0]][cell[1]].right == False and current.left == False: 
                    current.draw_move(self._cells[cell[0]][cell[1]])
                    if self._solve_r(cell[0],cell[1]):
                        return True
                    else:
                        current.draw_move(self._cells[cell[0]][cell[1]],True)

            if cell[1] == j + 1:
                if self._cells[cell[0]][cell[1]].top == False and current.bottom == False: 
                    current.draw_move(self._cells[cell[0]][cell[1]])
                    if self._solve_r(cell[0],cell[1]):
                        return True
                    else:
                        current.draw_move(self._cells[cell[0]][cell[1]],True)

            if cell[1] == j - 1:
                if self._cells[cell[0]][cell[1]].bottom == False and current.top == False: 
                    current.draw_move(self._cells[cell[0]][cell[1]])
                    if self._solve_r(cell[0],cell[1]):
                        return True
                    else:
                        current.draw_move(self._cells[cell[0]][cell[1]],True)

        return False






        
            
            








