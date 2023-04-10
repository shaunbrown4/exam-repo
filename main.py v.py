user_one ={
    'full name' : 'Ali Brown',
      'username' : 'alib',
           'password': 'lovelove',
           'account balance': 35000,
           'Connected accounts':[("Bank Of America",50000),("Navey Federal",100000)]}
user_two ={'full name': 'Anora Brown',
           'username': 'ab123',
           'password': 'baby1',
           'Citadel balance':350,
           'Connected accounts':[("Bank of America",500),("Navey Federal",3000)]}

realusername = "alib"
realpassword = "lovelove"
username =""
password = ""
while username != realusername or password != realpassword:
    username = input("Please enter username ")   
    password = input("enter your password ")

    if username != realusername: 
        print("incorrect user name")
    if password != realpassword:
        print("incorrect password")

print("Welcome Back Ali! ")
print("")
print(user_one["account balance"])
print("")
print(user_one["Connected accounts"])
print("")
print("Start user transaction.. ")
print("")
rec = input("Would you like to make a transfer to Anora Brown?(Y/N)  ")
rec = rec.upper()
N = "N"
Y = "Y"
if rec == N :
        print("No further transactions have a nice day.")
if rec == Y :
    input("How much would you lime to transfer?($1 increments)  ")
print(user_one["account balance"]-(""))





