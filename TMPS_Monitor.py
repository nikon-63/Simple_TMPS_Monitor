import json
import fileinput
import socket


# IP address of RPI running homebridge
homeBridge_IP = '192.168.0.33'

# Wheel ID's
Driver_F = "<Enter ID>"
Driver_B = "<Enter ID>"
Passenger_F = "<Enter ID>"
Passenger_B = "<Enter ID>"

# Function to send to homebridge
def sendHB(PSI, port):
    PSI = str(PSI)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(PSI.encode(), (homeBridge_IP, port))
    sock.close()


for line in fileinput.input():
    try:
        data = json.loads(line)
        try:
            if data['id'] == Driver_F:
                PSI = data['pressure_PSI']
                PSI = round(PSI)
                print("Driver_F wheel presser: ", str(PSI))
                sendHB(PSI, 8266)
            elif data['id'] == Driver_B:
                PSI = data['pressure_PSI']
                PSI = round(PSI)
                print("Driver_B wheel presser: ", str(PSI))
                sendHB(PSI, 8267)
            elif data['id'] == Passenger_F:
                PSI = data['pressure_PSI']
                PSI = round(PSI)
                print("Passenger_F wheel presser: ", str(PSI))
                sendHB(PSI, 8268)
            elif data['id'] == Passenger_B:
                PSI = data['pressure_PSI']
                PSI = round(PSI)
                print("Passenger_B wheel presser: ", str(PSI))
                sendHB(PSI, 8269)
            else:
                pass
        except Exception as e: 
            print(e)
    except:
        pass
