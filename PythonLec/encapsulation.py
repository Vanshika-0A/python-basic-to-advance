class bankaccount:
    def __init__(self,name,balance):
        self.name=name #public
        #for protected use _ and for private use __ but protected is just conventional not enforced 
        self.__balance= balance #private
        #to access priavte use getters and setters
    def get_balance(self):
        return self.__balance
       
# for without getters or setters use method in line 15

acc1 = bankaccount("vanshi","40000")

print(acc1.name , acc1.get_balance())
print(acc1._bankaccount__balance) # we can call private attribute like this