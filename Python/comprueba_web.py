#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, urllib2
import smtplib
import time
from email.MIMEText import MIMEText

fromaddr = "alarma@aprendiendoarduino.com"
toaddr = ['aprendiendoarduino@gmail.com','info@aprendiendoarduino.com']
toaddr2 = "aprendiendoarduino@gmail.com"

msg1 = MIMEText("Aviso de temperatura baja por debajo de 6 grados")
msg1['From'] = fromaddr
msg1['To'] = ", ".join(toaddr)
msg1['Subject'] = "Temperatura menor de 6 grados"

msg2 = MIMEText("Proceder a arrancar anticongelación")
msg2['From'] = fromaddr
msg2['To'] = ", ".join(toaddr)
msg2['Subject'] = "Aviso de temperatura baja por debajo de 5 grados"

msg3 = MIMEText("Problemas con acceso a web")
msg3['From'] = fromaddr
msg3['To'] = toaddr2
msg3['Subject'] = "Ver que pasa..."

s = smtplib.SMTP('localhost')
 
def gethtml(url):
    try:
       req = urllib2.Request(url)
       return urllib2.urlopen(req).read()
    except:
        time.sleep(2)
        s.sendmail(fromaddr, toaddr2, msg3.as_string())
        return ''

url = 'localhost'
web = gethtml(url)
inicio = web.find("Temperatura")
temperatura=web[22:27]

try:
    float(temperatura)
except:
    s.sendmail(fromaddr, toaddr2, msg3.as_string())

if float(temperatura) > 6:
   print(time.strftime("%Y/%m/%d %H:%M:%S")+" Todo OK")
elif float(temperatura) < 6 and float(temperatura) > 5:
   print(time.strftime("%Y/%m/%d %H:%M:%S")," Aviso")
   s.sendmail(fromaddr, toaddr, msg1.as_string())
else:
   print(time.strftime("%Y/%m/%d %H:%M:%S")+" Arranca anticongelación")
   s.sendmail(fromaddr, toaddr, msg2.as_string())
print temperatura
