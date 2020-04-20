import serial
ardserialdata= serial.Serial('COM3', 9600)
while True:
    if ardserialdata.inWaiting()>0:
     SerialData=ardserialdata.readline().decode('ASCII')
     print(SerialData)




