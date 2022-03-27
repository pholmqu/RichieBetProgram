import sys
import os
from headers import *

def main():
	selection = "-1"
	options = ['Enter Games', 'Import Spreadsheets', 'Exit']

	while int(selection) != 2:

		print("Welcome to Bet!")

		while (int(selection) < 0) or (int(selection) > len(options)):
			try:
				menu("Menu", options)
				selection = input("Please select an option (#) from above: ")

				if int(selection) == 0:
					selection = "-1"
					games, header = enter_games()
					outfile = input("Insert output file name: ")
					if games != None:
						print_entered_spreadsheet(games, header)
						print_spreadsheet_tsv(games, header)
				elif int(selection) == 1:
					selection = "-1"
					games, header, formatted = import_spreadsheet()
					outfile = input("Insert output file name: ")
					if games != None:
						if formatted == True:
							print_entered_spreadsheet(games, header, outfile)
							print_spreadsheet_tsv(games,header, outfile)
						elif formatted == False:
							print_spreadsheet_tsv(games,header, outfile)

				elif int(selection) == 2:
					exit()

			except ValueError as e:
				print(e)


main()