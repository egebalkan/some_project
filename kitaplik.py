import pandas as pd
import numpy as np
import Tkinter as tk
import csv

window = tk.Tk()

window.title("Arayan Bulur")
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

def kitap_ekle():
    f = open("books.csv","a+")
    
    kitap = raw_input("Kitap ismi girin \n")
    yazar = raw_input("Yazar ismi girin \n")
    yer   = raw_input("Kitap nerede? \n")
    
    f.write(kitap +","+ yazar +","+ yer +"\n")
    f.close()
 
def kitap_ara():
    try:
        
        books=pd.read_csv("books.csv")
        kitap = raw_input("Kitap ismi girin \n")
        index = books[books['Kitap']==kitap].index[0]
        book_found = books.iloc[index]
        print("Kitap bulundu! \n")
        print(book_found)
        
    except IndexError as noBook:
            print("Kitap bulunamadi! \n")

#Kitap
def books():
    fr_main.grid_forget()
    fr_book = tk.Frame()  
    fr_book.grid()
    frame = fr_book
    
    btn_search = tk.Button(
        fr_book,
        text="Kitap Ara",
        command = kitap_ara
        )
    btn_add = tk.Button(
        fr_book,
        text="Kitap Ekle",
        command = kitap_ekle
        )
    btn_back = tk.Button(
        fr_book,
        text = "Anasayfa",
        command = main(frame)
        )
    btn_search.grid(row = 0, column= 0 , sticky="ew", padx=10, pady=10)
    btn_add.grid(   row = 0, column= 2 , sticky="ew", padx=10)
    btn_back.grid(  row = 1, column = 1, sticky="ew")



def main(frame):
    frame.grid_forget()
    #fr_main = tk.Frame(window)
    fr_main.grid()

    btn_book = tk.Button(
        fr_main,
        text = "Kitap",
        command = books
        )

    btn_cd = tk.Button(
        fr_main,
        text = "CD"
        )

    btn_dvd = tk.Button(
        fr_main,
        text = "DVD"
        )

    btn_book.grid( row = 0, column = 0, sticky = "ew", padx=10, pady=5)
    btn_cd.grid(   row = 0, column = 1, sticky = "ew", padx=10, pady=5)
    btn_dvd.grid(  row = 0, column = 2, sticky = "ew", padx=10, pady=5)

    

fr_main = tk.Frame(window)
fr_book = tk.Frame()

frame = fr_book
main(frame)
window.mainloop() 
 


##fr_main = tk.Frame(window)
##fr_main.grid()
##
##btn_book = tk.Button(
##    fr_main,
##    text = "Kitap",
##    command = books
##    )
##
##btn_cd = tk.Button(
##    fr_main,
##    text = "CD"
##    )
##
##btn_dvd = tk.Button(
##    fr_main,
##    text = "DVD"
##    )
##
##btn_book.grid( row = 0, column = 0, sticky = "ew", padx=10, pady=5)
##btn_cd.grid(   row = 0, column = 1, sticky = "ew", padx=10, pady=5)
##btn_dvd.grid(  row = 0, column = 2, sticky = "ew", padx=10, pady=5)














'''


fr_buttons.grid(row=0, column=0, sticky="ns")
fr_search.grid(row=0, column=1, sticky="nsew")
'''





    
