# -*- coding: utf-8 -*-

'''
Created on 30/07/2015

@author: ecrespo
@version: 1.0
@description: grabar a fichero los datos leidos por un puerto serie

'''

# Para comunicarnos con nuestra placa Arduino por puerto serie utilizaremos la biblioteca pySerial
# http://pyserial.sourceforge.net/
import time

try:
    import serial
    arduino = serial.Serial('COM6', baudrate=115200, timeout=1.0)

    # Nota: provocamos un reseteo manual de la placa para leer desde
    # el principio, ver http://stackoverflow.com/a/21082531/554319
    arduino.setDTR(False)
    time.sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)
    print("Comienzo...")

except (ImportError, serial.SerialException):
    # No hay módulo serial o placa Arduino disponibles
    import io

    class FakeArduino(io.RawIOBase):
        """Clase para representar un "falso Arduino"
        """
        def readline(self):
            time.sleep(0.1)
            return b'No hay conexion con Arduino'
	
    arduino = FakeArduino()

f = open("log.txt","a")
f.write('\r\n--------------------\r\n')
	
# Con la sentencia with el arduino se cierra automáticamente, ver
# http://docs.python.org/3/reference/datamodel.html#context-managers
with arduino:
    while True:
        try:
            # En Python 3 esta función devuelve un objeto bytes, ver
            # http://docs.python.org/3/library/stdtypes.html#typebytes
            line = arduino.readline()
            s = line.decode('ascii', errors='replace')
            if not(s.find("Type")):
                f.write(time.strftime('%d-%m-%y,%H:%M:%S')+'\r\n')
                print(time.strftime('%d-%m-%y,%H:%M:%S'))
            f.write(line.decode('ascii', errors='replace'))
            # Con errors='replace' se evitan problemas con bytes erróneos, ver
            # http://docs.python.org/3/library/stdtypes.html#bytes.decode
            # Con end='' se evita un doble salto de línea
            print(line.decode('ascii', errors='replace'), end='')
        except KeyboardInterrupt:
            print("Error el lectura de Arduino")
    f.close()
