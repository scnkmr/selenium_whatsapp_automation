from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
no_list=[+917053769030,+919650266943,+917053769030,+919718099823]
msg_list=["*NO DEPOSIT*|* BONUS*","Make profits and get withdrawals with $30 |No Deposit Tradable Bonus. |Minimum Withdrawal $100.","visit |www.gicmarkets.com||healakdsj "]

driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
sleep(20)

#Function for sending message
def sendmessage(phone_no,textmsg):
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

i=0;
while(i<len(no_list)):
    j=0
    while(j<len(msg_list)):
        try:
            sendmessage(no_list[i],msg_list[j])
        except Exception as e:
            sleep(10)
        i+=1
        j+=1
