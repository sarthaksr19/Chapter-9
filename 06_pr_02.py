def game():  # game() fuction returning games score as a int.
    return 555 

score = game()       # storing return value of a game() functioninto a score variable
with open('hi-score.txt',) as f:  #  open hi-score.txt as a read mode
    HighScore = int(f.read())   # store .txt value as a int in a variable name via read function HighScore 
if score > HighScore:           # check whether this game() score variable is greater than previous stored highscore in .txt file
    with open('hi-score.txt','w') as f:  #if its true then open .txt file as a write mode 
        f.write(str(score))             # and write score variable value with str() as write() takes argument as a string not an integer
# else:
#     f.write(HighScore)

