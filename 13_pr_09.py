file1 = "this.txt"
file2 = "copy.txt"

with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("files are identical and matches the content of another file")
else:
    print("files are not identical and doesn't matches the content of another file")
    