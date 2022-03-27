import sys
import os
from headers import *

def import_spreadsheet():

	#here = os.path.dirname(__file__)
	here = os.getcwd()
	files = os.listdir(here)
	tsv = []

	for i in files:
		s = i.split(sep='.')
		if s[len(s) - 1] == 'tsv':
			tsv.append(i)			
					
	tsv.append("Back")

						 
	infile = "-1"
					
	while int(infile) < 0 or int(infile) > len(tsv) - 1:
		try:
			menu("Select File", tsv)
		
			infile = input("Select an file (#) from list below to import spreadsheet: ")
		except ValueError:
			print("Please select item number from list above.\n")
			infile = "-1"

	games = []
	if int(infile) != len(tsv) - 1:

		try:
			formatted = False
			f = open(os.path.join(here, tsv[int(infile)]), 'r')

			header = f.readline()
			headers = header.split(sep='\t')

			hasspace = True
			while hasspace == True:
				try:
					headers.remove("")
				except ValueError:
					hasspace = False

			headers.insert(0, "ID")
			if headers[6] == "Road Decision" and headers[7] == "Home Decision":
				formatted = True
			elif headers[6] == "Road" and headers[7] == "Home":
				headers[6] = "Road Decision"
				headers[7] = "Home Decision"
				formatted = True
			else:
				formatted = False

			for line in f:
				sect = line.split(sep='\t')

				try:
					if int(sect[0]) >= 0:

						id=int(sect[0])
						away=sect[1]
						home=sect[2]
						lb=float(sect[3])
						ub=float(sect[4])
						spread=float(sect[5])
						awaydecR=sect[6]
						homedecR=sect[7]

						game = Game(id, away, home, lb, ub, spread, awaydecR, homedecR)
						game.decision()
						games.append(game)
				except ValueError:
					print("Could not import entry")

			f.close()
			if formatted == True:
				return games, headers[0:len(headers)-1], formatted
			else:
				return games, header, formatted
					
		except FileNotFoundError:
			print("Error finding specified file. Please try again.")
	else:
		return None, "Menu"

