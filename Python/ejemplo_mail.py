#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 21/01/2015

@author: ecrespo
@version: 1.0
@description: ejemplo de envío de correos desde servidor con SMTP propio

'''

# Import smtplib for the actual sending function
import smtplib
from email.MIMEText import MIMEText

msg = MIMEText("Mensaje de prueba desde Python...\r\n" 
"Probando para futuras aplicaciones.")
fromaddr = "info@aprendiendoarduino.com"
toaddr = "aprendiendoarduino@gmail.com"
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mensaje de prueba desde Python."

print(msg)

s = smtplib.SMTP('localhost')
#Next, log in to the server
#s.login("youremailusername", "password")
s.sendmail(fromaddr, toaddr, msg.as_string())
s.quit()