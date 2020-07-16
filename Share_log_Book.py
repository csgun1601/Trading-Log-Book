# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:29:55 2020

@author: Chaitanya Guntoorkar

Project: Share Market Logbook
"""

import pandas as pd
from csv import writer

def cal_commi(Brokerage, STGST, STT, Stamp_value, trans_charges):
    return Brokerage + STGST + STT + Stamp_value + trans_charges

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def change_sell_date(df, date, num):
    df.at[df[df['SrNo']==num].index.values,'Date_of_sell'] = date
    
def change_qty_sold(df, qty, num):
    df.at[df[df['SrNo']==num].index.values,'Quantity_sold'] = qty
    
def change_rate_of_sell(df, rate, num):
    df.at[df[df['SrNo']==num].index.values,'Rate_of_sell'] = rate
    
def change_amount_sold(df, amount, num):
    df.at[df[df['SrNo']==num].index.values,'Amount_sold'] = amount

def change_commie_minus(df, commi, num):
    df.at[df[df['SrNo']==num].index.values,'commission_minus'] = commi
    
def change_net_amount_sold(df, net, num):
    df.at[df[df['SrNo']==num].index.values,'Net_amount_sold'] = net
    
def change_net_profit(df, profit, num):
    df.at[df[df['SrNo']==num].index.values,'Net_profit'] = profit
    
    
print('Welcome Back!!!')

FLAG = True
while FLAG == True:
    print('What do you want to do today? ')
    print('Want to enter a new transaction? (Enter N)')
    print('Want to update an existing Transaction? (Enter U)')
    print('Are you here just for statistics? (Enter S)')
    print('Do you want to see all transactions? (Enter A)')
    df = pd.read_csv(r'C:\Users\ASUS\Desktop\Share_data.csv')
    n = df.shape[0]
    print('The latest serial number is: ', n)
    
    p = True
    while p == True:
        Task = input('Enter your response (N/U/S/A): ')

        if Task == 'N':
            Flag = True
            while Flag == True:
                SrNo = input('Enter the serial number: ')                                                                                   # yet to figure out
                Date_of_buy = input('Enter the date in the format dd/mm/yyyy: ')
                Name_of_the_share = input('Enter the name of the share: ')
                Quantity_bought = int(input('Enter the quantity of shares bought: '))
                Rate_per_share = int(input('Enter the rate per share: '))
                Total_amount_bought = Quantity_bought * Rate_per_share
                print('Now to calculate the total commission(plus) enter following information:')
                Brokerage = int(input('The brokerage: '))
                STGST = int(input('ST/GST: '))
                STT = int(input('STT: '))
                Stamp_value = int(input('The Stamp Value: '))
                trans_charges = int(input('The Transaction Charges: '))
                commission_plus = cal_commi(Brokerage, STGST, STT, Stamp_value, trans_charges)
                Net_purchase_amount = Total_amount_bought + commission_plus
                
                choice = input("Do you have any information about this share's selling? (yes/no): ")
                if choice == 'yes':
                    Date_of_sell = input('Enter the date you sold the shares (in the dd/mm/yyyy format): ')
                    Quantity_sold = int(input('Enter the quantity of shares sold: '))
                    Rate_of_sell = int(input('Enter the rate at which you sold the shares: '))
                    Amount_sold = Quantity_sold * Rate_of_sell
                    print('Now to calculate the total commission(minus) enter following information:')
                    Brokerage = int(input('The brokerage: '))
                    STGST = int(input('ST/GST: '))
                    STT = int(input('STT: '))
                    Stamp_value = int(input('The Stamp Value: '))
                    trans_charges = int(input('The Transaction Charges: '))
                    commission_minus = cal_commi(Brokerage, STGST, STT, Stamp_value, trans_charges)
                    Net_amount_sold = Amount_sold - commission_minus
                    Net_profit = Net_purchase_amount - Net_amount_sold
                else:
                    Date_of_sell = None
                    Quantity_sold = None
                    Rate_of_sell = None
                    Amount_sold = None
                    commission_minus = None
                    Net_amount_sold = None
                    Net_profit = None
                lst = [SrNo,Date_of_buy,Name_of_the_share,Quantity_bought,Rate_per_share,Total_amount_bought,commission_plus,Net_purchase_amount,Date_of_sell,Quantity_sold,Rate_of_sell,Amount_sold,commission_minus,Net_amount_sold,Net_profit
]
                append_list_as_row('Share_data.csv', lst)
                print('Successfully added!!')
                fl = True
                while fl == True:
                    option = input('Do you have another new entry? (yes/no):')
                    if option == 'yes':
                        Flag = True
                        fl = False
                    elif option == 'no':
                        Flag = False
                        fl = False
                    else:
                        print('Invalid Response! Try Again.....')
                        fl = True
            p =False
            
        elif Task == 'S':
            df = pd.read_csv(r'C:\Users\ASUS\Desktop\Share_data.csv')
            print('Total amount bought = {}'.format(df['Total_amount_bought'].sum()))
            print('Total commission(positive) till now = {}'.format(df['commission_plus'].sum()))
            print('Total Amount purchased till now = {}'.format(df['Net_purchase_amount'].sum()))
            print('Total amount sold till now = {}'.format(df['Amount_sold'].sum()))
            print('Total commission(minus) till now  = {}'.format(df['commission_minus'].sum()))
            print('Net amount sold till now = {}'.format(df['Net_amount_sold'].sum()))
            print('Your net profit till now = {}'.format(df['Net_profit'].sum()))
            p = False


        elif Task == 'U':
            flag = True
            while flag == True:
                num = int(input("Enter the serial number of the entry you want to work on: "))
    
                df = pd.read_csv(r'C:\Users\ASUS\Desktop\Share_data.csv')
                #print(df)
                Net_purchase_amount = df.loc[df.SrNo == num, 'Net_purchase_amount'].values[0]
                
                Date_of_sell = input('Enter the date you sold the shares (in the dd/mm/yyyy format): ')
                Quantity_sold = int(input('Enter the quantity of shares sold: '))
                Rate_of_sell = int(input('Enter the rate at which you sold the shares: '))
                Amount_sold = Quantity_sold * Rate_of_sell
                print('Now to calculate the total commission(minus) enter following information:')
                Brokerage = int(input('The brokerage: '))
                STGST = int(input('ST/GST: '))
                STT = int(input('STT: '))
                Stamp_value = int(input('The Stamp Value: '))
                trans_charges = int(input('The Transaction Charges: '))
                commission_minus = cal_commi(Brokerage, STGST, STT, Stamp_value, trans_charges)
                Net_amount_sold = Amount_sold - commission_minus
                Net_profit = Net_purchase_amount - Net_amount_sold
    
                change_sell_date(df, Date_of_sell, num)
                change_qty_sold(df, Quantity_sold, num)   
                change_rate_of_sell(df, Rate_of_sell, num)
                change_amount_sold(df, Amount_sold, num)
                change_commie_minus(df, commission_minus, num)
                change_net_amount_sold(df, Net_amount_sold, num)
                change_net_profit(df, Net_profit, num)
    
                df.to_csv(r'C:\Users\ASUS\Desktop\Share_data.csv', index=False)
        
                print('Successfully updated!!!')
                f = True
                while f == True:
                    op = input('Do you want to update any other transaction? (yes/no): ')
                    if op == 'yes':
                        flag = True
                        f = False
                    elif op == 'no':
                        flag = False
                        f = False
                    else:
                        print('invalid command!')
                        f = True
            p = False
    
        elif Task == 'A':
            print(df)
            p = False
        else:
            print('Invalid Response! Try Again....')
            p = True
    w = True
    while w == True:
        q = input('Do you want to see the start menu again? (yes/no): ')
        if q == 'yes':
            FLAG = True
            w = False
        elif q == 'no':
            FLAG = False
            print('Thank you!!')
            w = False
        else:
            print('Invalid Response! Try again...')
            w = True
            
        
        
    