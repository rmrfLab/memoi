# memoi by rmrfLab
import random

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

cardL = []
version = "0.02a"
goalAcc = 1
exitCode = 0
helpInfo = """
'add cards' or 'adc'            Adding cards.
'set gol accuracy' or 'sga'     Set a goal accuracy, which should be input in decimal
'clear cards' or 'clc'          Delete all cards you've made
'check cards' or 'ckc'          Show all the cards you've made
'start memorizing' or 'smr'     Show cards in shuffle. We will first show a card's front
                                and then waiting for a Enter before showing its back, t-
                                hen, you can press Enter or whatever if your answer is
                                right, or simply input a no.
                                The shuffle will do again if your acuuracy is less than
                                that you set as goal. The default goal accuracy is 1.
'help'                          Show this help page.
'quit'                          Quit the program.
"""

def main():
    print("memoi version "+version+" by rmrf lab!")
    while True:
        cmd = input("[ Waiting for commands... input help for more info. ]\n[CMD]\t\t")
        execCmd(cmd)
        if exitCode: return 0
def execCmd(cmd):
    if cmd=="help":
        print(helpInfo)
    elif cmd=="add cards" or cmd=="adc":
        addCards()
    elif cmd=="set goal accuracy" or cmd=="sga":
        setGoalAcc()
    elif cmd=="clear cards" or cmd=="clc":
        cardL = []
    elif cmd=="check cards" or cmd=="ckc":
        checkCards()
    elif cmd=="start memorizing" or cmd=="smr":
        memo()
    elif cmd=="quit":
        global exitCode
        exitCode = 1
    else: print("Invalid command. Please check your input.")
def addCards():
    print("Cards adding mode. Input a card whose front is '/:quit' to stop")
    front = ''
    while True:
        l = str(len(cardL)+1)
        front = input("[FRONT "+l+"]\t\t")
        if front=='/:quit': break
        back = input("[BACK "+l+"]\t\t")
        cardL.append(Card(front, back))
def setGoalAcc():
    global goalAcc
    print("[ Your current goal accuracy is "+str(goalAcc)+", please input your new goal in float type: ]")
    t = input("[ACC]\t\t")
    try:
        p = float(t)
        if not 1>=p>=0:
            print("[ Goal accuracy should be in [0,1]! ]")
            setGoalAcc()
        else:
            goalAcc = p
    except ValueError:
        print("[ Invalid goal accuracy! ]")
        setGoalAcc()
def checkCards():
    if len(cardL)==0: 
        print("No cards added now!")
        return
    print("Here are all the cards:\nFront\t\tBack\t\tNumber")
    for i in range(0, len(cardL)):
        print(cardL[i].front+"\t\t"+cardL[i].back+"\t\t"+str(i+1))
def memo():
    n = len(cardL)
    if n==0: print("[ You haven't made any cards yet! ]"); return
    wrong = n
    trueAcc = -1
    tempL = cardL
    random.shuffle(tempL)
    while trueAcc<goalAcc:
        for i in range(0, n):
            print("[FRONT "+str(i)+": "+tempL[i].front+" ]", end='')
            input()
            print("[BACK "+str(i)+": "+tempL[i].back+" ]")
            ans = input("[CORRECT?]\t\t")
            if ans!="no": wrong -= 1
        trueAcc = (n-wrong)/n
        if trueAcc<goalAcc:
            print("[ Your accuracy in this round("+str(trueAcc)+") is less than your goal("+str(goalAcc)+"), try again! ]")
    print("[ Congrats! Your accuracy in this round is "+str(trueAcc)+". ]")

main()
