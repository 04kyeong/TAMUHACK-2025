from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import csv
import threading

# Set up for Flask and socket
app = Flask(__name__, template_folder="C:\\Users\\ham05\\OneDrive\\바탕 화면\\TAMUHACK 2025\\templates")
socketio = SocketIO(app)

# CSV address
csv_file = "C:\\Users\\ham05\\OneDrive\\바탕 화면\\TAMUHACK 2025\\trash_data.csv"

# CSV read
def read_csv():
    data = []
    try:
        print(f"Attempting to read CSV at: {csv_file}")
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                try:
                    # Remove 'seconds' and convert to float
                    time_to_fill = float(row[1].replace('seconds', '').strip())
                    data.append({'timestamp': row[0], 'time_to_fill': time_to_fill})
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
@app.route('/data')
def data():
    csv_data = read_csv()
    recent_5 = csv_data[-5:] if len(csv_data) >= 5 else csv_data  # Most recent 5 records
    return jsonify({
        'top5': recent_5,  # Last 5 entries for the table
        'graph_data': recent_5  # Last 5 entries for the chart
    })

# Background thread to simulate real-time updates
def update_data():
    while True:
        socketio.sleep(5)  # update every 5 secs
        csv_data = read_csv()
        recent_record = csv_data[-1] if csv_data else None
        if recent_record:
            print(f"Broadcasting new data: {recent_record}")
            socketio.emit('new_data', recent_record)

# Background thread to handle real-time updates
threading.Thread(target=update_data, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
