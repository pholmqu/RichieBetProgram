import sys
import os
class Game:


	def decision(self):
	
		#if abs(float(self.lb)) > abs(float(self.spread)):
		#	self.awaydec = "avoid"
		#elif abs(float(self.lb)) < abs(float(self.spread)):
		#	self.awaydec = "avoid"
		#else:
		#	self.awaydec = "BET"

		#if abs(float(self.spread)) - abs(float(self.lb)) >= 0:
		#	self.awaydec = "BET"
		#else:
		#	self.awaydec = "avoid"

		#if abs(float(self.spread)) - abs(float(self.ub)) >= 0:
		#	self.homedec = "BET"
		#else:
		#	self.homedec = "avoid"

		#if float(self.ub) < 0:
		#	if float(self.spread) <= float(self.ub):
		#		self.homedec = "BET"
		#	else:
		#		self.homedec = "avoid"
		#elif float(self.ub) > 0:
		#	if float(self.spread) >= float(self.ub):
		#		self.homedec = "BET"
		#	else:
		#		self.homedec = "avoid"
		#else:
		#	self.homedec = "avoid" 


		# THIS WORKS BEST SO FAR
		if float(self.lb) < 0:
			if float(self.spread) <= float(self.lb):
				self.awaydec = "BET"
			else:
				self.awaydec = "avoid"
		elif float(self.lb) > 0:
			if float(self.spread) >= float(self.lb):
				self.awaydec = "BET"
			else:
				self.awaydec = "avoid"
		else:
			self.awaydec = "avoid"

		if float(self.ub) < 0:
			if float(self.spread) <= float(self.ub):
				self.homedec = "BET"
			else:
				self.homedec = "avoid"
		elif float(self.ub) > 0:
			if float(self.spread) >= float(self.ub):
				self.homedec = "BET"
			else:
				self.homedec = "avoid"
		else:
			self.homedec = "avoid"

		
		
		#if float(self.lb) < 0:
		#	if float(self.spread) >= float(self.lb) and float(self.spread) < 0:
		#		self.awaydec = "avoid"
		#	else:
		#		self.awaydec = "BET"
		#elif float(self.lb) > 0:
		#	if float(self.spread) <= float(self.lb) and float(self.spread) > 0:
		#		self.awaydec = "avoid"
		#	else:
		#		self.awaydec = "BET"

		#if float(self.ub) < 0:
		#	if float(self.spread) >= float(self.lb) and float(self.spread) < 0:
		#		self.homedec = "BET"
		#	else:
		#		self.homedec = "avoid"
		#elif float(self.ub) > 0:
		#	if float(self.spread) <= float(self.lb) and float(self.spread) > 0:
		#		self.homedec = "BET"
		#	else:
		#		self.homedec = "avoid"
		

	def __init__(self, id, away, home, lb, ub, spread, awaydecR, homedecR):
		self.id = id
		self.away = away
		self.home = home
		self.lb = lb
		self.ub = ub
		self.spread = spread
		self.awaydecR = awaydecR
		self.homedecR = homedecR
		self.awaydec = ""
		self.homedec = ""

def main():
	running = True

	while running:
		keepRunning = ""

		files = os.listdir()
		tsv = []

		for i in files:
			s = i.split(sep='.')
			#for z in s:
			#	print("%s. %s" %(s.index(z), z))
			#print(s[len(s) - 1])
			if s[len(s) - 1] == 'tsv':
				tsv.append(i)			

		try: 
			infile = "-1"
			while int(infile) < 0 or int(infile) > len(tsv) - 1:
				print("Select an file from list below to import spreadsheet:")
				for i in tsv:
					print("%s. %s" % (tsv.index(i), str(i)))

		
				infile = input("Item Number: ")
		except ValueError:
			print("Please select item number from list above.\n")
			infile = "-1"

		outfile = input("Insert output file name: ")

		games = []

		try:
			f = open(tsv[int(infile)], 'r')

			header = f.readline()

			for line in f:
				sect = line.split(sep='\t')

				try:
					if int(sect[0]) >= 0:

						id=sect[0]
						away=sect[1]
						home=sect[2]
						lb=sect[3]
						ub=sect[4]
						spread=sect[5]
						awaydecR=sect[6]
						homedecR=sect[7]

						game = Game(id, away, home, lb, ub, spread, awaydecR, homedecR)
						game.decision()
						games.append(game)
				except ValueError:
					val=""

			f.close()

			f = open(outfile, 'w')
			print("")

			original_stdout = sys.stdout
			sys.stdout=f
			print(header[0:len(header)-1])
			sys.stdout=original_stdout

			for game in games:
				original_stdout = sys.stdout
				sys.stdout=f
				print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (game.id, game.away, game.home, game.lb, game.ub, game.spread, game.awaydec, game.homedec))  
				sys.stdout=original_stdout
				if game.awaydec != game.awaydecR or game.homedec != game.homedecR:
					print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (game.id, game.away, game.home, game.lb, game.ub, game.spread, game.awaydec, game.homedec))
					print("awaydec: %s\tshould be: %s" % (game.awaydec, game.awaydecR))
					print("homedec: %s\tshould be: %s\n" % (game.homedec, game.homedecR))

			sys.stdout=f
			print("\n")
			sys.stdout=original_stdout
			f.close()
		
		except FileNotFoundError:
			print("Error finding specified file. Please try again.")
			keepRunning = 'y'

		while keepRunning != 'y' and keepRunning != 'n':
			try:
				keepRunning = input("Do you want to import file again? y/n: ").lower()
			except ValueError:
				print("Please enter y or n.")

		if keepRunning == 'y':
			running = True
		elif keepRunning == 'n':
			running = False
		
		keepRunning = ""
main()