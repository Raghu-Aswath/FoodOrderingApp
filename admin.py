
import inventory as inv
import csv
import pandas as pd
import math,random


admin_keys={"Admin1":"rfc@1","Admin2":"rfc@2","Admin3":"rfc@3"}


def admin_login():
    print("*"*50)
    print("Welcome Raghu's Food Court to Admin panel")
    print("*"*50)
    password = admin_keys["Admin1"]
    usr=input("Please Enter Admin ID :")
    if usr not in admin_keys:
        print("Admin ID not found Contact Support")
    else:
        psd = input("Enter Your Password :")
        if psd != password:
            print("your Password is Incorrect")
        else:
            switch =True
            while switch:
                print("*"*50)
                print("Welcome Raghu's Food Court to Admin panel")
                print("*"*50)
                print(" Enter 1 to view Inventory", "\n", "Enter 2 add Items to inventory", "\n", "Enter 3 to Edit Item in Inventory","\n","Enter 4 to delete Items in Inventory","\n","Enter 5 to Logout")
                print("*"*50)
                key = int(input("Please Enter Your Choice"))
                try:
                    if key ==1:
                        inv.Show_inventory()
                    elif key ==2:
                        add_to_inventory()
                    elif key ==3:
                        edit_item()
                    elif key==4:
                        delete_item()
                    elif key ==5:
                        print("*"*20,"Logout Successful","*"*20)
                        switch=False
                        admin_login()
                    
                    else:
                        print("Something Went Wrong Contact Support")
                        admin_login()
                except:
                    pass
                
        
            



def gen():
        digits="0123456789"
        food_id = ""
        for i in range(3):
            food_id=food_id+digits[math.floor(random.random()*5)]
        return food_id






def add_to_inventory():
        print("*"*50)
        print("Welcome Fill the details below to add items")
        print("*"*50)
        switch = True
        while switch:
                food_id=gen()
                food_name = input("Enter Name of Food :")
                food_Qty = input("Enter the quantity :")
                food_price = int(input("Enter the Price :"))
                food_discount = int(input("Enter Discount% if applicable :"))
                food_stock = int(input("Enter Stock available :"))
                file = open("inventory.csv",'a',newline='')
                writer = csv.writer(file)
                writer.writerow(["RFC"+food_id,food_name,food_Qty,food_price,food_discount,food_stock])
                file.close
                data = pd.read_csv("inventory.csv")
                lst = data.iloc[:,0:1].values
                lst1= [x for xs in lst for x in xs]
                print("*"*50)
                option = input("Do you want to add one more item enter [YES/NO] :")
                if option.lower()=='no':
                        print("************Inventory Updated***********")
                        file.close
                        inv.Show_inventory()
                        switch=False
                        break
        
    
    



def edit_item():
        inv.Show_inventory()
        f = open("inventory.csv","r")
        reader=csv.reader(f)
        found=False
        temp_data=[]
        food_id= input("Enter Food Id which You wish to edit  :")
        for rows in reader:
                if rows[0]==food_id.upper():
                   rows[1]=input("Enter Name of Food :")
                   rows[2]=input("Enter the quantity :")
                   rows[3]=int(input("Enter the Price :"))
                   rows[4]=int(input("Enter Discount% if applicable :"))
                   rows[5]=int(input("Enter Stock available :"))
                   found=True
                temp_data.append(rows)
        if found==False:
                print("*"*50)
                print("Sorry Food Id not found try again")
                print("*"*50)
                edit_item()
                f.close
        else:
             f = open("inventory.csv","w+",newline="")
             writer=csv.writer(f)
             writer.writerows(temp_data)
             f.seek(0)
             f.close()
             print("-----------Inventory Updated-----------")
             inv.Show_inventory()
             print("*"*50)
             print("Enter 1 edit one more or 2 to exit  :")
             option=int(input("choose your option :"))
             if option==1:
                        edit_item()
             else:
                pass
                

def delete_item():
        inv.Show_inventory()
        f = open("inventory.csv","r")
        reader=csv.reader(f)
        found=False
        temp_data=[]
        food_id= input("Enter Food Id which You wish to Delete  :")
        for rows in reader:
                if rows[0]==food_id.upper():
                   found=True
                else:
                     temp_data.append(rows)
        if found==False:
                print("*"*50)
                print("Sorry Food Id not found try again")
                print("*"*50)
                delete_item()
                f.close
        else:
             f = open("inventory.csv","w+",newline="")
             writer=csv.writer(f)
             writer.writerows(temp_data)
             f.seek(0)
             f.close
             print()
             print("-----------Inventory Updated-----------")
             inv.Show_inventory()
             print("*"*50)
             print("Enter 1 delete one more or 2 to exit  :")
             option=int(input("choose your option :"))
             if option==1:
                        delete_item()
             else:
                pass
