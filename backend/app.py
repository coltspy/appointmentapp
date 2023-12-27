from flask import Flask, request, jsonify
from backend.dataset import load_appointments
from backend.logic import list_available_times, book_time_slot
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/available_times', methods=['GET'])
def available_times_route():
    date_str = request.args.get('date')
    try:
        appointment_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({"success": False, "message": "Invalid date format."}), 400

    dataset = load_appointments("appointments.csv")
    result = list_available_times(dataset, appointment_date)
    return jsonify(result)


@app.route('/book_appointment', methods=['POST'])
def book_appointment_route():
    data = request.json
    try:
        appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d')
        time_slot_index = int(data['time_slot_index'])

        dataset = load_appointments("appointments.csv")
        result = book_time_slot(dataset, appointment_date, time_slot_index)

        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})



if __name__ == '__main__':
    app.run(debug=True)
