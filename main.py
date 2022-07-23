
import admin
import user


print("*" * 50)
print("Weelcome to Raghu's Food Court")
print("*" * 50)
print("-"*20)
print("|",1,"|", "Admin Login")
print("-"*20)
print("-"*20)
print("|",2,"|", "User Login")
print("-"*20)
print("-"*20)
print("|",3,"|", "Exit")
print("-"*20)
print("*" * 50)
admin_crawler = True
while admin_crawler:
    
    inp = int(input("Where You want to login select"))
    if inp == 1:
        admin.admin_login()
    elif inp==2:
        print("-"*20)
        print("|",1,"|", "Login","|")
        print("-"*20)
        print("-"*20)
        print("|",2,"|", "Singup or Register","|")
        print("-"*20)
        inp2=input("Please Enter your Choice")
        if inp2=="2":
            user.register_new_user()
        elif inp2=="1":
            user.login()
        else:
            pass
    elif inp==3:
        admin_crawler = False
        break
    else:
        pass
        

            
