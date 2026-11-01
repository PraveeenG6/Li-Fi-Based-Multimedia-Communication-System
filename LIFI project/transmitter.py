#TRASMITTING PATH
import serial
import time
import base64
base64_data=""
print("\t \t LIGHT FEDILITY COMMUNICATION -> TRANSMITTER\n ")
while True:
    x=int(input("enter the mode of operation \n 1-> image \n 2-> audio \n 3-> text\n"))
    if x==1:
        print("Sending image data")
        with open(r"D:\praveen2\Downloads\image4.jpg", "rb") as img_file:
            base64_data = base64.b64encode(img_file.read()).decode('utf-8')
        break
    elif x==2:
        print("Sending audio data")
        file_path = r"D:\praveen2\Downloads\audio.opus" 
        with open(file_path, "rb") as f:
            base64_data = base64.b64encode(f.read()).decode('utf-8')
        break
    elif x==3:
        print("Sending Text data")
        base64_data=input("enter the text: ")
        break
    else:
        print("invalid try again\n\n")
# Optional: add an end marker (space)
base64_data += '#'
ser = serial.Serial('COM9', 115200, timeout=1) #arduino TX port
time.sleep(2)  # wait for Arduino to reset
# Send data
for ch in base64_data:
    ser.write(ch.encode('utf-8'))
    #time.sleep(0.001)  # small delay between bytes to avoid overflow
print(" Data sent successfully!")
ser.close()