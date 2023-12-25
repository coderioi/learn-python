print(2==2) #this is also true
print ("s" == "s")  # this is true
print( "s" == "s ") # this is false because of the space
print("s" == "p") # false


print("This is scissors paper and rock game")
print("Player 1 please choose either (s/p/r)")
player1 = input()

# we are validating if player 1 choose (s/p/r)

if player1 == "s" or player1 == "p" or player1 == "r":
  print("validation successful")
else: 
  print("not allowed, please choose (s/p/r) only")
  exit()
  
print("Player 2 please choose either (s/p/r)")
player2 = input()
if player2 == "s" or player2 == "p" or player2 == "r":
  print("validation successful")
else: 
  print("not allowed, please choose (s/p/r) only")
  exit()

print("player 1 chose: " + player1)
print("player 2 chose: " + player2)

'''
this is checking if player1 string and player2 string is same or not 
'''
if player1 == player2:
  print("Draw")
  print("both player chose same thing")


if player1 == "s" and player2 == "p":
  print("player 1 wins")

if player1 == "s" and player2 == "r":
  print("player 2 wins")

if player1 == "p" and player2 == "s":
  print("player 2 wins")

if player1 == "p" and player2 == "r":
  print("player1 wins")

if player1=="r" and player2 =="p":
  print("player 2 wins")

if player1 =="r" and player2 == "s":
  print("player 1 wins")
  
