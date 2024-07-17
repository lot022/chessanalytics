import berserk
from datetime import datetime

# work in progress :))

class API:
    def __init__(self, token,name,max):
        self.token = token
        self.name = name
        self.max = max
        self.__session = berserk.TokenSession(token)
        self.client = berserk.Client(session=self.__session)
        self.games = self.__Games(self)
        self.openings = self.__Openings(self)
        self.statistics = self.__Statistical(self)
        self.moves = self.__Moves(self)
        self.captures = self.__Captures(self)
        self.overall = self.__Overall(self)
        self.wdl = self.__WDL(self)

    class __Games:

        def __init__(self, inst):
            self.inst = inst

        def get_games(self) -> list:

            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max)

            l = []
            
            for el in list(d):

                for k,v in el.items():
                    if k == 'moves':
                        l.append(v)
            return l
        
        def whitepc_games(self) -> list:
            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max//2, color='white')

            l = []

            for el in list(d):

                for k,v in el.items():
                    if k == 'moves':
                        l.append(v)
                        
            return l
        
        def blackpc_games(self) -> list:
            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max//2, color='black')

            l = []

            for el in list(d):

                for k,v in el.items():
                    if k == 'moves':
                        l.append(v)
                        
            return l
        
        def games_opening(self, opening) -> list:

            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)
            l = []

            for el in list(d):
                    
                for k,v in el.items():
                    if k == 'opening':
                        if v['name'] == opening:
                            for k,v in el.items():
                                if k == 'moves':
                                    l.append(v)

            return l
        
    class __Openings:
        def __init__(self, inst):
            self.inst = inst

        def count(self) -> dict:
            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max//2, opening=True)
            ret = {}
            for el in list(d):
                for k,v in el.items():
                    if k == 'opening':
                        if v['name'] not in ret:
                            ret[v['name']] = 0

                        ret[v['name']] += 1

            return ret
        
        def count_white(self) -> dict:
            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max//2, opening=True, color='white')
            ret = {}
            for el in list(d):
                for k,v in el.items():
                    if k == 'opening':
                        if v['name'] not in ret:
                            ret[v['name']] = 0

                        ret[v['name']] += 1

            return ret
        
        def count_black(self) -> dict:
            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max//2, opening=True, color='black')
            ret = {}
            for el in list(d):
                for k,v in el.items():
                    if k == 'opening':
                        if v['name'] not in ret:
                            ret[v['name']] = 0

                        ret[v['name']] += 1

            return ret
        

        def eco(self) -> dict:

            d = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)
            ret = {}
            for el in list(d):
                for k,v in el.items():
                    if k == 'opening':
                        if v['eco'] not in ret:
                            ret[v['eco']] = 0

                        ret[v['eco']] += 1

            return ret
        
        def starting_squares(self) -> dict:
            
            l = self.inst.games.get_games()

            fsqr, ret = [el.split()[0] for el in l], {}

            for el in fsqr:
                if el not in ret:
                    ret[el] = 0

                ret[el] += 1

            return ret
        
    class __Statistical:

        def __init__(self, inst):
            self.inst = inst

        def game_length(self) -> float:
            l = self.inst.games.get_games()
            return sum([len(el.split()) for el in l]) / len(l)
        
        def opponents_elo(self) -> float:
            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            cnt,c = 0,0

            for el in dt:
                for k,v in el.items():
                    if k == 'players':
                        w = v['white']['user']['name']

                        if w == self.inst.name:
                            cnt += v['black']['rating']
                            c += 1

                        else:
                            cnt += v['white']['rating']
                            c += 1

            return cnt / c
        
        
        def winrate_white(self) -> float:
            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            cnt,c = 0,0

            for el in dt:
                pl = 0
                for k,v in el.items():
                    if k == 'players':
                        if v['white']['user']['name'] == self.inst.name:
                            pl += 1

                    if k == 'winner' and pl == 1:
                        if v == 'white':
                            cnt += 1

                        c += 1

            return cnt/c
                        

        def winrate_black(self) -> float:
            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            cnt,c = 0,0

            for el in dt:
                pl = 0
                for k,v in el.items():
                    if k == 'players':
                        if v['black']['user']['name'] == self.inst.name:
                            pl += 1

                    if k == 'winner' and pl == 1:
                        if v == 'black':
                            cnt += 1

                        c += 1

            return cnt/c

        def ply(self) -> float:
            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            cnt,c = 0,0

            for el in dt:
                for k,v in el.items():
                    if k == 'opening':
                        cnt += v['ply']
                        c +=1
            
            return cnt / c
        
        def fastest_mate(self, game=True) -> float:
            dt = self.inst.games.get_games()
            
            gry = [el for el in dt if '#' in el]

            gry = sorted(gry, key=lambda x: len(x.split()))   

            return len(gry[0].split()) if not game else gry[0]
        
        def fastest_check(self, game=True) -> str:
            dt = self.inst.games.get_games()
            
            gry = [el for el in dt if '+' in el]

            gry = sorted(gry, key=lambda x: len(x.split()))   

            return len(gry[0].split()) if not game else gry[0]
        
        def shortest_game(self, game=True):
            dt = self.inst.games.get_games()

            gry = sorted(dt, key=lambda x: len(x.split()))

            return len(gry[0].split()) if not game else gry[0]
        
        def longest_game(self, game=True):
            dt = self.inst.games.get_games()

            gry = sorted(dt, key=lambda x: len(x.split()))

            return len(gry[-1].split()) if not game else gry[-1]

        def spearman_winrate_elo(self):
            pass

        def game_time(self):

            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            l = []

            for el in dt:
                s,f = 0,0
                for k,v in el.items():
                    
                    if k == 'createdAt':
                        s = v.strftime('%Y-%m-%d %H:%M:%S')

                    if k == 'lastMoveAt':
                        f = v.strftime('%Y-%m-%d %H:%M:%S')

                datetime_format = "%Y-%m-%d %H:%M:%S"

                z = (datetime.strptime(f, datetime_format) - datetime.strptime(s, datetime_format))
                l.append(z.total_seconds())

            return sum(l) / len(l)
                        
            

    class __Moves:

        def __init__(self, inst):
            self.inst = inst

        def queen(self):


            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if ruch[0] == 'Q':

                        ruch = ruch.replace('+', '').replace('#', '')

                        if len(ruch) == 3:
                            ruch = ruch[1:]
                        
                        elif len(ruch) == 4 and 'x' in ruch:
                            ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        

        def rook(self):


            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if ruch[0] == 'B':

                        ruch = ruch.replace('+', '').replace('#', '')

                        if len(ruch) == 3:
                            ruch = ruch[1:]
                        
                        elif len(ruch) == 4 and 'x' in ruch:
                            ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def bishop(self):

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if ruch[0] == 'B':

                        ruch = ruch.replace('+', '').replace('#', '')

                        if len(ruch) == 3:
                            ruch = ruch[1:]
                        
                        elif len(ruch) == 4 and 'x' in ruch:
                            ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def knight(self):


            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if ruch[0] == 'N':

                        ruch = ruch.replace('+', '').replace('#', '')

                        if len(ruch) == 3:
                            ruch = ruch[1:]
                        
                        elif len(ruch) == 4 and 'x' in ruch:
                            ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def king(self):


            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if ruch[0] == 'K':

                        if len(ruch) == 3:
                            ruch = ruch[1:]
                        
                        elif len(ruch) == 4 and 'x' in ruch:
                            ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def pawn(self):

            pawnlet = 'abcedfgh'

            l, d = self.inst.games.get_games(), {}

            for partia in l:
                for ruch in partia.split():
                    if ruch[0] in pawnlet:

                        ruch = ruch.replace('+', '').replace('#', '')

                        if len(ruch) == 3:
                            ruch = ruch[1:]
                        
                        elif len(ruch) == 4 and 'x' in ruch:
                            ruch = ruch[2:]

                        elif '=' in ruch:
                            ruch = ruch.split('=')[0]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        

    class __Captures:

        def __init__(self, inst):
            self.inst = inst

        def queen(self):

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if 'x' in ruch and ruch[0] == 'Q':

                        ruch = ruch.replace('+', '').replace('#', '')

                        ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        

        def bishop(self):

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if 'x' in ruch and ruch[0] == 'B':

                        ruch = ruch.replace('+', '').replace('#', '')

                        ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def knight(self):

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if 'x' in ruch and ruch[0] == 'N':

                        ruch = ruch.replace('+', '').replace('#', '')

                        ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def rook(self):

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if 'x' in ruch and ruch[0] == 'R':

                        ruch = ruch.replace('+', '').replace('#', '')

                        ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d
        
        def king(self):

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if 'x' in ruch and ruch[0] == 'K':

                        ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d

        def pawn(self):

            pawnlet = 'abcedfgh'

            l, d = self.inst.games.get_games(), {}
            
            for partia in l:
                for ruch in partia.split():
                    if 'x' in ruch and ruch[0] in pawnlet:

                        ruch = ruch.replace('+', '').replace('#', '')

                        if '=' in ruch:
                            ruch = ruch.split('=')[0]

                        ruch = ruch[2:]

                        if len(ruch) == 2:
                            if ruch not in d:
                                d[ruch] = 0

                            d[ruch] += 1

            return d


    class __Overall:
        
        def __init__(self,inst):
            self.inst = inst

        def speed(self):
            g = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in g:
                for k,v in el.items():
                    if k=='speed':
                        if v not in d:
                            d[v] = 0

                        d[v] += 1

            return d
        
        def terminations(self):

            g = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in g:
                for k,v in el.items():
                    if k=='status':
                        if v not in d:
                            d[v] = 0

                        d[v] += 1

            return d
        
        def sources(self):

            g = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in g:
                for k,v in el.items():
                    if k=='source':
                        if v not in d:
                            d[v] = 0

                        d[v] += 1

            return d
        
        def date(self):
            
            g = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in g:
                for k,v in el.items():
                    if k=='lastMoveAt':
                        z = v.strftime('%Y-%m-%d')
                        if z not in d:
                            d[z] = 0

                        d[z] += 1

            return d
        
        def hour(self):

            g = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in g:
                for k,v in el.items():
                    if k=='lastMoveAt':
                        z = v.strftime('%H')
                        if z not in d:
                            d[z] = 0

                        d[z] += 1

            return d
        
        def part_day(self) -> dict:

            dt = self.inst.overall.hour()

            d = {'morning':0, 'afternoon':0, 'evening':0, 'night':0}

            for k,v in dt.items():
                if int(k) >= 6 and int(k) < 12:
                    d['morning'] += v
                elif int(k) >= 12 and int(k) < 18:
                    d['afternoon'] += v
                
                elif int(k) >= 18 and int(k) < 24:
                    d['evening'] += v

                else:
                    d['night'] += v

            return d
        
        def time_control(self):

            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in dt:

                czas = '' 

                for k,v in el.items():

                    if k == 'clock':
                        
                        czas = str(v['initial']) + '+' + str(v['increment'])

                        if czas not in d:
                            d[czas] = 0

                        d[czas] += 1

            return d



    class __WDL:
        def __init__(self, inst):
            self.inst = inst

        def speed(self):

            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {'bullet': [0,0,0], 'blitz':[], 'rapid':[], 'classical':[]}

            for el in dt:
                typ, kolor = 0,0
                for k,v in el.items():
                    if k == 'speed':
                        typ = v

                    if k == 'players':
                        if v['white']['user']['name'] == self.inst.name:
                            kolor = 'white'
                        else:
                            kolor = 'black'

                    if k == 'winner':

                        if v == kolor:
                            d[typ][0] += 1

                        elif v == 'draw':
                            d[typ][1] += 1

                        else:
                            d[typ][2] += 1
            
            return d
        
        def time_control(self):
        
            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in dt:
                czas,kolor,win = '', '', 0
                for k,v in el.items():
                    if k == 'players':
                        if v['white']['user']['name'] == self.inst.name:
                            kolor = 'white'
                        else:
                            kolor = 'black'

                    if k == 'winner':
                        if v == kolor:
                            win += 1

                        elif v == 'draw':
                            win += 2

                        else:
                            win -=1

                    if k == 'clock':
                        czas = str(v['initial']) + '+' + str(v['increment'])

                        if czas not in d:
                            d[czas] = [0,0,0]

                if win == 1:
                    d[czas][0] += 1

                elif win == 2:
                    d[czas][1] += 1

                else:
                    d[czas][2] += 1

            return d
        

        def date(self):

            dt  = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in dt:
                data,kolor,win = '', '', 0
                for k,v in el.items():
                    if k == 'players':
                        if v['white']['user']['name'] == self.inst.name:
                            kolor = 'white'
                        else:
                            kolor = 'black'

                    if k == 'winner':
                        if v == kolor:
                            win += 1

                        elif v == 'draw':
                            win += 2

                        else:
                            win -=1

                    if k == 'lastMoveAt':
                        data = v.strftime('%Y-%m-%d')

                        if data not in d:
                            d[data] = [0,0,0]

                if win == 1:
                    d[data][0] += 1

                elif win == 2:
                    d[data][1] += 1

                else:
                    d[data][2] += 1

            return d

        def hour(self):
                
            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in dt:
                godzina,kolor,win = '', '', 0
                for k,v in el.items():
                    if k == 'players':
                        if v['white']['user']['name'] == self.inst.name:
                            kolor = 'white'
                        else:
                            kolor = 'black'

                    if k == 'winner':
                        if v == kolor:
                            win += 1

                        elif v == 'draw':
                            win += 2

                        else:
                            win -=1

                    if k == 'lastMoveAt':
                        godzina = v.strftime('%H')

                        if godzina not in d:
                            d[godzina] = [0,0,0]

                if win == 1:
                    d[godzina][0] += 1

                elif win == 2:
                    d[godzina][1] += 1

                else:
                    d[godzina][2] += 1

            return d
        

        def part_day(self) -> dict:

            dt = self.inst.wdl.hour()

            d = {'morning': [0,0,0], 'afternoon': [0,0,0], 'evening': [0,0,0], 'night': [0,0,0]}

            for k,v in dt.items():
                for i in range(3):
                    if int(k) >= 6 and int(k) < 12:
                        d['morning'][i] += v[i]
                    elif int(k) >= 12 and int(k) < 18:
                        d['afternoon'][i] += v[i]
                    
                    elif int(k) >= 18 and int(k) < 24:
                        d['evening'][i] += v[i]

                    else:
                        d['night'][i] += v[i]

            return d
        
        def elo(self):

            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            for el in dt:
                elo,kolor,win = 0, '', 0
                for k,v in el.items():
                    if k == 'players':
                        if v['white']['user']['name'] == self.inst.name:
                            kolor = 'white'
                            elo = round(v['white']['rating'],-2)
                        else:
                            kolor = 'black'
                            elo = round(v['black']['rating'],-2)

                    if k == 'winner':
                        if v == kolor:
                            win += 1

                        elif v == 'draw':
                            win += 2

                        else:
                            win -=1

                    if elo not in d:
                        d[elo] = [0,0,0]

                if win == 1:
                    d[elo][0] += 1

                elif win == 2:
                    d[elo][1] += 1

                else:
                    d[elo][2] += 1

            return d
        
        def opening(self, defined=True):

            dt = self.inst.client.games.export_by_player(self.inst.name, as_pgn=False, max=self.inst.max, opening=True)

            d = {}

            if not defined:

                for el in dt:
                    opening,kolor,win = '', '', 0
                    for k,v in el.items():
                        if k == 'players':
                            if v['white']['user']['name'] == self.inst.name:
                                kolor = 'white'
                            else:
                                kolor = 'black'
                            
                        if k == 'opening':
                            opening = v['name']

                            if opening not in d:
                                d[opening] = [0,0,0]

                        if k == 'winner':
                            if v == kolor:
                                win += 1

                            elif v == 'draw':
                                win += 2

                            else:
                                win -=1

                    if win == 1:
                        d[opening][0] += 1

                    elif win == 2:
                        d[opening][1] += 1

                    else:
                        d[opening][2] += 1


            else:

                for el in dt:
                    opening,kolor,win = '', '', 0
                    for k,v in el.items():
                        if k == 'players':
                            if v['white']['user']['name'] == self.inst.name:
                                kolor = 'white'
                            else:
                                kolor = 'black'
                            
                        if k == 'opening':
                            if ':' in v['name']:
                                opening = v['name'].split(':')[0]

                            if opening not in d:
                                d[opening] = [0,0,0]

                        if k == 'winner':
                            if v == kolor:
                                win += 1

                            elif v == 'draw':
                                win += 2

                            else:
                                win -=1

                    if win == 1:
                        d[opening][0] += 1

                    elif win == 2:
                        d[opening][1] += 1

                    else:
                        d[opening][2] += 1

            return d
        
        
###  will finish it till the end of the week, both all API func and tools section 
