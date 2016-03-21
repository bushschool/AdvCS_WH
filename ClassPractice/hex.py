class Board():
    """ Board for Hex """
    def __init__(self, size):
        self.height = size
        self.width = size
        self.tiles = [["O"] * self.width for row in range(self.height)]

    def __repr__(self):
        """
        :return: Prints the hex board
        """
        height = self.height
        width = self.width
        # makes the board print out diagonally
        output = ""
        output += " " * (height + 2)
        for col in range(width):
            output += str(col % 10) + " "
        output += "\n"
        # prints out the numbrz
        for row in range(height):
            output += " " * (height - row)
            output += str(row % 10)
            output += " "
            for col in range(width):
                output += self.tiles[row][col] + " "
            output += "\n"
        return output

    def legal(self, row, col):
        """
        :return: Checks to see if a move is legal
        """
        if self.tiles[row][col] == "O":
            return True
        else:
            return False

    def play(self, piece, row, col):
        """
        :return: places a piece of type piece on the board in the stated location
        """
        if self.legal(row,col):
            self.tiles[row][col] = piece
        else:
            return False

    def nodeCheck(self, type, row, col):
        # Assumes all neighbours are empty nodes
        """
          0  1
         2  O  3
           4  5
        """
        full = [False, False, False, False, False, False]
        try:
            if self.tiles[row-1][col-1] == type:
                full[0] = True
        except IndexError:
            full[0] = False
        try:
            if self.tiles[row-1][col] == type:
                full[1] = True
        except IndexError:
            full[1] = False
        try:
            if self.tiles[row][col-1] == type:
                full[2] = True
        except IndexError:
            full[2] = False
        try:
            if self.tiles[row][col+1] == type:
                full[3] = True
        except IndexError:
            full[3] = False
        try:
            if self.tiles[row+1][col] == type:
                full[4] = True
        except IndexError:
            full[4] = False
        try:
            if self.tiles[row+1][col+1] == type:
                full[5] = True
        except IndexError:
            full[5] = False
        return full

    def checkWinHz(self, type):
        checked = [["N"] * self.width for row in range(self.height)]
        more = False
        for i in range(self.height):
            if self.tiles[i][0] == type:
                checked[i][0] = "Y"
                reps = self.nodeCheck(type, i, 0)
                if reps[3] == True:
                    checked[i][1] = "P"
                    more = True
                try:
                    if reps[5] == True:
                        checked[i+1][1] = "P"
                        more = True
                except IndexError:
                    True
        while more == True:
            more = False
            for row in range(self.height):
                for col in range(self.height):
                    if checked[row][col] == "P":
                        if col == self.width - 1:
                            return True
                        checked[row][col] = "Y"
                        reps = self.nodeCheck(type, row, col)
                        try:
                            if (reps[0] == True) and (checked[row-1][col-1] != "Y"):
                                checked[row-1][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[1] == True) and (checked[row-1][col] != "Y"):
                                checked[row-1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[2] == True) and (checked[row][col-1] != "Y"):
                                checked[row][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[3] == True) and (checked[row][col+1] != "Y"):
                                checked[row][col+1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[4] == True) and (checked[row+1][col] != "Y"):
                                checked[row+1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[5] == True) and (checked[row+1][col+1] != "Y"):
                                checked[row+1][col+1] = "P"
                                more = True
                        except IndexError:
                            True
        return False

    def checkWinVt(self, type):
        checked = [["N"] * self.width for row in range(self.height)]
        more = False
        for i in range(self.width):
            if self.tiles[0][i] == type:
                checked[0][i] = "Y"
                reps = self.nodeCheck(type, i, 0)
                if reps[4] == True:
                    checked[1][i] = "P"
                    more = True
                try:
                    if reps[5] == True:
                        checked[1][i+1] = "P"
                        more = True
                except IndexError:
                    True
        while more == True:
            more = False
            for row in range(self.width):
                for col in range(self.width):
                    if checked[row][col] == "P":
                        if row == self.height - 1:
                            return True
                        checked[row][col] = "Y"
                        reps = self.nodeCheck(type, row, col)
                        try:
                            if (reps[0] == True) and (checked[row-1][col-1] != "Y"):
                                checked[row-1][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[1] == True) and (checked[row-1][col] != "Y"):
                                checked[row-1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[2] == True) and (checked[row][col-1] != "Y"):
                                checked[row][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[3] == True) and (checked[row][col+1] != "Y"):
                                checked[row][col+1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[4] == True) and (checked[row+1][col] != "Y"):
                                checked[row+1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[5] == True) and (checked[row+1][col+1] != "Y"):
                                checked[row+1][col+1] = "P"
                                more = True
                        except IndexError:
                            True
        return False

    def playGame(self):
        print("Player one is X, player 2 is W\nPlayer one goes first\n")
        print self
        while True:
            allowed = False
            p1row = int(input("Player 1, what row? "))
            p1col = int(input("Player 1, what column? "))
            allowed = self.legal(p1row, p1col)
            while not allowed:
                print("Illegal Move! Try again.")
                p1row = int(input("Player 1, what row? "))
                p1col = int(input("Player 1, what column? "))
                allowed = self.legal(p1row, p1col)
            self.play("X", p1row, p1col)
            print self
            if self.checkWinHz("X") == True:
                print("Player 1 Wins!")
                return
            allowed = False
            p2row = int(input("Player 2, what row? "))
            p2col = int(input("Player 2, what column? "))
            allowed = self.legal(p2row, p2col)
            while not allowed:
                print("Illegal Move! Try again.")
                p2row = int(input("Player 2, what row? "))
                p2col = int(input("Player 2, what column? "))
                allowed = self.legal(p2row, p2col)
            self.play("W", p2row, p2col)
            print self
            if self.checkWinVt("W") == True:
                print("Player 2 Wins!")
                return


test = Board(6)
test.playGame()
