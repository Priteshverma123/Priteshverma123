print("WELCOME TO THE GAME!")
print("this game is all about computer quiz")
playing = input("do u wanna play? ")
print(playing)
if playing.lower() =="yes":
    print("lets start the game")
    score = 0
else:
    print("thank you for visiting to our game")
    quit()
answer1 = input("what does RAM stands for?  ")
if answer1.lower() == "random access memory":
    print("your ans is correct :)")
    score += 1
else:
    print("incorrect answer")
    print("correct answer is random access memory")
answer1 = input("what does CPU stands for?  ")
if answer1.lower() == "central processing unit":
    print("your ans is correct :)")
    score += 1
else:
    print("incorrect answer")
    print("correct answer is central processing unit")
answer1 = input("what does  GPU stands for?  ")
if answer1.lower() == " graphical processing unit":
    print("your ans is correct :)")
    score += 1
else:
    print("incorrect answer")
    print("correct answer is  graphical processing unit")
answer1 = input("what does ROM stands for?  ")
if answer1.lower() == "read only memory":
    print("your ans is correct :)")
    score += 1
else:
    print("incorrect answer")
    print("correct answer is read only memory")
print("you got " + str(score) + "question correct")
print("you got " , str((score/4)*100) , "%")
print("THANK YOU FOR PLAYING OUR QUIZ GAME :)")