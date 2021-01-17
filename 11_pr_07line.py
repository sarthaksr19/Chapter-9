a = True
i = 1
with open('log.txt') as f:
    while a:

        a = f.readline()
        if 'python' in a.lower():  # .lower make all file string in lower case so if we have uppercase 'python' written in log file is also detect by this lower() function.
            print(a)
            print("log file contains python")
            print(i)  #printing the line number where python is present
        
        i += 1
