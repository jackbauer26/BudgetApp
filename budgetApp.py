class Budget:

    # creating class variables named WelcomeMessage

    print('\n')
    WelcomeMessage = ' Welcome To Your Budget App '
    WelcomeMessage = WelcomeMessage.center(50,'*')
    
    # instance variables creation with default current balance set to 0
    def __init__(self,category):
        self.category = category
        self.currentBalance = 0
        self.demarcation = '*'*65

    def __str__(self):
        return 'Welcome to your {} category'.format(self.category)

    def deposit(self,amtToDeposit):
        # the deposit method accepts the amount user intends to deposit as parameter
        try:
            if amtToDeposit <= 0:
                print(self.demarcation)
                return '\nYou have entered an invalid input.'
            else:
                self.currentBalance += amtToDeposit
                print(self.demarcation)
                print('You have deposited #{:,.2f} into your {} category'.format(amtToDeposit,self.category))
                return 'Your {} category balance is now #{:,.2f}'.format(self.category,self.currentBalance)
        except:
            return ('Wrong User Input')

    def withdraw(self,amtToWithdraw):
        # the withdraw method accepts a parameter to process how much to withdraw

        if amtToWithdraw <= self.currentBalance:

            self.currentBalance -= amtToWithdraw
            message = 'You have withdrawn #{:,.2f} from your {} category'.format(amtToWithdraw,self.category)
            print(self.demarcation)
            print(message)
            return self.categoryBalance()

        else:
            return 'Insufficient Balance'

    def transfer(self,amtToTransfer):

        # the transfer method accepts a parameter that is the precise amount to transfer
        message = 'You have just transfered #{:,.2f} from your {} category'.format(amtToTransfer,self.category)
        print(self.demarcation)
        print(message)
        return amtToTransfer

    def categoryBalance(self):

        # this method returns a remaining balance of the object
        print(self.demarcation) 
        return 'The Current Balance left in the {} Category is #{:,.2f}'.format(self.category,self.currentBalance) 


food = Budget('food')
clothing = Budget('Clothing')

print(food.deposit(13000))
print(clothing.deposit(30000))
print(clothing.withdraw(1000))
print(food.deposit(clothing.transfer(150000)))
print(clothing.categoryBalance())