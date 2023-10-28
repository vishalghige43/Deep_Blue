from const import*
from square import*
from piece import*
class Board:
    
    def __init__(self):
        self.square=[[0,0,0,0,0,0,0,0] for col in range(COLM)]
        self._create()
        self.add_peices("white")
        self.add_peices("black")

    def _create(self):
        for row in range(ROWS):
            for col in range(COLM):
                self.square[row][col]=Square(row,col)
            
    def add_peices(self,color):
        row_pawn,row_other=(6,7)if color=="white" else (1,0)

        for col in range(COLM):
            self.square[row_pawn][col]=Square(row_pawn,col,Pawn(color))

        self.square[row_other][0]=Square(row_other,0,Rook(color))
        self.square[row_other][7]=Square(row_other,7,Rook(color))

        self.square[row_other][1]=Square(row_other,1,Knight(color))
        self.square[row_other][6]=Square(row_other,6,Knight(color))

        self.square[row_other][2]=Square(row_other,2,Bishop(color))
        self.square[row_other][5]=Square(row_other,5,Bishop(color))

        self.square[row_other][3]=Square(row_other,3,Queen(color))
        self.square[row_other][4]=Square(row_other,4,King(color))



    
