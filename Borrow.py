import Date_Time
import ListSplit

def borrowBook():
    success=False
    while(True):
        firstName=input("Enter the first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input alphabet from Aa-Zz")
    while(True):
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from Aa-Zz")
            
    t="Borrow :- "+firstName+".txt"
    with open(t,"w+") as f:
        f.write("               Library Management System  \n")
        f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
        f.write("    Date: " + Date_Time.getDate()+"    Time:"+ Date_Time.getTime()+"\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while success==False:
        print("Please select an option below: ")
        for i in range(len(ListSplit.bookname)):
            print("Enter", i, "to lend book", ListSplit.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("The book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")


                    # Codes for borrowing multiple books
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to lend more books? However you cannot lend same book twice. Press y for yes and n for no: "))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListSplit.bookname)):
                                print("Enter", i, "to lend book", ListSplit.bookname[i])
                            a=int(input())
                            if(int(ListSplit.quantity[a])>0):
                                print("The book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from our library. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("The book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their assigned number")
        except ValueError:
            print("")
            print("Please choose as suggested")
