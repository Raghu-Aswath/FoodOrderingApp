

import inventory as inv
import csv
import pandas as pd
import datetime
DATE = datetime.date.today()
d = str(DATE)



def register_new_user():
    print("*" * 50)
    print("Weelcome to Raghu's Food Court")
    print("Kindly Signup by providing details below")
    print("*" * 50)
    nm = input("Full Name :")
    user_name = input('create your user name :')
    df = pd.read_csv('userdata.csv')
    l = list(df['user_name'])
    if user_name in l:
        print("*" * 50)
        print("OOPS!!! user name already exists please Try again")
        register_new_user()
    else:
        password = input('create Password :')
        mob_num = input('Phone Number :')
        Email = input("Enter your Email :")
        address = input("Enter your address :")
        with open('userdata.csv', 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([user_name, nm, mob_num, Email, address, password])
            print("**************--Thank You For Registering with us--**************")
        print("Press 1 to Login to your Account")
        try:
            a = int(input("please Enter 1 to login : "))
            if a == 1:
                login()
        except:
            print("**************--Thank You For Registering with us--**************")


def login():
    global usr_name
    print("*" * 50)
    print("welcome to Raghu's Food court")
    print("Please login with your User Id and Password")
    print("*" * 50)
    usr_name = input("Please Enter your  User Name :")
    df = pd.read_csv('userdata.csv')
    l = list(df['user_name'])
    if usr_name not in l:
        print("you are not registered with us")
        print("Enter 1 to Register with us or 2 to login again")
        a = int(input("enter your choice :"))
        try:
            if a == 1:
                register_new_user()
            if a == 2:
                login()
        except:
            print("*********--Thank You--*********")
            login()
    filter = df['user_name'] == usr_name
    psd = df[filter]['password']
    user_info = df[filter].to_string(index=False)
    name = df[filter]['name']
    name1 = (name.to_string(index=False))
    pas = input("Enter your password :")
    psd1 = (psd.to_string(index=False))
    if pas == psd1:
        print("*" * 50)
        print("login Success!!!")
        print("Welcome", name1)
        user_menu()
    elif pas != psd1:
        print("user name or passoword is  incorrect")
        print("press 1 to sign up or 2 to login again")
        try:
            key1 = int(input("Enter your choice"))
            if key1 == 1:
                register_new_user()
            elif key == 2:
                login()
            else:
                print("*" * 20, "Thank You", "*" * 20)
        except:
            print("*" * 20, "Thank You", "*" * 20)
            return usr_name


def user_menu():
    import admin as ad
    print("*" * 50)
    print(" Enter 1 to place New order", "\n", "Enter 2 view or Edit Profile", "\n", "Enter 3 to order history to ","\n", "Enter 4 to logout")
    print("*" * 50)
    try:
        key = int(input("Please Select your Choice"))
        if key == 1:
            print('*' * 60)
            print("Food Menu")
            book_order()
            print('*' * 50)
            print("Enter 0 (Zer0) for main menu or 5 to logout for main menu")
            print('*' * 60)
            tmp_key = int(input("Enter your choice"))
            try:
                if tmp_key == 0:
                    user_menu()
                elif tmp_key == 5:
                    login()
            except:
                user_menu()
        if key == 2:
            edit_profile()
            print('*' * 50)
            print("Enter 0 (Zer0) for main menu or 5 to logout for main menu")
            print('*' * 50)
            tmp_key = int(input("Enter your choice"))
            try:
                if tmp_key == 0:
                    user_menu()
                elif tmp_key == 5:
                    login()
            except:
                user_menu()
        if key == 3:
            print("Order History")
            order_history()
            print('*' * 50)
            print("Enter 0 (Zer0) for main menu or 5 to logout for main menu")
            print('*' * 50)
            tmp_key = int(input("Enter your choice"))
            try:
                if tmp_key == 0:
                    user_menu()
                elif tmp_key == 5:
                    login()
            except:
                user_menu()
        if key == 4:
            print("Log out Success full!!","\n","*"*20," Thank You ","*"*20)
            login()
    except:
        print("Please Enter Correct Choice")
        user_menu()








def View_profile():
    df = pd.read_csv('userdata.csv')
    fltr = df["user_name"]==usr_name
    a = df[fltr].values
    user_info = list(list(a[0]))
    print('*' * 50)
    print("Name :",user_info[1],"    ","Mobile No. :",user_info[2])
    print()
    print("Email Id:",user_info[3])
    print()
    print("address :",user_info[4])
    print("-"*40)








                
def book_order():
    import inventory as inv
    inv.Show_inventory()
    print("*" * 50)
    print("welcome to Raghu's Food court")
    print("*" * 50)
    df = pd.read_csv('inventory.csv')
    l = list(df['FOOD_ID'])
    n=int(input("Enter how many items do you want to Order"))
    price=0
    finallist=[]
    for i in range(n):
        key = input("Please Enter Food Id which you wish to Order :" )
        if key.upper() not in l:
            print("Food id Not found")
            book_order()
        else:
            quantity = int(input("Please Enter Quantity Required"))
            if quantity <=0:
                print("quantity should be ATLEAST ONE try again")
            else:
                fltr = df["FOOD_ID"]==key.upper()
                order_info = df[fltr].values
                flat_list = [x for xs in order_info for x in order_info]
                l_s_t=[flat_list[0][1],flat_list[0][3],quantity,flat_list[0][2]]
                confirm_order = int(input("Enter 1 to confirm your Order or 2 to cancel"))
                if confirm_order ==2:
                    print("Your order has been cancelled Order Again")
                elif confirm_order==1:
                    price =price + (flat_list[0][3]*quantity)
                    lst=[["item Name :",flat_list[0][1]],["price :",flat_list[0][3]],["Discount :",flat_list[0][4]],["Quantity :",quantity],["item des :",flat_list[0][2]]]
                    finallist.append(lst)
                    file = open('orders.csv', 'a', newline="")
                    writer = csv.writer(file)
                    writer.writerow([usr_name,d,flat_list[0][1],flat_list[0][3],quantity,price,flat_list[0][2]])
                    print("************Order added Successfully**************")
                    file.close()
                    for i in finallist:
                        for j in i:
                            for k in j:
                                print(k, end=" ")
                            print()
                        print("-"*20)
                    print("*"*20)
                    print("Total Cost :", price)
                    print("*"*20)
                else:
                    print("inappropriate option")
                    user_menu()

        
        

def edit_profile():
        View_profile()
        f = open("userdata.csv","r")
        reader=csv.reader(f)
        found=False
        temp_data=[]
        for rows in reader:
                if rows[0]==usr_name:
                   print("Which information you want to update")
                   print(" Enter 1 for Name","\n","Enter 2 for Mobile Numeber","\n","Enter 3 for Email id","\n","Enter 4 for address","\n","Enter 5 for password","\n","Enter 0 for Main Menu")
                   edit_key=int(input("Please Enter your Choice"))
                   if edit_key==1:
                       rows[1]=input("Please Enter New Name :")
                   elif edit_key==2:
                       rows[2]=input("Please Enter New Mobile Number :")
                   elif edit_key==3:
                       rows[3]=input("Please Enter New E-mail id :")
                   elif edit_key==4:
                       rows[4]=input("Please Enter New Address :")
                   elif edit_key==5:
                       rows[5]=input("Please Enter New Password :")
                   elif edit_key==0:
                           user_menu()
                   found=True
                temp_data.append(rows)
        if found == False:
            f.close()
        else:
            f = open("userdata.csv","w+",newline="")
            writer=csv.writer(f)
            writer.writerows(temp_data)
            f.seek(0)
            f.close()
            print("-----------Profile Updated-----------")
            View_profile()



    





def order_history():
    df = pd.read_csv('orders.csv')
    fltr = df["user_name"]==usr_name
    history = df[fltr]
    a= history.iloc[:,1:]
    print(a)






