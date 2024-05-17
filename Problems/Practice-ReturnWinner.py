'''
We're asked to imagine there is an algorithms tournament in which multiple teams compete against each other. In each competition there will be two teams that compete. There will be one winner and one loser out of all of these competitions and there are no ties. Each team will compete against all other teams exactly once. A team gets 3 points for each competition it wins and 0 points for each competition it loses. It's guaranteed that the tournament always has at least two teams and there will be only one tournament winner.

We are given two inputs, the competitions array and the results array. We need to write a function that returns the winner of the tournament, or more specifically, the name of the team that has the most number of points. The competitions array is an array of pairs, representing all of the competitions in the tournament. Inside of these pairs, we have two strings: the first one is the name of the home team and the second one is the name of the away team. The results array represents the winner of each of these competitions. Inside the results array, a 1 means that the home team won and a 0 means the away team won. The results array is the same length as the competitions array, and the indices in the results array correspond with the indices in the competitions array.


competitions = [
    0 ["HTML", "C#"],
    1 ["C#", "Python"],
    2 ["Python", "HTML"],
]

first is home, second is away
           0  1  2 

results = [0, 0, 1] 




Python is the winner 
C# beats HTML, Python beats C#, and Python beats HTML

HTML - 0 points 
C# - 3 points 
Python - 6 points


competitions = [
   0 ["HTML", "C#"],
   1 ["C#", "Python"],
   2 ["Python", "HTML"],
]


competitions[i] = 0 = ["HTML", "C#"] 



'''
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]

results = [0, 0, 1]

HOME_TEAM_WINS = 1
def returnWinner(competitions, results):
    current_best_team = ""
    scoreboard = { current_best_team: 0 } 

    for i, competition in enumerate(competitions):

        home_team, away_team = competition
        result = results[i]
        current_winner = home_team if HOME_TEAM_WINS == result else away_team
        update_scoreboard(current_winner, scoreboard, 3)

        if scoreboard[current_winner] > scoreboard[current_best_team]: 
            current_best_team = current_winner

    return current_best_team


def update_scoreboard(team, scoreboard, points): 
    scoreboard[team] = scoreboard.get(team, 0) + points

    # for num in results:
    #     if num == 0:
    #         winIndex = 1
    #     elif num == 1:
    #         winIndex = 0
    #     for i in range(len(competitions)):
    #         dict[competitions[i][winIndex]] += 3

    # print(dict.values())

print(returnWinner(competitions, results))