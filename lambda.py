my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x== "Python",languages)

squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >=30 and x <=70 ,squares)

threes_and_fives = filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 16))
print threes_and_fives


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x!="X", garbled)
print message
