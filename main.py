from validation import 
from account_logic import 
def main():
  while True:
    print("***Welcome to ABC Bank***")
    login()
    choice=input("Enter the choice (1/2/3):")
    if choice=='1':
        withDraw()
        break
    elif choice=='2':
        Deposit()
        break
    elif choice=='3':
        check_Balance()
        break
    else:
        print("Wrong option selected. Try again")
        
if __name__=='__main__':
   main()