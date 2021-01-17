f = open('sample.txt')
text = f.readline() #this readline() uses for reading the one line.
print(text)
text = f.readline() #this readline() uses for reading the next one line....and so on.
print(text)
f.close()