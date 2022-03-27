class Game:


	def decision(self):
		if float(self.lb) < 0:
			if float(self.spread) > 0 or float(self.spread) < float(self.lb):
				self.awaydec = "BET"
			else:
				self.awaydec = "avoid"
		else:
			if float(self.spread) < 0 or float(self.spread) > float(self.lb):
				self.awaydec = "BET"
			else:
				self.awaydec = "avoid"
		
		if float(self.spread) < float(self.ub):
			self.homedec = "avoid"
		else:
			self.homedec = "BET"
	
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
		#if float(self.lb) < 0:
		#	if float(self.spread) <= float(self.lb):
		#		self.awaydec = "BET"
		#	else:
		#		self.awaydec = "avoid"
		#elif float(self.lb) > 0:
		#	if float(self.spread) >= float(self.lb):
		#		self.awaydec = "BET"
		#	else:
		#		self.awaydec = "avoid"
		#else:
		#	self.awaydec = "avoid"

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