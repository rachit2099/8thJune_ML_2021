import tkinter as t

app=t.Tk()
app.title("Basic calculator")
app.geometry('300x300')

val=t.Variable(app)
t.Entry(app,textvariable=val,justify='right',width=30).place(x=50,y=50)

exp=""

def operate(e):
    global exp
    exp= exp + str(e)
    val.set(exp)

def clr(x):
    global exp
    exp=""
    val.set("")
    
def equal(n):
    global exp
    r=str(eval(exp))
    val.set(r)
    exp=""

    
t.Button(app,text='clr',width=2,command=lambda:clr('clr')).place(x=50,y=10)
t.Button(app,text='7',width=2,command=lambda:operate('7')).place(x=50,y=80)
t.Button(app,text='4',width=2,command=lambda:operate('4')).place(x=50,y=120)
t.Button(app,text='1',width=2,command=lambda:operate('1')).place(x=50,y=160)
t.Button(app,text='.',width=2,command=lambda:operate('.')).place(x=50,y=200)
t.Button(app,text='8',width=2,command=lambda:operate('8')).place(x=100,y=80)
t.Button(app,text='5',width=2,command=lambda:operate('5')).place(x=100,y=120)
t.Button(app,text='2',width=2,command=lambda:operate('2')).place(x=100,y=160)
t.Button(app,text='0',width=2,command=lambda:operate('0')).place(x=100,y=200)
t.Button(app,text='9',width=2,command=lambda:operate('9')).place(x=150,y=80)
t.Button(app,text='6',width=2,command=lambda:operate('6')).place(x=150,y=120)
t.Button(app,text='3',width=2,command=lambda:operate('3')).place(x=150,y=160)
t.Button(app,text='=',width=2,command=lambda:equal('=')).place(x=150,y=200)
t.Button(app,text='+',width=2,command=lambda:operate('+')).place(x=200,y=80)
t.Button(app,text='-',width=2,command=lambda:operate('-')).place(x=200,y=120)
t.Button(app,text='*',width=2,command=lambda:operate('*')).place(x=200,y=160)
t.Button(app,text='/',width=2,command=lambda:operate('/')).place(x=200,y=200)


app.mainloop()
