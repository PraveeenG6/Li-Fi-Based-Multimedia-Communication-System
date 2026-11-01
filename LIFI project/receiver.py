#RECIEVING PYTH
import serial
import base64
from io import BytesIO
from PIL import Image
import time
print("\t \t LIGHT FEDILITY COMMUNICATION -> RECIEVER\n ")
while True:
    x=int(input("enter the mode of operation\n 1-> text\n 2->image \n 3->audio\n"))
    if x == 1 or x == 2 or x == 3:
        break
    print("invalid try again\n\n")
data_str = ""
ser = serial.Serial('COM11', 115200, timeout=20)  # COM11 = Arduino RX port
time.sleep(2)
print("Listening for Base64 data...")
last_data_time=time.time()
while True:
    if ser.in_waiting > 0:
        ch = ser.read().decode('ascii', errors='ignore')
        if ch=='#':
            break
        data_str += ch
        print(ch, end="")
        last_data_time = time.time()
    elif time.time() - last_data_time > 60:  # 5s no data
        print("\nNo data for 60 seconds, stopping.")
        break
ser.close()
data_str = data_str.strip()
print("\n\n Data received successfully.")
print(f"Length: {len(data_str)} chars")
try:
    if x==2:
        img_bytes = base64.b64decode(data_str)
        img = Image.open(BytesIO(img_bytes))
        img.show()
        print("image is reconstructed")
        #if u want to save the image file
        #img.save("received.jpg")  
        #print(" Image reconstructed and saved as 'received.jpg'")
    elif x==3:
        audio_bytes=base64.b64decode(data_str)
        output_file = "received1.opus"   # or received.mp3 / received.wav
        with open(output_file, "wb") as f:
            f.write(audio_bytes)
        print("audio is reconstructed and saved as recieved.opus")
    elif x==1:
        print("text data")
        print(data_str)
        print(' text recieved')
except Exception as e:
    print(" Error decoding image:", e)