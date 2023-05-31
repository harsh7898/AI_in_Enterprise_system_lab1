import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import itertools

class bank:
    def __init__(self):
        self.lst = []
        self.eidl = []
        self.l=[]
        self.df = pd.DataFrame(self.l, columns=['Name','Emailid', 'Acct_no', 'Total_balance'])
    
    def intro(self):
        print('_________________________________________')
        print('*********BANK MANAGEMENT SYSTEM********')
        print('_________________________________________')
        print('------MAIN MENU------\n')
        print('What would you like to choose')
        while True:
            try:
                options = int(input('Press 1 to Create new account\nPress 2 to Perform account deposit\nPress 3 to Perform account withdrawal\nPress 4 to Transfer money between accounts\nPress 5 to view account balance\nPress 6 to quit\n'))
                break
            except ValueError:
                print('"Invalid input, please enter a valid number."')

        if int(options) ==1:
            print('Create new account ')
            self.createacct()
#             print(self.df)
        elif int(options)==2:
            print('Perform account deposit')
            self.deposit()
        elif int(options)==3:
            print('Perform account withdraws')
            self.withdrawal()
        elif int(options)==4:
            print('Transfer money between accounts')
            self.transfer()
        elif int(options)==5:
            self.totbal()
        elif int(options)==6:
            print('Quit')
        else:
            print('Invalid option entered. Please try again')
            self.intro()
    
    
    def createacct(self):
        self.fn = input('Please enter your full name :')
        self.eid = input('Please enter your email id :')
        self.eidl.append(self.eid)
    
        print('Creating your new account.....')
        for i in range(1,1000,1):
            if i not in self.lst:
                self.lst.append(i)
                break
        while True:
            try:
                minm = int(input("Please add amount to your account: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        d={'Name':str(self.fn),'Emailid':str(self.eid),'Acct_no':int(i),'Total_balance':int(minm)}
        self.l.append(d)
        print('Your New Account Number:',d)
        self.df = pd.DataFrame(self.l, columns=['Name','Emailid', 'Acct_no', 'Total_balance'])
        cont = input('Press any value to return to main menu:')
        print('Returning To Main Menu...')
        self.intro()
        
    def deposit(self):
        self.eid = input('Please enter your mail id. :')
        self.dfd=self.df.loc[self.df['Emailid'] == self.eid]
        if (self.dfd.empty == True):
            print('User id not found')
            cont = input('Press any value to return to main menu:')
            print('Returning To Main Menu...')
            self.intro()
        while True:
            try:
                self.dact = int(input('Please enter your acct no.'))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        self.df.set_index('Acct_no',drop=False,inplace=True)
        self.df.rename_axis(None, axis=0,inplace=True)
        for index, row in self.df.iterrows():
            if row['Emailid'] == self.eid and row['Acct_no']==self.dact:
                while True:
                    try:
                        dp = int(input('Enter deposit amount:'))
                        break
                    except ValueError:
                        print("Invalid input, please enter a valid number.")
                self.df.at[index, 'Total_balance'] = self.df.at[index, 'Total_balance'] +dp
                for item in self.l:
                    if item['Acct_no'] == self.dact:
                        item['Total_balance'] +=dp
                print('Deposit Successful\nTotal balance :',self.df.at[index,'Total_balance'])
                break
        else:
            print('Incorrect Acct no.')
        cont = input('Press any value to return to main menu:')
        print('Returning To Main Menu...')
        self.intro()
            
    def withdrawal(self):
        de = input('Please enter your mail id. :')
        self.dfd=self.df.loc[self.df['Emailid'] == de]
        if (self.dfd.empty == True):
            print('User id not found')
            cont = input('Press any value to return to main menu:')
            print('Returning To Main Menu...')
            self.intro()
            
        while True:
            try:
                self.dact = int(input('Please enter your acct no.'))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        self.df.set_index('Acct_no',drop=False,inplace=True)
        self.df.rename_axis(None, axis=0,inplace=True)
        for index, row in self.df.iterrows():
            if row['Emailid'] == de and row['Acct_no']==self.dact:
                while True:
                    try:
                        dp = int(input('Enter withdrawal amount:'))
                        break
                    except ValueError:
                        print("Invalid input, please enter a valid number.")
                if (self.df.at[index, 'Total_balance'] -dp) >= 0:
                    self.df.at[index, 'Total_balance'] = self.df.at[index, 'Total_balance'] -dp
                    for item in self.l:
                        if item['Acct_no'] == self.dact:
                                item['Total_balance'] -=dp
                    print('Withdrawal Successful\nTotal balance :',self.df.at[index,'Total_balance'])
                    break
                else:
                    print('Insufficient balance')
                    break
        else:
            print('Incorrect Acct no.')
        cont = input('Press any value to return to main menu:')
        print('Returning To Main Menu...')
        self.intro()
            
    def transfer(self):
        self.de = input('Please enter your mail id. :')
        self.dfd=self.df.loc[self.df['Emailid'] == self.de]
        if (self.dfd.empty == True):
            print('User id not found')
            cont = input('Press any value to return to main menu:')
            print('Returning To Main Menu...')
            self.intro()

        while True:
            try:
                self.dact = int(input('Please enter your acct no.'))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        self.df.set_index('Acct_no',drop=False,inplace=True)
        self.df.rename_axis(None, axis=0,inplace=True)
        while True:
            try:
                self.dact1 = int(input('Please enter acct no to transfer money in :'))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        for index, row in self.df.iterrows():
            if row['Emailid'] == self.de and row['Acct_no']==self.dact:
                if self.dact and self.dact1:
                    while True:
                        try:
                            dp = int(input('Enter amount to transfer :'))
                            break
                        except ValueError:
                            print("Invalid input, please enter a valid number.")
                    if self.df.at[index,'Total_balance'] >= dp:
                        self.df.at[index, 'Total_balance'] = self.df.at[index, 'Total_balance'] -dp
                        for item in self.l:
                            if item['Acct_no'] == self.dact:
                                item['Total_balance'] -=dp
                        while True:
                            try:
                                credit_index = self.df[self.df['Acct_no'] == self.dact1].index[0]
                                break
                            except IndexError:
                                print('Account no. not found while transferring')
                                self.df.at[index, 'Total_balance'] = self.df.at[index, 'Total_balance'] +dp
                                for item in self.l:
                                    if item['Acct_no'] == self.dact:
                                        item['Total_balance'] +=dp
                                self.intro()
                        self.df.at[credit_index, 'Total_balance'] = self.df.at[credit_index, 'Total_balance'] +dp
                        for item in self.l:
                            if item['Acct_no'] == self.dact1:
                                item['Total_balance'] +=dp
                        
                        print('\nAmount to be Transfered :',dp)
                        print('Total balance in account no.'+str(self.dact)+' after debit :',self.df.at[index,'Total_balance'])
                        print('Total balance in account no.'+str(self.dact1)+' after credit :',self.df.at[credit_index,'Total_balance'])
                        break
                    else:
                        print('Insufficient balance')
                        break
        else:
            print('Your Acct no. is incorrect')
        cont = input('Press any value to return to main menu:')
        print('Returning To Main Menu...')
        self.intro()
            
    def totbal(self):
        de = input('Please enter your mail id. :')
        self.dfd=self.df.loc[self.df['Emailid'] == de]
        if (self.dfd.empty == True):
            print('User id not found')
            cont = input('Press any value to return to main menu:')
            print('Returning To Main Menu...')
            self.intro()

        while True:
            try:
                dact = int(input('Please enter your acct no.'))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        self.df.set_index('Acct_no',drop=False,inplace=True)
        self.df.rename_axis(None, axis=0,inplace=True)
        for index, row in self.df.iterrows():
            if row['Emailid'] == de and row['Acct_no']==dact:
                print('Total balance :',self.df.at[index,'Total_balance'])
                break
        else:
            print('Incorrect Acct no.')
        cont = input('Press any value to return to main menu:')
        print('Returning To Main Menu...')
        self.intro()
        


a = bank()
r = a.intro()