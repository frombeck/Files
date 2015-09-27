#Created by Bek Nurmatov
def calc():
	total = 0
	while True:
		try:
			total =float(input("Please enter your calculations and press Enter:"))
			print "Your total is =", total
		except ValueError:
            		print "wrong argument"
			break

calc()
