from pync import Notifier
import random

class UserInfo:
    def __init__(self, fname, lname, password) -> None:
        self.fullName = f'{fname} {lname}'
        self.__password = password
        self.__username = f'{fname.lower()}{lname.lower()}'
        self.__email = f'{self.__username}@totocompany.com'
        print("Profile created successully! Now complete your profile!")
        self.__completeInfo()

    def __twoFacAuth(self):
        self.__otp = random.randint(100000, 999999)
        try:
            Notifier.notify(
                title = "OTP",
                message = f"Your OTP is : {self.__otp}. Don't share it anything else.",
                timeout = 10
            )
        except Exception as e:
            print(f"Error displaying notification: {e}")
    
    def __verify(self):
        print("Verify first!")
        usernameEmail = input("Enter your email or username : ")
        password = input("Enter your password : ")
        if (usernameEmail == self.__username or usernameEmail == self.__email) and password == self.__password:
            self.__twoFacAuth()
            otp = int(input("OTP sent successfully! Enter your OTP : "))
            if otp == self.__otp:
                print("OTP matches successfully!")
                return True
            else:
                print("Wrong OTP!")
                return False
        else:
            print("Invalid Credential!")
            self.__verify()
            

    def __completeInfo(self):
            phone = input("Enter your phone number : ")
            address = input("Enter your address : ")
            dob = input("Enter your DOB : ")
            self.__phone = phone
            self.address = address
            self.__dob = dob
            print("Database saved successfully! Profile Completed!")

    def getInfo(self):
        if self.__verify():
            dic = {'Name' : self.fullName, 'Email' : self.__email, 'Address' : self.address, 'DOB' : self.__dob, 'Phone' : self.__phone}
            print(dic)
        else:
            self.getInfo()

fname = input("Enter your first name : ")
lname = input("Enter your last name : ")
password = input("Enter your password : ")

user = UserInfo(fname, lname, password)
user.getInfo()