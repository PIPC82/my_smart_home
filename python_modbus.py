#!/usr/bin/python3

import serial
import minimalmodbus
import time

modbus1 = minimalmodbus.Instrument('/dev/ttyS2', 31)# port name, slave address
modbus2 = minimalmodbus.Instrument('/dev/ttyS2', 32)# port name, slave address



while True:
    time.sleep(2)

    try:
        temp1 = modbus1.read_register(1, 0, 4, True)
        hum1 = modbus1.read_register(2, 0, 4, True)
    except IOError:
        print('Error modbus -IOError- read to adress')
    except ValueError:
        print('Error modbus -ValueError-  read to adress')
    except TypeError:
        print('Error modbus -TypeError-  read to adress')
     
    print(temp1)
    print(hum1) 
     
    time.sleep(2)

    try:
        temp2 = modbus2.read_register(1, 0, 4, True)
        hum2 = modbus2.read_register(2, 0, 4, True)
    except IOError:
        print('Error modbus -IOError- read to adress')
    except ValueError:
        print('Error modbus -ValueError-  read to adress')
    except TypeError:
        print('Error modbus -TypeError-  read to adress')
    print(temp2)        
    print(hum2)     
