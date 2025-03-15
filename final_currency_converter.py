import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class CurrencyConverter():

    #constructor ce preia APi-ul cu valorile monezilor si transforma site-ul in format JSON
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.rates = self.data['rates']
    
    #calculul conversiei
    def conversion(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]

        amount = amount * self.rates[to_currency]
        return amount
    
class Interface(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.configure(bg = '#292933')
        self.currency_converter = converter
        self.geometry("350x400")
        self.wm_title("Currency Convertor")
        
        #meniul de introducere si afisare al valorii monedelor
        self.input_amount = Entry(self, fg = 'white', bg = '#57576b')
        self.output_amount = Label(self, text = "", fg = 'white', bg = '#57576b', width = 17)
        self.from_text = Label(self, text = "FROM:", fg = 'white', bg = '#292933')
        self.to_text = Label(self, text = "TO:", fg = 'white', bg = '#292933')
        self.title = Label(self, text = "Currency Converter", font = ('Courier',15,'bold') , fg = 'white', bg = '#292933')

        #meniul in care se aleg monedele
        self.from_currency_converter = StringVar(self)
        self.from_currency_converter.set("EUR")
        self.to_currency_converter = StringVar(self)
        self.to_currency_converter.set("RON")
        self.dropdown_menu_from = ttk.Combobox(self,textvariable = self.from_currency_converter,
        values=list(self.currency_converter.rates.keys()), state= 'readonly')
        self.dropdown_menu_to = ttk.Combobox(self,textvariable = self.to_currency_converter,
        values=list(self.currency_converter.rates.keys()), state= 'readonly')

        #buton ce realizeaza conversia
        self.conversion_button = Button(self, text = "Convert", command = self.conversion_fct, fg = 'white', bg = '#57576b')

        #afisare meniuri
        self.title.place(x = 70, y = 250)
        self.from_text.grid(row = 0, column = 0)
        self.dropdown_menu_from.grid(row = 0, column = 1, padx = 5, pady = 50)
        self.to_text.grid(row = 1, column = 0)
        self.input_amount.grid(row = 0, column = 2)
        self.dropdown_menu_to.grid(row = 1, column = 1)
        self.output_amount.grid(row = 1, column = 2)
        self.conversion_button.place(x = 265, y = 170)

    def conversion_fct(self):
        
        #preia input-ul din entry box si din meniurile dropdown
        amount_to_covnert = float(self.input_amount.get())
        from_currency_var = self.from_currency_converter.get()
        to_currency_var = self.to_currency_converter.get()

        #apeleaza functia ce calculeaza valoarea convertita
        amount_converted = self.currency_converter.conversion(from_currency_var, to_currency_var, amount_to_covnert)
        amount_converted = round(amount_converted, 2)

        #modifica valoarea afisata in label-ul de output    
        self.output_amount.config(text = str(amount_converted))

url = 'https://api.exchangerate-api.com/v4/latest/USD'
app = CurrencyConverter(url)
Interface(app)

mainloop()
        