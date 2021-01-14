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
v_product = StringVar()
v_price = StringVar()
v_quantity = StringVar()

L2 = ttk.Label(GUI,text = 'Name inventory', font = FONT2)
L2.pack()
E1 = ttk.Entry(GUI,textvariable = v_product, font = FONT1,width=40)
E1.pack(pady=10)

L3 = ttk.Label(GUI,text = 'Units', font = FONT2)
L3.pack()
E2 = ttk.Entry(GUI,textvariable = v_price, font = FONT1,width=40)
E2.pack(pady=10)

L4 = ttk.Label(GUI,text = 'PRICE', font = FONT2)
L4.pack()
E4 = ttk.Entry(GUI,textvariable = v_quantity, font = FONT1,width=40)
E4.pack(pady=10)


# ฤRaio เลือกประเภท VAT

F1 = Frame(GUI)
F1.pack(pady=10)
myColor = '#40E0D0'
GUI.configure(bg=myColor)   
s = ttk.Style()                     
s.configure('Wild.TRadiobutton',background=myColor,foreground='black',font=FONT1)         


### ข้างบนคือการแก้ font


v_radio = StringVar()

R1 = ttk.Radiobutton(F1,text='ราคารวม vat แล้ว', style = 'Wild.TRadiobutton', variable=v_radio,value='ic')
R1.grid(row=0,column=0)

R1.invoke() ## default

R2 = ttk.Radiobutton(F1,text='ราคารวม + vat 7', style = 'Wild.TRadiobutton', variable=v_radio,value='av')
R2.grid(row=0,column=1)

R3 = ttk.Radiobutton(F1,text='ราคาไม่รวม vat', style = 'Wild.TRadiobutton', variable=v_radio,value='nic')
R3.grid(row=0,column=2)






#DEF
def cal7(event=None): 
# event มาจาก bind <Return> ถเาไม่ใส่ agru event จะ Enter Error 
# event=None กรณี ใช้ปุ้มด้วยต้องใส่ =None
    print(v_radio.get())
    product = v_product.get()
    price = int(v_price.get())
    quantity = int(v_quantity.get())
    total = price * quantity
    try:


        if v_radio.get() == 'ic':   
            vat7 = total * (7/107)
            nettotal = total * (100/107)
            #print('ราคาก่อน vat: {:.2f} (vat 7%: {:.2f})'.format(nettotal,vat7))
            v_result.set('สินค้า: {} จำนวน {} ชิ้น ทั้งหมด {} บาท ({} บาท/ชิ้น)\nราคาสินค้า: {:.2f}.- VAT7%: {:.2f}.-'.format(product,
                                                                                                    quantity,total,
                                                                                                    price,
                                                                                                    nettotal,vat7))
        elif v_radio.get() == 'av':
            vat7 = (total * (7/100))
            nettotal = total
            sumtotal = total + vat7
            v_result.set('สินค้า: {} จำนวน {} ชิ้น ทั้งหมด {:.2f} บาท ({:.2f} บาท/ชิ้น)\nราคาสินค้า: {:.2f}.- VAT7%: {:.2f}.-'.format(product,
                                                                                                    quantity,sumtotal,
                                                                                                    price + (vat7 / quantity),
                                                                                                    nettotal,vat7))
        else:
            v_result.set('สินค้า: {} จำนวน {} ชิ้น ทั้งหมด {:.2f} บาท ({:.2f} บาท/ชิ้น)\n'.format(product,quantity,total,price))
            # if promble is pass
    except:
        messagebox.showwarning('Try again','Please input the number')

E4.bind('<Return>',cal7)   # ในช่อง PRICE มีการกด enter จะสั้งใช่ DEF "Return ต้อง R ใหญ่"

    

#RESULT

v_result = StringVar()
B1 = ttk.Button(GUI,text='RESULT',command=cal7)
B1.pack(ipadx=20,ipady=10)

Z1 = ttk.Label(GUI,textvariable=v_result,font=FONT1)
Z1.pack()

# LOOP FOR Run
GUI.mainloop()
