# instance variable : Name, Amount, Address, AccountNo
# Instance Method : CreateAccount(), DisplayAccountInfo
# class variable : Bank_name , ROI_On_FD
# class method : DisplayBankInformation
# Static method : DisplayKYCInfo

class Bank_Account:

    Bank_Name = "HDFC Bank Pvt LTD"
    ROI_on_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter Your Name :")
        self.Name = input()

        print("Enter Your Initial Amount :")
        self.Amount = int(input())

        print("Enter Your Address :")
        self.Address = input()

        print("Enter Your Account Number :")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("------------Your Account Information is as follow-------------")
        print("Name of Account Holder :", self.Name)
        print("Account Number :", self.AccountNo)
        print("Address of Account Holder :", self.Address)
        print("Current Amount in Account :", self.Amount)
        print()

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome To Banking Console")
        print("Name Of Bank :", cls.Bank_Name)
        print("Rate of Interest on fixed deposite :", cls.ROI_on_FD)
        
    @staticmethod
    def DisplayKYCInfo():
        print("please consider below kyc information")
        print("Submit Below Document")
        print("1 : Clear Passport size photo")
        print("2 : Photo of Adhar Card")
        print("3 : Photo of Pan Card")

    def Deposite(self,Value):
        self.Amount = self.Amount + Value
       
    def Withdraw(self,Value):
        self.Amount = self.Amount - Value 

def main():
    Bank_Account.DisplayKYCInfo()
    
    print("name of bank :", Bank_Account.Bank_Name)
    print("Rate of Interest on FD :", Bank_Account.ROI_on_FD)

    Bank_Account.DisplayBankInformation()

    user1 = Bank_Account()
    user2 = Bank_Account()

    user1.CreateAccount()
    user2.CreateAccount()

    user1.DisplayAccountInfo()
    user2.DisplayAccountInfo()
    
    user1.Deposite(500)
    user1.Deposite(1200)
    
    print("Amount of {} after deposite is {}:".format(user1.Name,user1.Amount))
    print("Amount of {} after deposite is {}:".format(user2.Name,user2.Amount))

    
    user1.Withdraw(200)
    user2.Withdraw(3000)
    print("Amount of {} after withdraw is {}:".format(user1.Name,user1.Amount))
    print("Amount of {} after withdraw is {}:".format(user2.Name,user2.Amount))


if __name__ == "__main__":
    main()
