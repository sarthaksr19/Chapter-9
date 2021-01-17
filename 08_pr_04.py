with open ("sample1.txt") as f:
    a = f.read()

a = a.replace("donkey","#####")

with open ("sample1.txt","w") as f: 
    f.write(a)

