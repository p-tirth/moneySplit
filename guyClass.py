global giverList;
giverList = []
global reciverList;
reciverList = []
global listOfGuys;
listOfGuys = []

class guy:
    
    #initiate all lists

    def __init__(self,Name,money=0,append=True):
        self.name=Name 
        if append:
            listOfGuys.append(self)
        self.moneySpent=money

    def spendMoremoney(self,money):
        self.moneySpent =money+self.moneySpent  
    
    # def setAftermoney(self,money) :
    #     self.aftermoney=money

    def analyse (self,avg):  # group guys (according to their pay) to recivers or givers
        self.aftermoney = avg - self.moneySpent # positive = money to give  ; negative = money to recive  
        if self.aftermoney==0:
            self.grpStats='None'

        elif self.aftermoney < 0:
            self.grpStats ='reciver'
            reciverList.append(self)
            self.aftermoney = abs(self.aftermoney)

        elif self.aftermoney >  0 : 
            self.grpStats='giver'
            giverList.append(self)
            self.aftermoney = abs(self.aftermoney)

            

def getListOfGuys():
    return listOfGuys;

def addPll(): # add new ppl into grp 
    next=1
    while next ==1:

        inputName=input('enter new name : ')
        inputmoney=int(input(f'enter money payed by {inputName} : '))
        guy(inputName,inputmoney)
        next=int(input('add more ppl ? [1 - yes , 0 - no] : '))

def calAvg(): # money 1 guy supposed to pay 
    sum=0
    for guyName in listOfGuys:
        sum+=guyName.moneySpent
    moneyPerGuy= sum/len(listOfGuys)
    print(f'the money to be paied by 1 guy is : {round(moneyPerGuy)} bucks')
    return round(moneyPerGuy)

def grpGuys(moneyPerGuy) :
    for i in listOfGuys:
        i.analyse(moneyPerGuy)
    # print(giverList)
    # print(reciverList)

def showmoneySpent():
    for i in getListOfGuys():
        print(f'{getListOfGuys().index(i)} : {i.name} - spent ${i.moneySpent}')

def spendmoney():
    for i in getListOfGuys():
        print(f'{getListOfGuys().index(i)} : {i.name} - spent ${i.moneySpent}')
        # print(f"kok{i.name}")
    personNumber = int(input('ENTER NUMBER TO SPEND HIS/HER money : '))
    cashAmount = int(input('ENTER THE AMOUNT TO SPEND : '))
    getListOfGuys()[personNumber].spendMoremoney(cashAmount)

def sortmoney():
    # sortin = True
    # while sortin :
    grpGuys(calAvg())
    transaction =[]

    while reciverList != [] :
        if reciverList[0].aftermoney == giverList[0].aftermoney :
            transaction.append(f'{giverList[0].name} to {reciverList[0].name} ; {reciverList[0].aftermoney}')
            reciverList[0].aftermoney=0
            giverList[0].aftermoney=0
            

        elif reciverList[0].aftermoney > giverList[0].aftermoney :
            transaction.append(f'{giverList[0].name} to {reciverList[0].name} ; {giverList[0].aftermoney}')
            giverList[0].aftermoney , reciverList[0].aftermoney = 0 , reciverList[0].aftermoney - giverList[0].aftermoney


        elif reciverList[0].aftermoney < giverList[0].aftermoney:
            transaction.append(f'{giverList[0].name} to {reciverList[0].name} ; {reciverList[0].aftermoney}')
            reciverList[0].aftermoney , giverList[0].aftermoney = 0 , giverList[0].aftermoney - reciverList[0].aftermoney
        else:
            pass

        if reciverList[0].aftermoney == 0:
            del reciverList[0]

        if giverList[0].aftermoney == 0:
            del giverList[0]

    for i in transaction :
        print(i)

