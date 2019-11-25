'''
Observer pattern designs example

It uses when have objects that depend on other, needing to be notify
in case occurs any change in itself
'''

class Server:
    def __init__(self):
        self._players  = []

    def register(self, player):
        print('New player has arrived at server: {}'.format(player))
        self._players.append(player)

    def notifyAll(self, *args, **kwargs):
        for player in self._players:
            player.notify(self, *args, **kwargs)

class Spartan:
    def __init__(self, Server):
        Server.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__," --> Got ", args, " From ", Server)
        print("New Spartan member has arrived to fight")

class Covenant:
    def __init__(self, Server):
        Server.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__," --> Got ", args, " From ", Server)
        print("New Covenant member has arrived to fight")
        
HaloServer = Server()
team1 = []
for i in range(10):
    team1.append(Spartan(HaloServer))
print(" ")
team2 = []
for i in range(10):
    team2.append(Covenant(HaloServer))
print(" ")
HaloServer.notifyAll("New players has arrived to match")
