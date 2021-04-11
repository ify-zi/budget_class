import datetime

#********************MAIN BUDGET CLASS****************************
class Budget:
     #----------------Constructor------------------------
     def __init__(self, balance):
         self.balance = balance

     #----------------deposit method-------------------------
     def deposit(self, amount):
         self.balance += amount
         print("Deposit Successful\nBalance : ${}".format(self.balance))
         tym=datetime.datetime.now()
         print(tym)
    #------------------withdrawal method-------------------------------
     def withdraw(self, amount):
         self.balance -= amount
         print("Withdrawal Successful\nBalance : ${}".format(self.balance))
         tym=datetime.datetime.now()
         print(tym)
     #----------------------transfer method----------------------------
     def transfer(amount,fro,to,fN,tN):
         fro.withdraw(amount)
         to.deposit(amount)
         print("${} Successfully Transfered from {} to {}".format(amount,fN,tN))
     #------------------------balance checking method---------------------------
     def checkBalance(self, className):
         
         print("{}   :   ${}".format(className,self.balance))
         tym=datetime.datetime.now()
         print(tym)
     #-----------------------total balance check---------------
     def totalBalance(T):
               for key in T:
                    print(key, ': $',T[key])
               tym=datetime.datetime.now()
               print(tym)
     
#-------------------------Budget Class instance-----------------------------
food = Budget(10000)
clothing = Budget(15000)
health = Budget(20000)
flex = Budget(5000)
investment = Budget(20000)
#--------------------------depositOption function--------------------------------
def depositOpt(cart):
     if cart == '1':
             amount=int(input("Enter amount:$"))
             food.deposit(amount)
             start()
     elif cart == '2':
             amount=int(input("Enter amount:$"))
             clothing.deposit(amount)
             start()
     elif cart == '3':
             amount=int(input("Enter amount:$"))
             health.deposit(amount)
             start()
     elif cart == '4':
             amount=int(input("Enter amount:$"))
             flex.deposit(amount)
             start()
     elif cart == '5':
             amount=int(input("Enter amount:$"))
             investment.deposit(amount)
             start()
     else:
             print("Wrong input please try again")
             start()
#---------------------------withdrawOption function------------------------------
def withdrawOpt(cart):
     if cart == '1':
             amount=int(input("Enter amount:$"))
             food.withdraw(amount)
             start()
     elif cart == '2':
             amount=int(input("Enter amount:$"))
             clothing.withdraw(amount)
             start()
     elif cart == '3':
             amount=int(input("Enter amount:$"))
             health.withdraw(amount)
             start()
     elif cart == '4':
             amount=int(input("Enter amount:$"))
             flex.withdraw(amount)
             start()
     elif cart == '5':
             amount=int(input("Enter amount:$"))
             investment.withdraw(amount)
             start()
     else:
             print("Wrong input please try again")
             start()
#--------------------------transferOption function------------------------------------
def transferOpt():
     bCategory=input("Select account to REMOVE from:\n1. food\n2. clothing\n3. health\n4. flex\n5. investment\n=>")
     if bCategory == '1':
                    fro = food
                    fN = 'food'
     elif bCategory == '2':
              fro = clothing
              fN = 'clothing'
     elif bCategory == '3':
              fro = health
              fN = 'health'
     elif bCategory == '4':
              fro = flex
              fN = 'flex'
     elif bCategory == '5':
              fro = investment
              fN = 'investment'
     else:
              print("wrong input try again")
              start()
        
     fCategory=input("Select account to Tranfer to:\n1. food\n2. clothing\n3. health\n4. flex\n5. investment\n=>")
     if fCategory == '1':
                    to = food
                    tN = "food"
     elif fCategory == '2':
              to = clothing
              tN = "clothing"
     elif fCategory == '3':
              to = health
              tN = "health"
     elif fCategory == '4':
              to = flex
              tN = "flex"
     elif fCategory == '5':
              to = investment
              tN = "investment"
     else:
              print("wrong input try again")
              start()
     amount=int(input("Enter Amount:$"))
     Budget.transfer(amount,fro,to,fN,tN)
     start()
#------------------------Check balance option method------------------------     
def cbOpt(cart):
     if cart == '1':
             food.checkBalance("Food")
             start()
     elif cart == '2':
             clothing.checkBalance("Clothing")
             start()
     elif cart == '3':
             health.checkBalance('Health')
             start()
     elif cart == '4':
             flex.checkBalance('Flex')
             start()
     elif cart == '5':
             investment.checkBalance('Investment')
             start()
     else:
             print("Wrong input please try again")
             start()
#------------------------Category selection process function------------------------------------
def catOpt(ops):
     print("From which category do you want to {}".format(ops))
     cart=input("1. FOOD\n2. Clothing\n3. Health\n4. Flex\n5. investment\n=>")
     if ops == 'Deposit':
         depositOpt(cart)
     elif ops == 'Withdraw':
         withdrawOpt(cart)
         
     elif ops == 'Check Balance':
           cbOpt(cart)
     else:
         print("wrong input Try again")
         start()
         

#--------------------------main start function of the program-----------------------------
def start():
     print("****************************************************")
     print("*******BETA ASUSU*******\n we help you plan for the future")
     
     opt=input("Select an option\n1. Deposit\n2. Withdrawal\n3. Tranfer\n4. Check Balance\n0. End program\n=>")
     if opt == '1':
         catOpt('Deposit')
     elif opt == '2':
         catOpt('Withdraw')
     elif opt == '3':
         transferOpt()     
     elif opt == '4':
          total=input("Choose one:\n1. General Account Balance \n2. Individual Account Balance\n=>")
          if total == '1':
               T={"food" : food.balance, "clothing" : clothing.balance, "health" : health.balance, "flex" : flex.balance, "investment" : investment.balance}
               Budget.totalBalance(T)
               start()
          elif total == '2':
               catOpt('Check Balance')
     elif opt == '0':
          exit()
     else:
         print("Wrong input try again")
         start()
    
#program started
start()

     

