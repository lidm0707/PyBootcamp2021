from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# MAIN UI
GUI= Tk()
GUI.title('HW 1 for cal')
GUI.geometry('800x600')

#FONT
FONT1 = ('Angsana NEW',20 )
FONT2 = ('Angsana NEW',15 )
#Desciption
L = ttk.Label(GUI,text = 'calculate VAT 7%', font = FONT1)
L.pack()

#BOX INPUT
v_inventory1 = StringVar()
v_number1 = IntVar()
v_number2 = IntVar()

L2 = ttk.Label(GUI,text = 'Name inventory', font = FONT2)
L2.pack()
E1 = ttk.Entry(GUI,textvariable = v_inventory1, font = FONT1,width=40)
E1.pack(pady=10)

L3 = ttk.Label(GUI,text = 'Units', font = FONT2)
L3.pack()
E2 = ttk.Entry(GUI,textvariable = v_number1, font = FONT1,width=40)
E2.pack(pady=10)

L4 = ttk.Label(GUI,text = 'PRICE', font = FONT2)
L4.pack()
E4 = ttk.Entry(GUI,textvariable = v_number2, font = FONT1,width=40)
E4.pack(pady=10)

#DEF
def cal7():

    try:
        v_nameinv = v_inventory1.get()
        number1 = v_number1.get()
        number2 = v_number2.get()
        vat = 1.07
        print((number1 * number2)*vat)
        nameinv.set("Inventory" +' : '+v_nameinv)
        units.set("Inventory" +' : '+str(number1))
        RESULT.set("Price" +' : '+ str((number1 * number2)*vat) )

        # if promble is pass
    except:
        messagebox.showwarning('Try again','Please input the number')

    

    

#RESULT
RESULT = StringVar()
nameinv = StringVar()
units = StringVar()
B1 = ttk.Button(GUI,text='RESULT',command=cal7)
B1.pack(ipadx=20,ipady=10)

R1 = ttk.Label(GUI,textvariable = nameinv , font = FONT1 , foreground='green')
R1.pack()

R2 = ttk.Label(GUI,textvariable = units , font = FONT1 , foreground='green')
R2.pack()

R4 = ttk.Label(GUI,textvariable = RESULT , font = FONT1 , foreground='green')
R4.pack()


# LOOP FOR Run
GUI.mainloop()
