import sys
import os
from headers import * 

def print_entered_spreadsheet(games, headers, outfile):
	#here = os.path.dirname(__file__)
	here = os.getcwd()
	outfile += ".txt"
	try:
		f = open(os.path.join(here,outfile), 'w')
		sizes = []
		tempHead = []
		totalSize = 0
		for h in headers:
			if h[len(h) - 1] == '\n':
				tempHead.append(h[0:len(h) - 1])
			else:
				tempHead.append(h)

		headers = tempHead

		for h in headers:
			size = getSize(h, games) + 2
			sizes.append(size)
			totalSize += size

		totalSize += 7

		table = "+{}+\n".format('-' * totalSize)
		for h in headers:
			table += "|{header: ^{size:}}".format(header=h, size=sizes[headers.index(h)])
		table += "|\n"
		table += "+{}+\n".format('-' * totalSize)


		for game in games:
			table += "|{ID: ^{size:}}".format(ID=game.id, size=sizes[headers.index("ID")])
			table += "|{Road: ^{size:}}".format(Road=game.away, size=sizes[headers.index("Road")])
			table += "|{Home: ^{size:}}".format(Home=game.home, size=sizes[headers.index("Home")])
			table += "|{LB: ^{size:}}".format(LB=game.lb, size=sizes[headers.index("LB")])
			table += "|{UB: ^{size:}}".format(UB=game.ub, size=sizes[headers.index("UB")])
			table += "|{Spread: ^{size:}}".format(Spread=game.spread, size=sizes[headers.index("Spread")])
			table += "|{RoadDecision: ^{size:}}".format(RoadDecision=game.awaydec, size=sizes[headers.index("Road Decision")])
			table += "|{HomeDecision: ^{size:}}|\n".format(HomeDecision=game.homedec, size=sizes[headers.index("Home Decision")])
		
		table += "+{}+\n".format('-' * totalSize)

		#original_stdout = sys.stdout
		#sys.stdout=f
		f.write(table)
		#sys.stdout=original_stdout
		f.close()
	except FileNotFoundError:
		print("Error finding existing file.")


def print_spreadsheet_tsv(games, header, outfile):
	here = os.path.dirname(__file__)

	outfile += ".tsv"
	table = "{header}".format(header=header[0])
	
	for h in range(1, len(header)):
		table += "\t{header}".format(header=header[h])
	table += "\n"

	try:

		f = open(os.path.join(here,outfile), 'w')


		for game in games:
			#original_stdout = sys.stdout
			#sys.stdout=f
			table += "{id}\t{away}\t{home}\t{lb}\t{ub}\t{spread}\t{awaydec}\t{homedec}\n".format(
				   id=game.id, away=game.away, home=game.home, lb=game.lb, ub=game.ub,
				   spread=game.spread, awaydec=game.awaydec, homedec=game.homedec)

			#sys.stdout=original_stdout
#			if game.awaydec != game.awaydecR or game.homedec != game.homedecR:
#				print("{id}\t{away}\t{home}\t{lb}\t{ub}\t{spread}\t{awaydec}\t{homedec}".format(
#					id=game.id, away=game.away, home=game.home, lb=game.lb, ub=game.ub, 
#					spread=game.spread, awaydec=game.awaydec, homedec=game.homedec))

#				print("awaydec: {awaydec}\tshould be: {awaydecR}".format(awaydec=game.awaydec,
#											 awaydecR=game.awaydecR))
#				print("homedec: {homedec}\tshould be: {homedecR}\n".format(homedec=game.homedec,
#											   homedecR=game.homedecR))

		#sys.stdout=f
		#print("\n")
		#sys.stdout=original_stdout
		f.write(table)
		f.close()
	except FileNotFoundError:
		print("Error finding specified file. Please try again.")