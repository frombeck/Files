def word_wrap():
	text= "Wombats are short-legged, muscular quadrupedal marsupials that are native to Australia and are approximately 1 metre (40 in) in length, with small, stubby tails. All are members of the family Vombatidae. They are adaptable in habitat tolerance, and are found in forested, mountainous, and heathland areas of south-eastern Australia, including Tasmania, as well as an isolated patch of about 300 hectares (740 acres) in Epping Forest National Park[2] in central Queensland. "
	#new = filter(lambda x: x==x.split(' ',8)  ,text)
	#a = len(text[::80])
	new = filter(lambda x: x.split("x[:80]")  ,text)
	print new ,
print word_wrap()
