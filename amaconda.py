import serial
import time

serialPort = serial.Serial(port="COM5", baudrate=9600, bytesize=7, stopbits=serial.STOPBITS_ONE, xonxoff=True, parity=serial.PARITY_EVEN, timeout=2500)
serialPort.write(b"> ASTZ KV <")

def main():
    
    recieve = b""
    
    while recieve == b"":
        time.sleep(2)
        incoming = serialPort.inWaiting()
        recieve = serialPort.read(incoming)
        print(recieve)

    serialPort.close()

    #print(recieve.decode("ascii"))


if __name__ == '__main__':
    main()