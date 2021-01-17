# the best thing about this with statement is it doesn't need .close command 

with open('another.txt','r') as f:
    a = f.read()
with open('another.txt','w') as f:
    a = f.write("i am a python programmer")

print(a)
