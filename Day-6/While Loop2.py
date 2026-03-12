# WAP to print How many bullets are left after every iteration using while loop and  while-else 
bullets=10
while bullets>0:
    print(f"Bullets left: {bullets}")
    bullets-=1
else:
    print("No bullets left")
    
# WAP to print the logic of candy crusher game using while loop and while-else
moves=32
winning_point=8
while moves>0:
    if moves == winning_point:
        print("You win the game")
        break
    else:
        print(f"Moves left: {moves} to play the game!")
        moves-=1
else:
    print("Game Over")
    
    
