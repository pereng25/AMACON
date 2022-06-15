import time
import telnetlib

HOST = "141.75.28.108"
PORT = "7700"


def main():

    telnetObj = telnetlib.Telnet(HOST,PORT)
    message = ("> AKON K0 <").encode('ascii')
    telnetObj.write(message)
    time.sleep(0.05)
    output=telnetObj.read_eager()
    print(output)
    telnetObj.close()


if __name__ == '__main__':
    main()


