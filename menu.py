def menu(header, items):
	items = addIndexes(items)
	max = getSize(header, items)
	strMenu = "\n+{}+\n".format('-' * (max + 2))
	strMenu += "|{header: ^{max}}|\n".format(header=header, max=max + 2)
	strMenu += "+{}+\n".format('-' * (max + 2))
	for item in items:
		strMenu += "| {item: <{space}}|\n".format(item=item, space=(max + 1))
	strMenu += "+{}+\n".format('-' * (max + 2))

	print(strMenu)

def getSize(header, items):
	if header == "ID":
		max = len(str(header))
		for item in items:
			if len(str(item.id)) > max:
				max = len(str(item.id))
	elif header == "Road":
		max = len(str(header))
		for item in items:
			if len(str(item.away)) > max:
				max = len(str(item.away))
	elif header == "Home":
		max = len(str(header))
		for item in items:
			if len(str(item.home)) > max:
				max = len(str(item.home))
	elif header == "LB":
		max = len(str(header))
		for item in items:
			if len(str(item.lb)) > max:
				max = len(str(item.lb))
	elif header == "UB":
		max = len(str(header))
		for item in items:
			if len(str(item.ub)) > max:
				max = len(str(item.ub))
	elif header == "Spread":
		max = len(str(header))
		for item in items:
			if len(str(item.ub)) > max:
				max = len(str(item.ub))
	elif header == "Road Decision":
		max = len(str(header))
		for item in items:
			if len(str(item.awaydec)) > max:
				max = len(str(item.awaydec))
	elif header == "Home Decision":
		max = len(str(header))
		for item in items:
			if len(str(item.homedec)) > max:
				max = len(str(item.homedec))
	else:
		max = len(header)
		for item in items:
			if len(str(item)) > max:
				max = len(str(item))

	return max

def addIndexes(items):
	newItems = []

	for item in items:
		temp = str(items.index(item)) + ". " + item
		newItems.append(temp)

	return newItems