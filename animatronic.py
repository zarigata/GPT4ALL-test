import serial 

arduino = serial.Serial('/dev/ttyACM0', 9600) #Replace '/dev/ttyACM0' with your Arduino port and '9600' with your baudrate
code_A = "YOUR_CODE_HERE" # Replace this with your actual code

while True:
  arduino.write(code_A.encode()) 