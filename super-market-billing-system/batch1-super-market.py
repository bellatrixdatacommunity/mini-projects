print("                                                                   Welcome To The Super Market App")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
store=input("Please Enter Your Store Name\n")
customer=input("Please Enter Your Customers Name:\n")
phone=int(input("Please Enter Customers Phone No:\n"))
dict={"Hp Pavallion":"33000","Dell Inspiron":"45000","Lenovo":"24000","Apple":"60000"}
purchased=[]
bought=[]
quantity=[]
final=[]
import os
os.system("cls")
print("                                                                 Welcome To The Store",store)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
import datetime
current_time = datetime.datetime.now()
print("Customers Name:",customer,"                               Phone No:",phone,"                                     Time:",current_time)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Please Enter The Items Purchased")
while(True):
    items=input()
    num=int(input("Please Enter The Quantity"))
    bum=int(dict[items])*num
    purchased.append(bum)
    bought.append(items)
    quantity.append(num)
    a=items,"                                                           ",num,"                                         ",bum
    final.append(a)

    print(purchased)
    press=int(input("Press 1 To View The Bill\nPress Any Other Key To Continue"))
    if press==1:
        print("                                                                 Welcome To The Store", store)
        print(
            "------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        import datetime

        current_time = datetime.datetime.now()
        print("Customers Name:", customer, "                               Phone No:", phone,
              "                                     Time:", current_time)
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Items","                                                                       Quantity","                                           Value")
        #print(final,"\n")
        print(*final,sep="\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Total:",sum(purchased))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Press 0 For Break")
        pres=int(input())
        if pres==0:
            break
