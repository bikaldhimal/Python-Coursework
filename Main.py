import Return
import ListSplit
import Date_Time
import Borrow

def start():
    while(True):
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||| Welcome To The Library Management System ||||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("Enter 1 : To Display")
        print("Enter 2 : To Lend a book")
        print("Enter 3 : To return a book")
        print("Enter 4 : To Quit")
        try:
            a=int(input("Select an option from 1-4: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Hope you had a great experience, Thank you")
                break
            else:
                print("Please enter a valid options from 1-4")
        except ValueError:
            print("Please enter as suggested")
start()
