# Selecting a Grid position
l = []
for x in range(1,10):
        l += [x]

p1_select = []
p2_select = []
#Input from Player1
def player1():

    p1 = input("Player1 - select a no. between: %r" %(l))
    global p1_select
    if int(p1) == 0 or int(p1) < 10:
        print ("Player 1 entered: %r" %(p1))
        p1_select += [int(p1)]
        l.remove(int(p1))
    else:
        print ("Enter a no. between 0-9")
    print ("Player one Selections : %r" %(p1_select))
    if len(p1_select) > 2:
        return check_winning()
#Input from Player2
def player2():

    p2 = input("Player2 - select a no. between: %r" %(l))
    global p2_select
    if int(p2) != 0 or int(p2) < 10:
        print ("Player 2 entered: %r" %(p2))
        p2_select += [int(p2)]
        l.remove(int(p2))
    else:
        print ("Enter a no. below 9")
    print ("Player Two Selections : %r" %(p2_select))
    if len(p2_select) > 2:
        return check_winning()

# Checking who is winning win for Player1
def check_winning():
    winning_combo = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    if p1_select in winning_combo:
        print("Player1 Won!!!")
        return 1
    elif p2_select in winning_combo:
        print("Player2 Won!!!!")
        return 1
    else:
        return 0
#
for count in range(1,11):
    if player1() == 1:
        break
    elif  player2() == 1:
        break
    else:
        continue
