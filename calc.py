
def calc():

	try:
		total = input("Please enter calculation and press Enter:") 
		return (lambda total: float(total))
	except AttributeError:
	        print("not a valid number")
		return(0)
print ('Your total is =', calc())
