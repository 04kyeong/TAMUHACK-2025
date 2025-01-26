import serial
import csv
import time

# Arduino connect
def connect_to_arduino(port, baudrate):
    try:
        arduino = serial.Serial(port, baudrate)
        time.sleep(2)  # Arduino set up time
        print(f"Connected to Arduino on {port}")
        return arduino
    except serial.SerialException as e:
        print(f"Error connecting to Arduino: {e}")
        return None

# Arduino connect try
arduino = connect_to_arduino('COM3', 9600)  

if not arduino:
    print("Failed to connect to Arduino. Exiting program.")
    exit()  # quit when failed to connect

# CSV address
csv_file = 'trash_data.csv'

# no file, write header
def initialize_csv(file_path):
    try:
        with open(file_path, 'r') as file:  
            pass  
    except FileNotFoundError:
        with open(file_path, 'w', newline='') as file:  # create file
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'time_to_fill'])  # add header
            print(f"Initialized CSV with headers at {file_path}")


# CSV  initialize
initialize_csv(csv_file)

# loop for data
while True:
    try:
        # Arduino data reading
        data = arduino.readline().decode('utf-8').strip()
        print(f"Received: {data}")

        # record when the trashbag got replaced
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # time of rn

        # add data to csv
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            # Extract numeric part of the "time_to_fill" if it contains 'seconds'
            numeric_data = data.replace('seconds', '').strip()  # remove "seconds" 
            writer.writerow([timestamp, numeric_data])

            print(f"Logged: {timestamp}, {numeric_data}")  # debudding
    except Exception as e:
        print(f"Error: {e}")
