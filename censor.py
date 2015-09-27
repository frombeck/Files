def censor(text, word):
    wordlen = len(word)
    astrix = "*" * wordlen
    mylist = text.split()
    for i in (i for i,x in enumerate(mylist) if x == word):
        mylist[i] = astrix
        finalresult = " ".join(mylist)
    return finalresult

censor("this hack is wack hack", "hack") 
