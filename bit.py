from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context
#import win32gui, win32con


#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)
root = Tk()
root.configure(bg='white')
root.title('Bitcoin Tracker by Kavin Jindal v1.3')
root.resizable(False, False)
root.geometry('420x420')
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")
global previous
previous = False

my_notebook = ttk.Notebook(root)
my_notebook.pack()


frame2 = Frame(my_notebook, width=1000, height=1000, bg="white")

frame2.pack(fill="both", expand=10)
my_notebook.add(frame2, text="Home")

'''
logo = PhotoImage(file='K:/programming/bitcoin/bit.png')
logo_label = Label(root, image=logo, bd=0)
logo_label.pack()'''
def Update():
    global previous

    page = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json' , verify = False)
    data = page.json()
    price_large2 = data["bpi"]["USD"]["rate"]    #price_large = html.find(class_ = 'price-large')
    #print(price_large2)

    #price_large1 = str(price_large)

    #price_large2 = price_large1[54:63]

    bit_label.config(text=f'${price_large2}')


    frame2.after(30000, Update)

    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")

    current = price_large2
    status_bar.config(text=f'Last Updated: {current_time}   ')


    current = current.replace(',','')

    if previous:
        if float(previous) > float(current):
            lprice_label.config(text=f'-{round(float(previous) - float(current), 2)}', fg='red')

        elif float(previous) == float(current):
            lprice_label.config(text='+0.00', fg='grey')

        else:
            lprice_label.config(text=f'+{round(float(current) - float(previous), 2)}', fg='green')






    else:
        previous = current
        lprice_label.config(text='+0.00', fg='grey')
        
bit_emo = Label(frame2, text='₿', font=('Consolas', 100), fg='orange', bg='white')
head = Label(frame2, text='Bitcoin Price', font=('Verdana', 50), bg='white')
bit_label = Label(frame2, text='TEST', font=('Consolas', 36), bg='white')
status_bar = Label(frame2, text=f'Last Updated {current_time}   ',
	bd=0,
	anchor=E,
	bg="black",
	fg="grey")
status_bar.pack(fill=X, side=TOP, ipady=2)
bit_emo.pack()
head.pack()
bit_label.pack()
lprice_label = Label(frame2, text='Developed by Kavin Jindal', font=('Consolas', 36), bg='white')
lprice_label.pack()


Update()
root.mainloop()
