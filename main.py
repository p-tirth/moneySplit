from guyClass import *



allowExit = False





while True :
    x=int(input('''SELECT OPTIONS :
    1:ADD MORE PPL
    2:FIND AVG money TO BE PAIED BY 1 PERSON 
    3:SPEND SOMEONES money
    4:SHOW money SPENT BY EVERYONE
    5:SETTLE ALL money DEBTS
    6:quit
        : '''))

    if x==1:
        addPll()
    elif x==2:
        calAvg()
    elif x==3:
        spendmoney()
    elif x==4:
        showmoneySpent()
    elif x==5:
        sortmoney()
        allowExit=True
    elif x==6 :
        if allowExit :
            print('thank you for running the program ...   :)')
            break
        else :
            print('run the fifth option to see the main output of the program , then you can quit , thank you \n ')


        

