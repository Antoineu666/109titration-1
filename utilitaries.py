from point import Point

def create_list_point(path):
	try:
		list = [0] * (len(open(path, "r").readlines()))
	except:
		print("Bad file")
		sys.exit(84)
	i = 0
	for s in open(path, "r").readlines():
		try:
			s = s.split(';')
			assert(len(s) == 2)
			float(s[0])
			float(s[1])
		except:
			print("Bad point")
			sys.exit(84)
		list[i] = Point(s[0], s[1])
		i = i + 1
	list = sorted(list, key=lambda Point: Point.x)
	return (list)

def calcul(list, i):
	try:
		res = (list[i + 1].y - list[i - 1].y) / (list[i + 1].x - list[i - 1].x)
	except:
		print("division by zero")
		sys.exit(84)
	return (res)

def derivative(list):
	i = 1
	new_list = [0] * (len(list) - 2)
	while i != len(list) - 1:
		try:
			assert(list[i].x == int(list[i].x))
			print("volume:	%i ml" % int(list[i].x), "-> %.2f" % calcul(list, i))
		except:
			print("volume:	%.1f ml" % list[i].x, "-> %.2f" % calcul(list, i))
		new_list[i - 1] = Point(list[i].x, calcul(list, i))
		i = i + 1
	return (new_list)

def find_equivalent_point(list):
	mem = 0
	i = 0
	while i != len(list):
		if abs(list[i].y) > abs(list[mem].y):
			mem = i
		i = i + 1
	return (mem)
