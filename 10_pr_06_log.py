with open('log.txt') as f:
    a = f.read()
if 'python' in a.lower():  # .lower make all file string in lower case so if we have uppercase 'python' written in log file is also detect by this lower() function.
    print("log file contains python")
else:
    print("log file doesn't contains python")