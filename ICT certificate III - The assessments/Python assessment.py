import string
def encrypt(Password):

    charSet= string.punctuaion + string.digits + string.ascii_letters
    encText = "".join([charSet[(charSet.find(c)+3)%95] for c in Password])
    return encText

def decrypt(data):
    global charSet

    string= charSet
    encText = "".join([string[(string.find(c)-3)%95] for c in data])
    return encText
       
#========================================================
#Welcome in the program

print("="*23)
print("Welcome in Digicore")
print("="*23)

choice = ''
#=========================================================
#here is the menu
while choice != '3':
    print("_"*50)
    print("\n[1] Enter 1 To Create an Account")
    print("[2] Enter 2 To see Your Enformation")
    print("[3] Enter 3 quit Form the program")
    print("_"*50)

    choice = input("\n Make Your Choice ---> : ")

#==========================================================
#here is choice (1) for create a Encryption key

    if choice == '1':
        print("Please Answer the questions in the below")
        print("-"*50)
        Username = input("Enter Your Username Please: ")
        Email = input("Enter Your Email Please: ")
        Password = input("Enter Your Password Please: ")
        userdata = (Username, Email, Password)
        encrypted_Password =  encrypt(Password)
        f = open("userinfo.txt", "a")
        f.write(Username + "|"  + Email + "|"  + encrypted_Password + "\n")
        f.close()
    
        
#=============================================================
#here is Choice (2) for Decrypted key

    elif choice == '2':
        
        try:
            with open("userinfo.txt", "r") as file:
                print("\n--- Saved Credentials---")
                print(f"{'Username':20}{'Email':<30}{'Password'}")
                print("="*60)
                for line in file:
                    Username, Email, encrypted_Password = line.strip().split('|')
                    decrypted_Password = decrypt(encrypted_Password)
                    print(f"{Username:<20}{Email:<30}{decrypted_Password}")
        except FileNotFoundError:
            print("File not Found")


#===============================================================
#here is choice (3) To exist form the program

    elif choice == '3':
        import time
        print("exiting the program")
        time.sleep(1)
        print("thank you to use Digicore")
