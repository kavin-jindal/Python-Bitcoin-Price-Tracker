from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime
import tkinter.ttk as ttk
from PIL import ImageTk, Image

#import win32gui, win32con


#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)
root = Tk()
root.configure(bg='white')
root.title('Bitcoin Price')
root.resizable(False, False)
root.geometry('1000x1000')
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")
global previous
previous = False

'''
logo = PhotoImage(file='K:/programming/bitcoin/bit.png')
logo_label = Label(root, image=logo, bd=0)
logo_label.pack()'''
def Update():
    global previous

    page = urllib.request.urlopen('https://www.coindesk.com/price/bitcoin').read()
    html = BeautifulSoup(page, 'html.parser')
    price_large = html.find(class_ = 'price-large')
    print(price_large)

    price_large1 = str(price_large)

    price_large2 = price_large1[54:63]

    bit_label.config(text=f'${price_large2}')


    root.after(30000, Update)

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
        
bit_emo = Label(root, text='₿', font=('Consolas', 100), fg='orange', bg='white')
head = Label(root, text='Bitcoin Price', font=('Verdana', 50), bg='white')
bit_label = Label(root, text='TEST', font=('Consolas', 36), bg='white')
status_bar = Label(root, text=f'Last Updated {current_time}   ',
	bd=0,
	anchor=E,
	bg="black",
	fg="grey")
status_bar.pack(fill=X, side=TOP, ipady=2)
bit_emo.pack()
head.pack()
bit_label.pack()
lprice_label = Label(root, text='move test', font=('Consolas', 36), bg='white')
lprice_label.pack()


Update()
root.mainloop()