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
      

        size = QtCore.QSize(600,600)
        self.resize(size)
        self.setFixedSize(size)
        self.setWindowTitle('Threes?')
        self.board.start()
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
        
        self.deck = Deck()
        


        
    def clearBoard(self):
        self.tiles = [[0 for c in range(Board.N_Cols)] for r in range(Board.N_Rows)]
        positions = random.sample([i for i in range(Board.N_Cols * Board.N_Rows)], 9)
        
        for p in positions:
            self.tiles[p // Board.N_Cols][p % Board.N_Cols]=self.deck.getCard()
            

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

        self.update()
            
    def slideLeft(self):
        rows_moved = []
        for i,row in enumerate(self.tiles):
            if self.shift(row,Board.N_Cols):
                rows_moved.append(i)
        if len(rows_moved) == 0:
            return
        self.tiles[random.choice(rows_moved)][-1] = self.getRandomTile()


            
    
    def slideRight(self):
        rows_moved = []
        for i,row in enumerate(self.tiles):
            row.reverse()
            if self.shift(row,Board.N_Cols):
                rows_moved.append(i)
            row.reverse()
        if len(rows_moved) == 0:
            return
        self.tiles[random.choice(rows_moved)][0] = self.getRandomTile()
        
    def slideDown(self):
        tiles_transposed = [list(i) for i in zip(*self.tiles)]
        rows_moved = []
        for i,row in enumerate(tiles_transposed):
            row.reverse()
            if self.shift(row,Board.N_Rows):
                rows_moved.append(i)
            row.reverse()
        if len(rows_moved) == 0:
            return
        tiles_transposed[random.choice(rows_moved)][0] = self.getRandomTile()
        self.tiles = [list(i) for i in zip(*tiles_transposed)]
        
        
    def slideUp(self):
        tiles_transposed = [list(i) for i in zip(*self.tiles)]
        rows_moved = []
        for i,row in enumerate(tiles_transposed):
            if self.shift(row,Board.N_Rows):
                rows_moved.append(i)
        if len(rows_moved) == 0:
            return
        tiles_transposed[random.choice(rows_moved)][-1] = self.getRandomTile()
        self.tiles = [list(i) for i in zip(*tiles_transposed)]

            
    def shift(self,row,N):
        for i in range(N-1):
            if row[i] == 0 and row[i+1] != 0: #empty rows don't shift
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
        # ignore larger bonus tiles for now
        return self.deck.getCard(self.maxTile)


    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        rect = self.contentsRect()
        
        for row in range(Board.N_Rows):
            for col in range(Board.N_Cols):
                if self.tiles[row][col] != 0:
                    self.drawTile(painter,col*100,row*150,self.tiles[row][col])
        self.drawTile(painter,450,200,self.deck.showNext(), showNumber = False)
        
    
    def drawTile(self, painter, x, y, value, showNumber = True):
        if value == 1:
            color = QtGui.QColor(0xccccff)
        elif value == 2:
            color = QtGui.QColor(0xffcccc)
        else:
            color = QtGui.QColor(0xcccccc)
        
        rect = QtCore.QRectF(x+2,y+2,100-2,150-2)
        painter.fillRect(rect, color)
        
        painter.setPen(QtGui.QColor(168, 34, 3))
        painter.setFont(QtGui.QFont('Calibri', 40))
        if showNumber:
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(value))
        elif value > 3:
            painter.drawText(rect, QtCore.Qt.AlignCenter, '+')

class Deck(object):
    def __init__(self):
        self.cards = []
        self.reshuffle()
        
    def getCard(self,maxTile = 3):
        card = self.cards.pop()
        if random.randint(0,20) == 0 and maxTile >= 48: # add bonus card to stack
            bonusrank = int(log(maxTile/3)/log(2) - 3)
            bonuscards = [3*2**(i+1) for i in range(bonusrank)]
            self.cards.append(random.choice(bonuscards))
        if len(self.cards) == 0:
            self.reshuffle()
        return card
        
    def reshuffle(self):
        self.cards = [1,2,3]*4
        random.shuffle(self.cards)
        
    def showNext(self):
        return self.cards[-1]
        
    
       
def main():
    
    app = QtGui.QApplication([])
    game = Threes()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()