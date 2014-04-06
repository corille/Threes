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
        
    def clearBoard(self):
        self.tiles = [[0 for c in range(Board.N_Cols)] for r in range(Board.N_Rows)]

    def start(self):
        self.clearBoard()
        self.timer.start(100,self)

    def keyPressEvent(self, event):
        
        key = event.key()
                
        if key == QtCore.Qt.Key_Left:
            print('left')
            
        elif key == QtCore.Qt.Key_Right:
            print('right')
            
        elif key == QtCore.Qt.Key_Down:
            print('down')
            
        elif key == QtCore.Qt.Key_Up:
            print('up')
            
           
        else:
            super(Board, self).keyPressEvent(event)
    
    def displayBoard(self):
        for row in self.tiles: print(row)
    
    def shiftBoard(self, direction):
        pass

       
def main():
    
    app = QtGui.QApplication([])
    game = Threes()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()