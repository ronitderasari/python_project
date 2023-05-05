from tkinter import *
import os
master=Tk()
master.title("My Bank")
def Login():
    global Username
    global Password
    global login_screen
    global login_notif
    login_screen=Toplevel(master)
    login_screen.title('Login dashboard')
    Username=StringVar()
    Password=StringVar()
    Button(login_screen,text='Login',command=login_session).grid(row=5,column=0)
    Label(login_screen,text="Username:-").grid(row=1,column=0)
    Label(login_screen,text="Password:-").grid(row=2,column=0)
    l2=Label(login_screen)
    Entry(login_screen,textvar=Username).grid(row=1,column=1)
    Entry(login_screen,textvar=Password).grid(row=2,column=1)
    l2
    login_notif=Label(login_screen)
    login_notif.grid(row=6)
def login_session():
    global login_username
    global login_password
    login_username=Username.get()
    login_password=Password.get()
    all_accounts=os.listdir()
    if login_username in all_accounts:
        file=open(login_username,'r')
        file_data=file.read()
        file_data=file_data.split('\n')
        
        password=file_data[3]
        if password==login_password:
            login_screen.destroy()
            account_dashboard=Toplevel(master)
            account_dashboard.title('Dashboard')
            Label(account_dashboard,text='account dashboard').grid(row=0)
            Label(account_dashboard,text='welcome').grid(row=1)
            Button(account_dashboard,text='Personal details',command=personal_details).grid(row=2)
            Button(account_dashboard,text='Deposit',command=Deposit).grid(row=3)
            Button(account_dashboard,text='Withdraw',command=Withdraw).grid(row=4)
            Label(account_dashboard).grid(row=5)
        else:
            login_notif.config(fg='red',text='Password incorrect')
    else:
        login_notif.config(fg='red',text='No account found')
def personal_details():
    file=open(login_username,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_username=user_details[0]
    details_age=user_details[1]
    details_gender=user_details[2]
    details_balance=user_details[4]
    print(file_data)
    
    personal_details_screen=Toplevel(master)
    personal_details_screen.title('Personal details')
    
    Label(personal_details_screen,text='Personal details').grid(row=0)
    Label(personal_details_screen,text='Username: '+details_username).grid(row=1)
    Label(personal_details_screen,text='Age: '+details_age).grid(row=2)
    Label(personal_details_screen,text='Gender: '+details_gender).grid(row=3)
    Label(personal_details_screen,text='balance: '+details_balance).grid(row=4)
def Deposit():
    global amount
    global deposit_notif
    global current_balance_label
    
    amount=StringVar()
    file=open(login_username,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    
    deposit_screen=Toplevel(master)
    deposit_screen.title('Deposit')
    
    Label(deposit_screen,text="desposit").grid(row=0)
    current_balance_label=Label(deposit_screen,text='Current balance: RS.'+user_details[4])
    current_balance_label.grid(row=1)
    Label(deposit_screen,text='Amount :').grid(row=2)
    deposit_notif=Label(deposit_screen)
    deposit_notif.grid(row=4)
    Entry(deposit_screen,textvariable=amount).grid(row=2,column=1)
    Button(deposit_screen,text='Finish',command=finish_deposit).grid(row=3)
def finish_deposit():
    if amount.get()=='':
        deposit_notif.config(text='Amount is required*',fg='red')
        return
    if float(amount.get())<=0:
        deposit_notif.config(text="negative amount cant be inserted*",fg='red')
        return
    file=open(login_username,'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    updated_balance=float(current_balance)+float(amount.get())
    file_data=file_data.replace(current_balance,str(updated_balance))
    print(file_data)
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text='Current Balance : Rs-'+str(updated_balance),fg='green')
    deposit_notif.config(text="balance Updated",fg='green')
def Withdraw():
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount=StringVar()
    file=open(login_username,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    
    withdraw_screen=Toplevel(master)
    withdraw_screen.title('Withdraw')
    
    Label(withdraw_screen,text='Withdraw').grid(row=0)
    current_balance_label=Label(withdraw_screen,text='Current balance: RS.'+user_details[4])
    current_balance_label.grid(row=1)
    Label(withdraw_screen,text='Amount :').grid(row=2)
    withdraw_notif=Label(withdraw_screen)
    withdraw_notif.grid(row=4)
    Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1)
    Button(withdraw_screen,text='Finish',command=finish_withdraw).grid(row=3)
def finish_withdraw():
    if withdraw_amount.get()=='':
        withdraw_notif.config(text='Amount is required*',fg='red')
        return
    if float(withdraw_amount.get())<=0:
        withdraw_notif.config(text="negative amount cant be inserted*",fg='red')
        return
    
    file=open(login_username,'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    if float(withdraw_amount.get())>float(current_balance):
        withdraw_notif.config(text='insufficient balance*',fg='red')
    updated_balance=float(current_balance)-float(withdraw_amount.get())
    file_data=file_data.replace(current_balance,str(updated_balance))
    print(file_data)
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text='Current Balance : Rs-'+str(updated_balance),fg='green')
    withdraw_notif.config(text="balance Updated",fg='green')
def finish_reg():
    name=Name.get()
    age=Age.get()
    gender=Gender.get()
    password=Password.get()
    balance=Balance.get()
    all_accounts=os.listdir()
    
    if name=='' or age=="" or gender=='' or password=='' or balance=='':
        notif.config(fg='red',text='All field required')
        return
    for Name_check in all_accounts:
        if Name==Name_check:
            notif.config(fg='red',text='Account already exists')
            return
        else:
            new_file=open(name,'w')
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.write(balance+'\n')
            new_file.close()
            notif.config(fg='green',text='Account has been created')
    
    
def Register():
    global Name
    global Age
    global Gender
    global Password
    global Balance
    global notif
    
    register_screen=Toplevel(master)
    register_screen.title('Register dashboard')
    Name=StringVar()
    Age=StringVar()
    Password=StringVar()
    Gender=StringVar()
    Balance=StringVar()
    Button(register_screen,text='Register',command=finish_reg).grid(row=5,column=0)
    Label(register_screen,text='Name').grid(row=0,column=0)
    Label(register_screen,text='Age').grid(row=1,column=0)
    Label(register_screen,text='Gender').grid(row=2,column=0)
    Label(register_screen,text='Password').grid(row=3,column=0)
    Label(register_screen,text='Balance').grid(row=4,column=0)
    l3=Label(register_screen)
    Entry(register_screen,textvar=Name).grid(row=0,column=1)
    Entry(register_screen,textvar=Age).grid(row=1,column=1)
    Entry(register_screen,textvar=Gender).grid(row=2,column=1)
    Entry(register_screen,textvar=Password).grid(row=3,column=1)
    Entry(register_screen,textvar=Balance).grid(row=4,column=1)
    l3
    notif=Label(register_screen)
    notif.grid(row=6)
Button(text='Login',command=Login).grid(row=10,column=0)
Button(text='Register',command=Register).grid(row=12,column=0)
Label(text="Welcome to my Bank").grid(row=2,column=0)
Label(text='Customer satisfaction is our moto').grid(row=4,column=0)
l1=Label(master)
l1.grid(row=5,column=0)
master.mainloop()
l1