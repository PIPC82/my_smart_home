#!/usr/bin/python3

import serial
import minimalmodbus
import time

modbus1 = minimalmodbus.Instrument('/dev/ttyS2', 31)# port name, slave address
modbus2 = minimalmodbus.Instrument('/dev/ttyS2', 32)# port name, slave address



while True:
    time.sleep(0.5)

    try:
        temp1 = modbus1.read_register(1, 0, 4, True)
        hum1 = modbus1.read_register(2, 0, 4, True)
    except IOError:
        print('Error modbus1 -IOError-')
    except ValueError:
        print('Error modbus1 -ValueError-')
    except TypeError:
        print('Error modbus -TypeError-')
    
    print("==========31=============")    
    print(temp1/10)
    print(hum1/10) 
     
    time.sleep(0.5)

    try:
        temp2 = modbus2.read_register(1, 0, 4, True)
        hum2 = modbus2.read_register(2, 0, 4, True)
    except IOError:
        print('Error modbus2 -IOError-')
    except ValueError:
        print('Error modbus2 -ValueError-')
    except TypeError:
        print('Error modbus2 -TypeError-')
    print("==========32=============")    
    print(temp2/10)        
    print(hum2/10)   
