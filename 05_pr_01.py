with open('poem.txt','r') as f:
    a = f.read()
    if 'Twinkle' in a:
        print("poem contain twinkle keyword")
    else:
        print("poem doesn't contain twinkle keyword")
print(a)