from tkinter import*
root=Tk()
root.title("CALUCULATOR")
txt_box=Entry(root,width=40,borderwidth=5)
txt_box.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def on_click(num):
    if num!='clear'and num!='=':
        txt_box.insert(END,num)
    elif num=='=':
        input_user=txt_box.get()
        txt_box.delete("0",END)
        x=""
        op=['-','+','*','/','%']
        for i in range(len(input_user)):
            if input_user[i] in op:
                break
            x+=input_user[i]
        x=int(x)
        ope=input_user[i]
        y=""
        for j in range(i+1,len(input_user)):
            if input_user[j] in op:
                break
            y+=input_user[j]
        y=int(y)
        if ope=='+':
            txt_box.insert(END,x+y)
            print(x+y)
        elif ope=='-':
            txt_box.insert(END,x-y)
        elif ope=='*':
            txt_box.insert(END,x*y)
        elif ope=='/':
            txt_box.insert(END,x/y)
        elif ope=='%':
            txt_box.insert(END,x%y)
    else:
        txt_box.delete("0",END)


b_1=Button(root,text="1",padx=40,pady=20,command=lambda: on_click(1))
b_2=Button(root,text="2",padx=40,pady=20,command=lambda: on_click(2))
b_3=Button(root,text="3",padx=40,pady=20,command=lambda: on_click(3))
b_4=Button(root,text="4",padx=40,pady=20,command=lambda: on_click(4))
b_5=Button(root,text="5",padx=40,pady=20,command=lambda: on_click(5))
b_6=Button(root,text="6",padx=40,pady=20,command=lambda: on_click(6))
b_7=Button(root,text="7",padx=40,pady=20,command=lambda: on_click(7))
b_8=Button(root,text="8",padx=40,pady=20,command=lambda: on_click(8))
b_9=Button(root,text="9",padx=40,pady=20,command=lambda: on_click(9))
b_0=Button(root,text="0",padx=40,pady=20,command=lambda: on_click(0))
b_a=Button(root,text="+",padx=40,pady=20,command=lambda: on_click('+'))
b_s=Button(root,text="-",padx=40,pady=20,command=lambda: on_click('-'))
b_m=Button(root,text="x",padx=40,pady=20,command=lambda: on_click('*'))
b_d=Button(root,text="/",padx=40,pady=20,command=lambda: on_click('/'))
b_module=Button(root,text='%',padx=40,pady=20,command=lambda:on_click('%'))
b_clear=Button(root,text='clear',padx=95,pady=20,command=lambda:on_click('clear'))
b_equal=Button(root,text='=',padx=40,pady=20,command=lambda:on_click('='))

b_1.grid(row=1,column=0)
b_2.grid(row=1,column=1)
b_3.grid(row=1,column=2)

b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)

b_7.grid(row=3,column=0)
b_8.grid(row=3,column=1)
b_9.grid(row=3,column=2)

b_0.grid(row=4,column=0)
b_a.grid(row=4,column=1)
b_s.grid(row=4,column=2)

b_m.grid(row=5,column=0)
b_d.grid(row=5,column=1)
b_module.grid(row=5,column=2)

b_clear.grid(row=6,column=0,columnspan=2)
b_equal.grid(row=6,column=2)

root.mainloop()