import xml.etree.ElementTree as et
import unittest

class NQueens:
    def __init__(self, sizeOfBoard):
        self.sizeOfBoard = sizeOfBoard
        self.board = [[0 for x in range(self.sizeOfBoard)] for x in range(self.sizeOfBoard)]                
        self.colCount = 0
        self.placements = 0
        self.backtracks = 0
        
    def parser(self, filename):
        
        tree = et.parse(filename)
        matrix = tree.getroot()
        
        for row in range(self.sizeOfBoard):
            for col in range(self.sizeOfBoard):
                try:
                    if matrix[row][col].text=="1":
                        return row,col
                except:
                    return -1, -1
                
        return -1,-1
        
                
                
    def isSafe(self, row, col):
        
        for i in range(col):
            if self.board[row][i] == 1:
                #print "Row ",row, " Col ",col," Attack : Horizontal"
                return False
            
            
        for i in range(row):
            if self.board[i][col] == 1:
                #print "Row ",row, " Col ",col," Attack : Vertical"
                return False
            
            
        currentRow = row
        currentCol = col
        
        while currentRow >= 0 and currentCol >= 0:
            if self.board[currentRow][currentCol] == 1:
                #print "Row ",row, " Col ",col," Attack : upper left dig"
                return False
            
            currentRow -= 1
            currentCol -= 1
            
            
        currentRow = row
        currentCol = col
        
        while currentRow < self.sizeOfBoard and currentCol < self.sizeOfBoard:
            if self.board[currentRow][currentCol] == 1:
                #print "Row ",row, " Col ",col," Attack : lower right dig"
                return False
            
            currentRow += 1
            currentCol += 1
            
            
        currentRow = row 
        currentCol = col
        
        while currentRow < self.sizeOfBoard and currentCol >= 0:
            if self.board[currentRow][currentCol] == 1:
                #print "Row ",row, " Col ",col," Attack : lower left dig"
                return False
            
            currentRow += 1
            currentCol -= 1
        
        currentRow = row
        currentCol = col
        
        while currentRow >= 0 and currentCol < self.sizeOfBoard:
            if self.board[currentRow][currentCol] == 1:
                #print "Row ",row, " Col ",col," Attack : upper right dig"
                return False
            
            currentRow -= 1
            currentCol += 1
           
        return True
        
        
        
    def solveNQueens(self, col):
        if self.colCount >= self.sizeOfBoard:
            print "Solution found !"
            print "Total placements made :", self.placements
            print "Total backtracks made :", self.backtracks
            return True
        
        for row in range(self.sizeOfBoard):
            
            if self.isSafe(row, col):
                self.board[row][col] = 1 
                self.colCount += 1
                self.placements += 1
                
                                    
                if self.solveNQueens((col+1)%self.sizeOfBoard):
                    return True
                
                self.backtracks += 1
                #Backtracking here because failed to place queen
                self.board[row][col] = 0
                self.colCount -= 1
                
                
        return False
                
                
            
        
    def NQueensDriver(self, filename):
        
        startRow, startCol = self.parser(filename)
        
        if startRow==-1 and startCol==-1:
            print "Error in Input !"
            return False
        else:
            self.board[startRow][startCol] = 1
            self.colCount += 1
            print self.colCount
        
        if self.solveNQueens((startCol+1)%self.sizeOfBoard) == False:
            self.printBoard()
            print "Solution doesn't exist !"
            return False
        
        self.printBoard()
        return True
        
    def printBoard(self):
        for row in self.board:
            print row
            
        
#n = NQueens(8)
#n.NQueensDriver("negativematrix2.xml")

class Testing(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(NQueens(8).NQueensDriver("positivematrix.xml"), True)
    
    def test_negative(self):
        self.assertEqual(NQueens(8).NQueensDriver("negativematrix2.xml"), False)
        
    def test_negative2(self):
        self.assertEqual(NQueens(3).NQueensDriver("negativematrix.xml"), False)
        
         
if __name__=="__main__":
    unittest.main()
    
