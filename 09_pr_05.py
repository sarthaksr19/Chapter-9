words = ["donkey","kaddu","ghanta","thappad"]
with open ("sample1.txt") as f:
    a = f.read()

for word in words:
    a = a.replace(word,"#####")

with open ("sample1.txt","w") as f: 
    f.write(a)

