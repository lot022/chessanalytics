import berserk

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
        self.board = self.__Board(self)

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


    class __Board:
        def __init__(self, inst):
            self.inst = inst


        
###  will finish it till the end of the week, both all API func and tools section 
