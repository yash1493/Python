def summer_69(args):
	add=0
	flag=True
	for i in args:
		while flag:
			if i!=6:
				add+=i
				break
			else:
				flag=False
				break
		while not flag:
			if i!=9:
				break
			flag=True
	return add
