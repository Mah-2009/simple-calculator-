import tkinter as tk

calculation=""

def add_to(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_to():
    global calculation
    try:
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)

    except:
        clear_all()
        text_result.insert(1.0,"Error")
        

def clear_all():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("300x275")

text_result=tk.Text(root,height=2, width=16,font=('Arial',24))
text_result.grid(columnspan=5)


bt1=tk.Button(root , text=1 ,command=lambda:add_to(1),width=5,font=("Arial",14))
bt1.grid(row=4 ,column=1)

bt2=tk.Button(root , text=2 ,command=lambda:add_to(2),width=5,font=("Arial",14))
bt2.grid(row=4 ,column=2)

bt3=tk.Button(root , text=3 ,command=lambda:add_to(3),width=5,font=("Arial",14))
bt3.grid(row=4 ,column=3)

bt4=tk.Button(root , text=4 ,command=lambda:add_to(4),width=5,font=("Arial",14))
bt4.grid(row=3 ,column=1)

bt5=tk.Button(root , text=5 ,command=lambda:add_to(5),width=5,font=("Arial",14))
bt5.grid(row=3 ,column=2)

bt6=tk.Button(root , text=6 ,command=lambda:add_to(6),width=5,font=("Arial",14))
bt6.grid(row=3,column=3)

bt7=tk.Button(root , text=7 ,command=lambda:add_to(7),width=5,font=("Arial",14))
bt7.grid(row=2 ,column=1)

bt8=tk.Button(root , text=8 ,command=lambda:add_to(8),width=5,font=("Arial",14))
bt8.grid(row=2 ,column=2)

bt9=tk.Button(root , text=9 ,command=lambda:add_to(9),width=5,font=("Arial",14))
bt9.grid(row=2 ,column=3)

btnmin=tk.Button(root , text="+" ,command=lambda:add_to("+"),width=5,font=("Arial",14))
btnmin.grid(row=4,column=4)

btnmul=tk.Button(root , text="-" ,command=lambda:add_to("-"),width=5,font=("Arial",14))
btnmul.grid(row=3,column=4)

btndiv=tk.Button(root , text="*" ,command=lambda:add_to("*"),width=5,font=("Arial",14))
btndiv.grid(row=2,column=4)


btnrq=tk.Button(root , text="C" ,command=clear_all,width=5,font=("Arial",14))
btnrq.grid(row=1,column=1)

btnlq = tk.Button(root, text="+/-", command=lambda: add_to("-" if not calculation.startswith("-") else ""), width=5, font=("Arial", 14))
btnlq.grid(row=1,column=2)

btnlq=tk.Button(root , text="%" ,command=lambda:add_to("%"),width=5,font=("Arial",14))
btnlq.grid(row=1,column=3)

btnlq=tk.Button(root , text="/" ,command=lambda:add_to("/"),width=5,font=("Arial",14))
btnlq.grid(row=1,column=4)

btn0=tk.Button(root , text="0" ,command=lambda:add_to("0"),width=11,font=("Arial",14))
btn0.grid(row=5,column=1,columnspan=2)

btneq=tk.Button(root , text="=" ,command=evaluate_to,width=5,font=("Arial",14))
btneq.grid(row=5,column=4)

btndot=tk.Button(root , text="." ,command=lambda:add_to("."),width=5,font=("Arial",14))
btndot.grid(row=5,column=3)

root.mainloop()