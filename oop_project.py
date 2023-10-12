from bank_account import *

Dave = BankAccount(1000,"Dave")
Sara = BankAccount(2000,"Sara")

Dave.getBalance()
Sara.deposit(500)

Dave.withdraw(5000)
Dave.withdraw(500)

Sara.transfer(1000,Dave)

Jim = InterestRewardsAcct(1000,'Jim')

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Sara)

Blaze = SavingsAcct(1000,"Blaze")

Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000,Sara)