import ListSplit
import Date_Time
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow :- "+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The name of the lender is incorrect")
        returnBook()

    b="Return :- "+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + Date_Time.getDate()+"    Time:"+ Date_Time.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(3):
        if ListSplit.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t$"+ListSplit.cost[i]+"\n")
                ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            total+=float(ListSplit.cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the date of book returned expired? ")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days the book was returned late? ")
        day=int(input())
        fine=2*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("All Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
