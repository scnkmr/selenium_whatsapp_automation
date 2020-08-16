from tkinter import *
from tkinter import filedialog
import csv

window=Tk()
window.title("Whatsapp NO list and message")


#select no button
def noCsv():
    nname= filedialog.askopenfilename(title="SELECT CSV FILE OF PHONE NUMBER")
    with open(nname, 'r') as f:
        reader = csv.reader(f)
        n_list = list(reader)
        n_list=sum(n_list,[])
        n_list=list(map(int,n_list))
    print(n_list)


Button(text='Select Phone No', command=noCsv).pack(fill=X)

#select msg button
def msgCsv():
    msgname= filedialog.askopenfilename(title="SELECT CSV FILE OF MESSAGES")
    with open(msgname, 'r') as f:
        reader = csv.reader(f)
        m_list = list(reader)
        m_list=sum(m_list,[])
    print(m_list)


Button(text='Select Messages', command=msgCsv).pack(fill=X)


#send message button
def callback():
    print(txt.get("1.0",END))
txt=Text(window,width=50)
txt.pack()
Button(text="Send",command=callback).pack()

window.mainloop()
