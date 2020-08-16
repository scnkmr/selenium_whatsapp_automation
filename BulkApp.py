from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import filedialog
import csv

no_list=[]
msg_list=[]

def lod():
    driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    sleep(20)

#Function for sending message
def sendmessage(phone_no,textmsg,driver):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    sleep(10)
    try:
        txt_box=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]")
        splited_msg=textmsg.split("|")
        for x in splited_msg:
            txt_box.send_keys(x)
            txt_box.send_keys(Keys.SHIFT,Keys.ENTER)
        #txt_box.send_keys(textmsg+Keys.SHIFT,Keys.ENTER,Keys.ENTER)
        txt_box.send_keys("\n")

        sleep(2)
    except Exception as e:
        print("Invalid no"+str(phone_no))

def lodsend():
    driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    sleep(20)
    i=0;
    while(i<len(no_list)):
        j=0
        while(j<len(msg_list)):
            try:
                sendmessage(no_list[i],msg_list[j],driver)
            except Exception as e:
                sleep(10)
                print(e)
            i+=1
            j+=1
#lodsend()


window=Tk()
window.title("Whatsapp NO list and message")


#select no button
def noCsv():
    nname= filedialog.askopenfilename(title="SELECT CSV FILE OF PHONE NUMBER")
    with open(nname, 'r') as f:
        reader = csv.reader(f)
        n_list = list(reader)
        n_list=sum(n_list,[])
        global no_list
        no_list=list(map(int,n_list))
    print(no_list)


Button(text='Select Phone No', command=noCsv).pack(fill=X)

#select msg button
def msgCsv():
    msgname= filedialog.askopenfilename(title="SELECT CSV FILE OF MESSAGES")
    with open(msgname, 'r') as f:
        reader = csv.reader(f)
        m_list = list(reader)
        global msg_list
        msg_list=sum(m_list,[])
    print(msg_list)


Button(text='Select Messages', command=msgCsv).pack(fill=X)


#send message button
Button(text="Send",command=lodsend).pack()

window.mainloop()
