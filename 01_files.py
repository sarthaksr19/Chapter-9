#use open function to read the content of a file.

# f = open('sample.txt','r')
f = open('sample.txt')  #by default if we don't pass operation argument then it by default takes read(r) operation.
# text = f.read()  function is used to read all character
text = f.read(5) #reads only 5 character.
print(text)
f.close()