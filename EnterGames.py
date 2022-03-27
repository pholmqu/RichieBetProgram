import os
import sys
from headers import *

def enter_games():
	#headers = ['ID', 'Road', 'Home', 'LB', 'UB', 'Spread', 'Road Decision', 'Home Decision']
	header = "ID\tRoad\tHome\tLB\tUB\tSpread\tRoad Decision\tHome Decision\n"
	headers = header.split(sep='\t')

	enter_team = 'y'
	games = []
	id = 1

	while enter_team == 'y':
		valid = False
		while valid == False:
			try:
				enter_team = ''
				road_team = input("Enter Road team name: ")
				home_team = input("Enter Home team name: ")
				lb = float(input("Enter Lower Bet: "))
				ub = float(input("Enter Upper Bet: "))
				spread = float(input("Enter spread: "))

				game = Game(id, road_team, home_team, lb, ub, spread, "", "")
				game.decision()
				games.append(game)

				id += 1
				valid = True

			except ValueError:
				print("Please enter the correct data as follows:\nRoad Team - Team Name\n" \
				      "Home Team - Team Name\nLower Bet - Number\nUpper Bet - Number\nSpread - Number\n")
				valid = False
		
		while enter_team != 'y' and enter_team != 'n':
			try:
				enter_team = input("Would you like to enter another game's info? y or n: ")
			except ValueError:
				print("Please enter y or n.")
	
	return games, headers
		
		

		


