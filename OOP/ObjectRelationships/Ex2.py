# Player class
class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


# Team class contains a list of Player
# Objects
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)


# School class contains a list of Team
# objects.
class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def addTeam(self, teams):
        self.teams.append(teams)

    def getTotalPlayersInSchool(self):
        count = 0
        for team in self.teams:
            count += team.getNumberOfPlayers()
        return count


# Complete the implementation

# code to test the implementation
# remove backticks when you want to test the implemenation of your code
p1 = Player("Harris", 1, "Red");
p2 = Player("Carol", 2, "Red");

p3 = Player("Johnny", 1, "Blue");
p4 = Player("Sarah", 2, "Blue");

red_team = Team("Red Team")
red_team.players.append(p1)
red_team.players.append(p2)

blue_team = Team("Blue Team")
blue_team.players.append(p2)
blue_team.players.append(p3)

mySchool = School("My School")
mySchool.teams.append(red_team)
mySchool.teams.append(blue_team)

print("Total players in my school:", mySchool.getTotalPlayersInSchool())
