#  question 2 
import random

def game():
    print("you are playing the game...")
    score = random.randint(1, 62)
    # fethch the highscore 
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"your score is : {score}")
    if(score > highscore):
        # write this score to the file
        with open("highscore.txt" , "w") as f:
            f.write(str(score))

    return score

game()