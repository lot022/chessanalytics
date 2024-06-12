# Chess Analytics

Library to perform simple operations from input file containing chess games.

# Install 

      $ pip install chessanalytics

# Usage

### Import CA from chessanalytics and initialize Chess Analytics class

When initializing class as first parameter pass the path to file with your chess games and specify username of the player whose games you want to analyse.

      from chessanalytics import CA

      ca = CA(path_to_file, username)



# Game manipulation related functions

### pure_moves

Extracts all games from a file and returns them in the format of pure moves.


     ca.pure_moves()

     ['b3 c5 Bb2 d6 e3 e5 Bb5+ Bd7 Bxd7+ Nxd7 Ne2', 'e4 e6 d4 g6 c4 Bg7 Nf3 Nf6 Nc3 d6']


### game_without_movechars

Returns game without move characters.

     ca.game_without_movechars('1. b3 c5 2. Bb2 d6 3. e3 e5 4. Bb5+ Bd7 5. Bxd7+ Nxd7')

     b3 c5 Bb2 d6 e3 e5 Bb5+ Bd7 Bxd7+ Nxd7

### whitepc_games

Returns games played by player with white pieces.

      ca.whitepc_games()
      ['1. Nf3 Nf6 2. g3 g6 3. Bg2 Bg7 4. O-O O-O 5. d4 d5', '1. Nf3 c5 2. g3 Nc6 3. Bg2 Nf6 4. O-O g6' ]

### blackpc_games

Returns games played by player with black pieces.

      ca.blackpc_games()
      ['1. d4 e6 2. c4 b6 3. Nc3 Bb4 4. e3 Bb7', '1. d4 Nf6 2. c4 b6 3. Nc3 Bb7 4. d5 e6 5. e4 Bb4']
      
### games_opening

Extracts games from a file and returns only the games that feature a specific opening.

       ca.games_opening('Nimzo-Larsen Attack')
       ['1. b3 g6 2. Bb2 Nf6 3. e3 Bg7 4. Be2 O-O 5. Nc3 d6, '1. b3 g6 2. Bb2 Nf6 3. e3 Bg7 4. Be2 d6 5. Nc3 O-O']

### games_date

Returns games played by player on certain date. Date should be passed in yyyy/mm/dd format [ISO 8601 standard]

       ca.games_date('2024.05.31')
       ['1. e4 e5 2. Nf3 Nf6 3. Nc3 Nc6 4. d4 Bb4 5. dxe5 Bxc3+', '1. b3 e6 2. Bb2 a6 3. e3 b5 4. f4 c5 5. c4 d6']


# Statistical / Average related functions

### game_length

Returns average of moves for all games in file.

     ca.game_length()

     22.0



### squares_with_captures

Returns the squares where caption was made.

     ca.squares_With_captures()

     {'d7': 2, 'e5': 12, 'b6': 4, 'f8': 2, 'f5': 2, 'g7': 2, 'd5': 7, 'e7': 1, 'g5': 1}



### squares_with_Pawncaptures

Returns the squares where caption was made by a pawn. The functions identical to this one are: squares_with_Bishopcaptures, squares_with_Knightcaptures, 
squares_with_Queencaptures, squares_with_Kingcaptures, squares_with_Rookcaptures.


     ca.squares_with_Pawncaptures()

     {'e5': 5, 'b6': 2, 'd5': 3, 'e4': 2, 'e3': 2, 'g4': 1}

### opponent_elo

Returns elo of average opponent.

       ca.opponent_elo()
       1970.222

### white_black_total

Returns games played with white pieces,black pieces and total games.
       
       ca.white_black_total()
       [504, 496, 1000]

### xth_move

Returns dictionary withfrequency of x'th move of the game.

       ca.xth_move(move)
       {'Ne2': 1, 'f3': 1, 'Bb5': 1, 'Nf3': 1, 'e5': 1}

### xth_move_opening

Returns dictionary with frequency of x'th move of the game featuring specific opening.

       ca.xth_move_opening(move,opening)
       {'Nxd7': 1, 'Bf5': 1}


### xth_move_square

Returns dict with square of x'th move.

       ca.xth_move_square(move)
       {'c3': 102, 'O-O': 76, 'e3': 33, 'h3': 25, 'e1': 10}

### ranked_unranked

Returns amount of ranked and unranked games played by player.

       ca.ranked_unranked()
       {'Ranked': 837, 'Unranked': 163}

# Overall related functions 

### game_types

Returns variants of games played by player.

      ca.game_types()
      {'Standard': 1000}


### time_control

Returns time control of games played by player.


     ca.type_control()
     {'180+0': 612, '60+0': 237, '180+2': 78, '300+3': 5, '300+0': 63, '1500+10': 3, '900+10': 2}

### count_of_gamesDate

Returns count of games played in specific date.

     ca.count_of_gamesDate
     {'2024.05.25': 4, '2024.05.17': 6, '2024.05.14': 2, '2024.05.13': 2, '2024.05.12': 18}

### count_of_gamesTime

Returns count of games played in specific date.

     ca.count_of_gamesTime
     {'23': 124, '22': 112, '20': 164, '19': 148, '17': 42, '11': 35, '21': 137}

### termination_stats

Returns way in which games has ended.

     ca.termination_stats()
     {'Normal': 868, 'Time forfeit': 130, 'Abandoned': 2}


# Function related to player stats

### blitz_progress

Returns player's blitz progress. Same functions for different time controls are bullet_progress and rapid_progress.

     ca.blitz_progress()
     ['3001', '3002', '3004', '3005', '3006', '3007', '3008', '3000', '3003', '3007']

### blitz_progress_date

Returns player's progress on certain date. Same functions for different time controls are bullet_progress_date and rapid_progress_date.

      ca.blitz_progress_date()
      {'2024.05.25': 6, '2024.05.17': 0, '2024.05.14': 6, '2024.05.13': 2, '2024.05.12': -7}

### blitz_progress_hour

Returns player's progress on certain date. Same functions for different time controls are bullet_progress_hour and rapid_progress_hour.

      ca.blitz_progress_hour()
      {'23': -14, '22': 8, '20': 82, '19': -24, '17': -29, '11': -20, '21': 92}

### win_percentage_white


Returns player's win percentage while playing with white pieces.

      ca.win_percentage_black()
      0.685

### win_percentage_black

Returns player's win percentage while playing with black pieces.

      ca.win_percentage_black()
      0.216

### win_percentage_opponent

Returns player's win percentage against exact opponent.

       ca.win_percentage_opponent('player03')
       0.5

### common_opponents

Returns list of players in descending order that analyzing player has faced. Parameter 'amount' helps specifing how many opponents to be returned.

       ca.common_opponents(amount=5)
       {'player01': 40, 'player02': 37, 'player03': 30, 'player04': 30, 'player05': 16}


# Win/Draw/Loss related functions

### WDL_date()

Returns player's WDL stats on exact date.

      ca.WDL_date
      {'2024.05.25': [3, 1, 0], '2024.05.17': [4, 1, 1]}

### WDL_Time()

Returns player's WDL stats on exact hour.

     ca.WDL_Time()
     {'23': [80, 18, 26], '22': [63, 18, 31], '20': [111, 24, 29], '19': [102, 20, 26], '17': [24, 5, 13]}


### WDL_Part

Returns player's WDL stats on exact part of the day.

       ca.WDL_Part()
       {'Morning': [49, 16, 7], 'Afternoon': [112, 42, 29], 'Evening': [464, 153, 68], 'Noon': [24, 6, 3]}

### WDL_Day

Returns player's WDL stats on exact day of the week.

      ca.WDL_Day()
      {'Saturday': [39, 9, 6], 'Friday': [51, 12, 14], 'Tuesday': [136, 18, 30], 'Monday': [85, 15, 43]}

### WDL_Opening

Returns player's WDL stats by opening.

      ca.WDL_opening()
      {'Nimzo-Larsen Attack': [2, 0, 0], 'Russian Game': [0, 0, 1], "Bishop's Opening": [0, 0, 1], 'French Defense': [0, 0, 1]}

### WDL_Stats

Returns player's total WDL stats.

      ca.WDL_Stats()
      (674, 118, 208)

### WDL_opponent

Returns player's WDL stats with all the players that he had faced. Ordered by number of the wins and returned in descending order. Amount is a parameter that specifies how many players to be returned - if set to None, function returns full dictionary of players.

       ca.WDL_opponent(amount=4)
       {'player01': [23, 2, 12], 'player02': [22, 3, 5], 'player03': [21, 3, 6], 'player04': [13, 1, 1]}

### WDL_accurate_elo

Returns player's WDL stats against players with specific elo.

       ca.WDL_accurate_elo(2900)
       [28, 8, 22]

### WDL_elo

Returns player's WDL against player in all elo-ranges that appeared in file.

       ca.WDL_elo()
       {2600: [137, 15, 25], 2800: [137, 24, 47], 2700: [206, 50, 67], 1400: [2, 0, 0], 2500: [25, 2, 6]}



# Functions related to openings

### detailed_openings

Returns count of openings played by player inclunding variant of opening if appeared.

      ca.detailed_openings()
      {'Nimzo-Larsen Attack': 23, 'Englund Gambit Complex: Englund Gambit': 5, 'Nimzo-Larsen Attack: Modern Variation': 7}


### not_detailed_openings

Returns count of openings played by player not including variants.

     ca.not_detailed_openings()
     {'Nimzo-Larsen Attack': 53, 'Englund Gambit Complex': 5, 'Four Knights Game': 6}

### openings_ECO


Returns player's count of openings specified by their ECO code.

      ca.openings_ECO()
      {'A': 80, 'C': 18, 'E': 1, 'B': 1}

### starting_squares


Returns dictionary of first moves.

      ca.starting_squares()
      {'b3': 53, 'd4': 16, 'e4': 18, 'Nf3': 4, 'a3': 1, 'f4': 2, 'g3': 2, 'c4': 1, 'd3': 1, 'e3': 2}


### openings_with_white

Returns count of openings played by player while playing as white

       ca.openings_with_white()
       {'Nimzo-Larsen Attack: Classical Variation': 2, 'Nimzo-Larsen Attack': 2}


### openings_with_black

Returns count of openings played by player while playing as black

       ca.openings_with_black()
       {'Sicilian Defense: Bowdler Attack': 1, 'Zukertort Opening: Nimzo-Larsen Variation': 1, "Van't Kruijs Opening": 1, "Bishop's Opening: Vienna Hybrid": 1}


      
#
#     API FUNCTIONS
 
 These functions use Lichess API. You can read more about Lichess API on their website -> https://lichess-org.github.io/berserk/ or check their project site on pypi -> https://pypi.org/project/berserk/. Consider following safety rules when operating with API tokens as being carefuless may lead to unwanted behaviour like losing access to your account. Remember not to share your token with anyone.

 # Initialize Chess Analytics class with API functions

       ca = CA(path_to_file, username, 'lichess_API_token')





      
