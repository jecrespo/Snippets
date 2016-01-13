# -*- coding: utf-8 -*-

'''
Created on 21/01/2015

@author: ecrespo
@version: 1.0
@description: ejemplo de envio de correos desde servidor con SMTP propio

'''

# Import smtplib for the actual sending function
import smtplib
import os
from email.mime.text import MIMEText

hostname = "10.1.1.2" #example
response = os.system("ping -n 2 -w 10 " + hostname)
print (response)
if response == 0:
  print (hostname + ' is up!')
else:
  print (hostname, ' is down!')

msg = MIMEText("Mensaje de prueba desde Python con Windows...\r\n" 
"Probando para futuras aplicaciones.")
fromaddr = "info@aprendiendoarduino.com"
toaddr = "aprendiendoarduino@gmail.com"
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mensaje de prueba desde Python."

print(msg)

s = smtplib.SMTP('smtp server IP')
#Next, log in to the server
s.sendmail(fromaddr, toaddr, msg.as_string())
s.quit()