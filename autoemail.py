import json

import email
import imaplib
import getpass
import sys
import re

from asn1crypto.x509 import EmailAddress
from asn1crypto._ffi import null

#Needed to send email
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

from pprint import pprint as pp

#from zope.interface.common import mapping

username = "sdsdsd@gmail.com"
password = "dsdsds"

myFile = open("conversations.json")

data = json.load(myFile)

myFile.close()

for myValues in data:
    print(myValues['title'])

for myValues in data:
    print("------------------")
    #print("myValues['mapping']")
    #print(myValues['mapping'])
    #print("------------------")

#print("------")
#print(" ")

subject = data[0]['title']

strMap = myValues['mapping']

#print(strMap.items())

#print(strMap.keys())

myCount = 0
myPayload = " "

for item in strMap.items():
    #print(strMap['message'])
    #print("--  START --------")
    #print("item[0] " + item[0])
    #print("-----END -----")

    #print("--  START --------")
    #print("item[1]")
    #print(item[1])
    #print("-----END -----")

    #print("--  START --------")
    #print("item[1]['id']")
    #print(item[1]['id'])
    #print("----  END ------")

    #print("----------")
    #print("item[1]['message']")
    #print(item[1]['message'])
    #print("----------")

    myMessage = item[1]['message']



    #print(myMessage)


    if myMessage is not null():
        #print(myMessage.keys())
        #print(myMessage.items())
        #print(myCount)
        #print("myMessage['content']['parts']")
        #print(myMessage['content']['parts'])
        #print("----------")
        #myCount = myCount + 1

        myParts = myMessage['content']['parts'].__str__()

        print(myParts)

        myLen = len(myParts)

        print(myLen)

        if ((myLen>10) and (myLen<300)):
            #This is the Question
            print("New Subject")
            newSubject = subject + " " + myParts[2:200]
            newSubject = newSubject.replace("\\t"," ")
            newSubject = newSubject.replace("']"," ")
            print(newSubject)
        elif (myLen>500):
            print("myPayload")
            #mystr = myParts.split('\t')
            #mystr = myParts.splitlines()
            myPartsBK = myParts

            print(myPartsBK)
            mystr = myPartsBK.replace("\\n"," \r\n ")
            #mystr = myPartsBK.replace("\\n"," \r\n \r\n")
            mystr = mystr.replace("\t"," ")
            mystr = mystr.replace("['"," ")
            mystr = mystr.replace("']"," ")
            mystr = mystr.replace("\\","")
            mystr = mystr.replace("Certainly, here's a","")

            #mystr = mystr.replace("\\n","%OD%OA")
            #print(mystr)

            #myLines = mystr.split('\n')

            #myLines = mystr.split('\n')

            #newMyLines=""

            #for myLine in myLines:
            #    newMyLines = newMyLines + myLine + '\n'

            #print(newMyLines)

            #myPayload=myParts

            myPayload=mystr

            #print(mystr)
            #print(myPayload)
            print("----")

            newmsg = EmailMessage()
            newmsg['subject'] = newSubject
            newmsg['From'] = 'dsdsds@gmail.com'
            newmsg['To'] = 'sdsdsdsd@gmailcom'
            #newmsg.set_content(myPayload,subtype='text')

            newmsg.set_content(myPayload,subtype='text/plain')

            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls() #enable security
            session.login('dsdsds@gmail.com','dilpqdizrhaiaaqw')
            session.send_message(newmsg)
            session.quit()

            subject=""
            myPayload=""





        #if (myMessage['content']['parts'].find(""))

        #for myMsgVal in myMessage:
            #print("--------------")
            #print("MYMESSAGE")
            #print(myMsgVal)

            #myDict = json.loads(myMsgVal)
            #print(myDict)
            #print(myMsgVal.keys())





    #for submsg in item[1]['message']:
    #    print(submsg)

    #for subitem in (item[1]):
    #    print("subitem START")
    #    print (subitem)
    #    print("subitem END")
        #for subsubitem in subitem:
        #    print(subsubitem)




#print ("data[0]['title'] = " + data[0]['title'])


#newmsg = EmailMessage()
#newmsg['subject'] = subject

#newmsg['From'] = 'sdsdsdsdsds@gmail.com'
#newmsg['To'] = 'sdfdfdsfdsfs@blogger.com'

#myPayload ="myPayload"

#print(myPayload)

#newmsg.set_content(myPayload)

#session = smtplib.SMTP('smtp.gmail.com', 587)
#session.starttls() #enable security
#session.login('sffdsfdsfdsf@gmail.com','dilpqdizrhaiaaqw')
# session.send_message(newmsg)
#session.quit()





#print(range(len(item)))



# for subitem in item.keys:
#        print (subitem)

print("------")
print(" ")




#for i in range(len(strMap)):
#    print(strMap.items[i])






#for j in range(len(item[i])):



#for item in strMap.items():
#    print(range(len(item)))

    #for i in range(len(item)):
    #    for j in range(len(item[i])):
    #        print('index: ',j, ' value:', item[i][j])


















#with open('conversations.json') as string:
#    my_dict=json.load(string)
#string.close()



#for k in my_dict:
#    print(" Key:   " + str(k) )
#    print("Value: " + k('title'))




    #print(" Value: " + str(my_dict[k]) )



#myFile = open("conversations.json")

#data = json.load(myFile)

#for myValues in data:
#    print(myValues['mapping'])

#myFile.close()

#for (k, v) in data.items():
#    print("Key: " + k)
#    print("Value: " + str(v))

#for iterator in data:
#    print(iterator, ":", data[iterator])
