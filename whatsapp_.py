import pywhatkit
import time
phone_num=0
def check_contact(contact):
    contact_list=['contact','contact','Sally']
    if contact in contact_list:
      return True        
def phone_contacts(contact):
    global phone_num
    if(contact=='Sally'):
         phone_num="Your number"
    return phone_num     
     
def Whatsapp_open(message_,contact):
    pywhatkit.sendwhatmsg_instantly(phone_contacts(contact),message_)
    ##time_hour=1,
    ##time_min=30
    time.sleep(4)
#Whatsapp_open()    
#print(check_contact("me"))
#t=check_contact("me")
#if t==True:
 #  print("me")
 #
 # Whatsapp_open("my voice","me")