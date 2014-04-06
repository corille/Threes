# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 09:21:37 2014

@author: alexey
"""

import sys, random
from PyQt4 import QtCore, QtGui

class Threes(QtGui.QMainWindow):
    
    def __init__(self):
        super(Threes, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        
        self.board = Board(self)
        self.setCentralWidget(self.board)
        
        self.board.start()
        
        self.resize(400,600)
        self.setWindowTitle('Threes?')
        self.show()
        
class Board(QtGui.QFrame):
    N_Rows = 4
    N_Cols = 4
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.initBoard()

    def initBoard(self):     

        self.timer = QtCore.QBasicTimer()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        
        self.tiles=[]
        self.maxTile = 3
        
    def clearBoard(self):
        self.tiles = [[0 for c in range(Board.N_Cols)] for r in range(Board.N_Rows)]
        self.tiles[0][0]=1
        self.tiles[0][2]=2
        self.tiles[2][0]=3
        self.tiles[2][1]=3
    def start(self):
        self.clearBoard()
        self.timer.start(300,self)

    def keyPressEvent(self, event):
        
        key = event.key()
                
        if key == QtCore.Qt.Key_Left:
            self.slideLeft()
            
        elif key == QtCore.Qt.Key_Right:
            self.slideRight()
            
        elif key == QtCore.Qt.Key_Down:
            self.slideDown()
            
        elif key == QtCore.Qt.Key_Up:
            self.slideUp()
        else:
            super(Board, self).keyPressEvent(event)
        self.displayBoard() 
            
    def slideLeft(self):
        result = []
        for row in self.tiles:
            result.append(self.shift(row,Board.N_Cols))
    
    def slideRight(self):
        result = []
        for row in self.tiles:
            row.reverse()
            result.append(self.shift(row,Board.N_Cols))
            row.reverse()

    def slideDown(self):
        tiles_transposed = [list(i) for i in zip(*self.tiles)]
        result = []
        for row in tiles_transposed:
            row.reverse()
            result.append(self.shift(row,Board.N_Rows))
            row.reverse()
        self.tiles = [list(i) for i in zip(*tiles_transposed)]
        
        
    def slideUp(self):
        tiles_transposed = [list(i) for i in zip(*self.tiles)]
        result = []
        for row in tiles_transposed:
            result.append(self.shift(row,Board.N_Rows))
        self.tiles = [list(i) for i in zip(*tiles_transposed)]
            
    def shift(self,row,N):
        for i in range(N-1):
            if row[i] == 0:
                break
            if row[i] == row[i+1] and row[i] > 2:
                row[i+1] *= 2
                if row[i+1] > self.maxTile:
                    self.maxTile = row[i+1]
                break
            if row[i]*row[i+1] == 2: # a pair of 1 and 2:
                row[i+1] = 3
                break
        else:
            return False
        row.pop(i)
        row.append(0)
        return True
    
    def getRandomTile(self):
        pass
    
    def displayBoard(self):
        for row in self.tiles:
            print(row)
        print(self.maxTile)
    
       
def main():
    
    app = QtGui.QApplication([])
    game = Threes()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()