import serial

ser = serial.Serial("COM5", 115200, timeout=1)
def sendSerial(txtString):

    ser.write(f"{txtString}\n".encode("utf-8"))
    ser.close()