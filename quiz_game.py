from lib2to3.pgen2.token import GREATER


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ") 

if playing.lower() != "yes":
    quit()
    
player_name = input("Enter your name ")

print("okay! let's play :)")
score = 0
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")


answer = input("What does RAM stanf for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + "question correct!")
print("You got " + str((score / 4) * 100) + "%") 
print("show it's going to the old remote")
print("Hello, Adeyemi!")
print("hello james")