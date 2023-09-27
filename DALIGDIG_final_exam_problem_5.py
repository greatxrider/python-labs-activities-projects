class Piece:
    
    def intro(self):
        print("\nEvery chess piece has different movement.")

class Rook(Piece):
    def move(self):
        print("Moving in a straight path.")

class Bishop(Piece):
    def move(self):
        print("Moving diagonally.")

class King(Piece):
    def move(self):
        print("Moving one step.")

class Knight(Piece):
    def move(self):
        print("Moving in a L-shaped path.")

class Queen(Piece):
    def move(self):
        print("Moving uniquely.")

class Pawn(Piece):
    def move(self):
        print("Moving one step ahead.")

if __name__ == "__main__":
    rook = Rook()
    rook.intro()
    rook.move()
    bishop = Bishop()
    bishop.intro()
    bishop.move()
    king = King()
    king.intro()
    king.move()
    knight = Knight()
    knight.intro()
    knight.move()
    queen = Queen()
    queen.intro()
    queen.move()
    pawn = Pawn()
    pawn.intro()
    pawn.move()