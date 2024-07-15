import re
import chess


# yet unfinished 


class Tools:

    def __init__(self):
        self.games = self.Games()
        self.convert = self.Convert()
        self.moves = self.Moves()

    class Games:

        def __init__(self):
            pass

        def remove_movechars(self,game : str) -> str:
            '''
            Function to remove the move characters from the game.

            Params:
            game: str
                The game in standard algebraic notation.
            '''

            g = ''

            for el in game.split():
                if not el.endswith('.'):
                    g += el + ' '

            return g

        def remove_clock(gself,ame : str) -> str:
            '''
            Function to remove the clock from the game.

            Params:
            game: str
                The game in standard algebraic notation.
            '''

            game = re.sub(r'\{ \[%clk.*?\] \}', '', game)  
            game = re.sub(r'\{.*?\}', '', game)  
            for el in game.split():
                if el.endswith('...'):
                    game=game.replace(el, '')
            return game


        def remove_comments(self,game : str)-> str:
            '''
            Function to remove the comments from the game.

            Params:
            game: str
                The game in standard algebraic notation.
            '''
            game = re.sub(r'\{.*?\}', '', game)  
            return game

        def remove_score(self,game):
            '''
            Function to remove the score from the game.

            Params:
            game: str
                The game in standard algebraic notation.
            '''

            game = game.replace('1-0', '').replace('0-1', '').replace('1/2-1/2', '')
            return game

        def add_move_numbers(self,game : str) -> str:
            '''
            Function to add move numbers to the game.

            Params:
            game: str
                The game in standard algebraic notation.
            '''
            game = game.split()
            move_number = 1
            for i in range(len(game)):
                if i % 2 == 0:
                    game[i] = str(move_number) + '. ' + game[i]
                    move_number += 1
            return ' '.join(game)


    class Convert:

        def __init__(self):
            self.inst = Tools.Games()

        def san2figurine(self,moves : str, check_chars : bool = True, move_count : bool = True, pgn_tags : bool=True) -> str:
            '''
            Function to convert moves in standard algebraic notation to figurine notation.

            Params:
            moves: str
                The moves in standard algebraic notation

            check_chars: bool
                If False, remove the check, checkmate characters from the game. Default is True.

            move_count: bool
                If False, remove the move numbers from the game. Default is True.

            pgn_tags: bool
                If False, remove the PGN tags from the game. Default is True.

            '''

            assert isinstance(moves,str), 'Moves should be passed as str object'

            if check_chars == False:

                moves = moves.replace('#', '').replace('+', '')

            if move_count == False:

                moves = self.inst.remove_movechars(moves)

            if pgn_tags == False:

                moves = self.remove_score(moves)


            move_list = moves.split()

            new_moves = []

            for i, move in enumerate(move_list):

                if move[0] == 'N':   
                    new_moves.append('♘' + move[1:]) if i % 2 == 0 else new_moves.append('♞' + move[1:])

                elif move[0] == 'R':
                    new_moves.append('♖' + move[1:]) if i % 2 == 0 else new_moves.append('♜' + move[1:])

                elif move[0] == 'B':
                        new_moves.append('♗' + move[1:]) if i % 2 == 0 else new_moves.append('♝'+ move[1:])

                elif move[0] == 'Q':
                        new_moves.append('♕' + move[1:]) if i % 2 == 0 else new_moves.append('♛'+ move[1:])

                elif move[0] == 'K':

                        new_moves.append('♔'+ move[1:]) if i % 2 == 0 else new_moves.append('♚'+ move[1:])
                
                else:
                    new_moves.append(move)

            new_moves_str = ' '.join(new_moves)

            return new_moves_str


        def figurine2san(self,moves : str, check_chars :bool = True, move_count :bool = True, pgn_tags : bool =True ) -> str:
            '''
            Function to convert moves in figurine notation to standard algebraic notation.

            Params:
            moves: str
                The moves in figurine notation

            check_chars: bool
                If False, remove the check, checkmate characters from the game. Default is True.

            move_count: bool
                If False, remove the move numbers from the game. Default is True.

            pgn_tags: bool
                If False, remove the PGN tags from the game. Default is True.
            '''

            assert isinstance(moves,str), 'Moves should be passed as str object'

            if check_chars == False:

                moves = moves.replace('#', '').replace('+', '')

            if move_count == False:

                moves = self.inst.remove_movechars(moves)

            if pgn_tags == False:

                moves = self.inst.remove_score(moves)


            moves = moves.replace('♔', 'K').replace('♕', 'Q').replace('♖', 'R').replace('♗', 'B').replace('♘', 'N').replace('♚', 'K').replace('♛', 'Q').replace('♜', 'R').replace('♝', 'B').replace('♞', 'N')

            return moves


        def san2lan(self,game : str) -> str:
            '''
            Function to convert standard algebraic notation to long algebraic notation.

            Params:
            game: str
                The game in standard algebraic notation.
            '''

            l = []

            board = chess.Board()

            game = self.inst.remove_movechars(game)
            game = self.inst.remove_score(game)

            gierka = ' '.join([el for el in game.split() if not el.endswith('.')])

            for move in gierka.split():
                l.append((board.push_san(move)))

            z = [str(el) for el in l]

            return ' '.join([el for el in z])



        def figurine2lan(self,game : str) -> str:
            '''
            Function to convert figurine notation to long algebraic notation.

            Params:
            game: str
                The game in figurine notation.
            '''

            return self.inst.san2lan(self.inst.figurine2san(game))
        

        # converting from [1,1] to 'a1'

        def coord2board(self,curr:str) -> str:
            '''
            Function to convert from board coordinates to square notation. [1,1] -> 'a1'

            Params:
            curr: list
                The board coordinates.
            '''

            literki = ['xxx', 'a', 'b','c','d','e','f','g','h']

            cyferki = ['xxx', '1','2','3','4','5','6','7','8']

            return  literki[curr[0]] + cyferki[curr[1]]


        # converting from 'a1' to [1,1]


        def board2coord(self,curr:str) -> list:
            '''
            Function to convert from square notation to board coordinates. 'a1' -> [1,1]

            Params:
            curr: str
                The square notation.
            '''

            d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}


            return [d[curr[0]], int(curr[1])]



    class Moves:

        def __init__(self):
            self.inst = Tools.Convert()

        def knight_moves(self,position, squares : bool = True) -> list:
            '''
            generator function to generate all possible knight moves from passed square.

            Params:
            position: str
                The square to generate the moves from.
            
            '''

            if isinstance(position, str) == True:
                if position[0] not in 'abcdefgh' or position[1] not in '12345678':
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, list) == True:
                if position[0] not in range(1,9) or position[1] not in range(1,9):
                    raise ValueError('Invalid position passed.')
                elif len(position) != 2:
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, str) == True:
                position = self.inst.board2coord(position)

            l = []

            pos = [[-2, 1],
                [-1, 2],
                [1, 2],
                [2, 1],
                [2, -1],
                [1, -2],
                [-1, -2],
                [-2, -1]]
            
            for el in pos: 
                if position[0] + el[0] <= 8 and position[0] + el[0] >= 1 and position[1] + el[1] <= 8 and position[1] + el[1] >= 1:
                    l.append((position[0] + el[0], position[1] + el[1])) if not squares else l.append(self.inst.coord2board([position[0] + el[0], position[1] + el[1]]))

            return l

        def bishop_moves(self,position, squares : bool = True) -> list:
            '''
            generator function to generate all possible bishop moves from passed square.

            Params:
            position: str
                The square to generate the moves from.

            '''
            
            x,y,g,r = 1,1,1,1

            l = []

            if isinstance(position, str) == True:
                if position[0] not in 'abcdefgh' or position[1] not in '12345678':
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, list) == True:
                if position[0] not in range(1,9) or position[1] not in range(1,9):
                    raise ValueError('Invalid position passed.')
                elif len(position) != 2:
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, str) == True:
                position = self.inst.board2coord(position)

            while position[0] + x <= 8 and position[1] + x <= 8:
                l.append((position[0] + x, position[1] + y)) if not squares else l.append(self.inst.coord2board([position[0] + x, position[1] + y]))
                x += 1

            while position[0] - r >= 1 and position[1] - r >= 1:
                l.append((position[0] - r, position[1] - r)) if not squares else l.append(self.inst.coord2board([position[0] - r, position[1] - r]))
                r += 1

            while position[0] + y <= 8 and position[1] - y >= 1:
                l.append((position[0] + y, position[1] - y)) if not squares else l.append(self.inst.coord2board([position[0] + y, position[1] - y]))
                y += 1

            while position[0] - g >= 1 and position[1] + g <= 8:
                l.append((position[0] - g, position[1] + g)) if not squares else l.append(self.inst.coord2board([position[0] - g, position[1] + g]))
                g += 1

            return l
            

        def rook_moves(self,position, squares : bool = False) -> list:
            '''
            generator function to generate all possible rook moves from passed square.

            Params:
            position: str
                The square to generate the moves from.
            '''

            if isinstance(position, str) == True:
                if position[0] not in 'abcdefgh' or position[1] not in '12345678':
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, list) == True:
                if position[0] not in range(1,9) or position[1] not in range(1,9):
                    raise ValueError('Invalid position passed.')
                elif len(position) != 2:
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, str) == True:
                position = self.inst.board2coord(position)
            

            l = []

            x,y,g,r = 1,1,1,1

            while position[0] + x <= 8:
                l.append((position[0] + x, position[1])) if not squares else l.append(self.inst.coord2board([position[0] + x, position[1]]))
                x += 1

            while position[0] - r >= 1:
                l.append((position[0] - r, position[1])) if not squares else l.append(self.inst.coord2board([position[0] - r, position[1]]))
                r += 1

            while position[1] + y <= 8:
                l.append((position[0], position[1] + y)) if not squares else l.append(self.inst.coord2board([position[0], position[1] + y]))
                y += 1

            while position[1] - g >= 1:
                l.append((position[0], position[1] - g)) if not squares else l.append(self.inst.coord2board([position[0], position[1] - g]))
                g += 1

            return l

        def queen_moves(self,position, squares : bool = False) -> list:
            '''
            generator function to generate all possible queen moves from passed square.

            Params:
            position: str
                The square to generate the moves from.
            '''

            if isinstance(position, str) == True:
                if position[0] not in 'abcdefgh' or position[1] not in '12345678':
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, list) == True:
                if position[0] not in range(1,9) or position[1] not in range(1,9):
                    raise ValueError('Invalid position passed.')
                elif len(position) != 2:
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, str) == True:
                position = self.inst.board2coord(position)

            return self.inst.bishop_moves(position, squares) + self.inst.rook_moves(position, squares)

        def king_moves(self,position, squares : bool = True) -> list:
            '''
            generator function to generate all possible king moves from passed square.

            Params:
            position: str
                The square to generate the moves from.
            '''

            if isinstance(position, str) == True:
                if position[0] not in 'abcdefgh' or position[1] not in '12345678':
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, list) == True:
                if position[0] not in range(1,9) or position[1] not in range(1,9):
                    raise ValueError('Invalid position passed.')
                elif len(position) != 2:
                    raise ValueError('Invalid position passed.')
                
            if isinstance(position, str) == True:
                position = self.inst.board2coord(position)

            pos = [

                [1, 0],
                [0, 1],
                [-1, 0],
                [0, -1],
                [1, 1],
                [-1, 1],
                [-1, -1],
                [1, -1]

            ]

            l = []

            for el in pos:
                if position[0] + el[0] <= 8 and position[0] + el[0] >= 1 and position[1] + el[1] <= 8 and position[1] + el[1] >= 1:
                    l.append((position[0] + el[0], position[1] + el[1])) if not squares else l.append(self.inst.coord2board([position[0] + el[0], position[1] + el[1]]))

            return l

