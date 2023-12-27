from dataset import load_appointments
from availability import check_availability
from datetime import datetime



def book_time_slot(dataset, appointment_date, time_slot_index):
    available_times = dataset[(dataset['datetime'].dt.date == appointment_date.date()) & (dataset['Available'] == True)]
    
    if available_times.empty:
        return {"success": False, "message": "No available times to book for this date."}

    if 0 <= time_slot_index < len(available_times):
        selected_datetime = available_times.iloc[time_slot_index]['datetime']
        dataset.loc[dataset['datetime'] == selected_datetime, 'Available'] = False
        dataset.to_csv("appointments.csv", index=False)
        return {"success": True, "booked_time": selected_datetime.strftime('%Y-%m-%d %H:%M')}
    else:
        return {"success": False, "message": "Invalid time slot selection."}



def list_available_times(dataset, appointment_date):
    available_times = dataset[(dataset['datetime'].dt.date == appointment_date.date()) & (dataset['Available'] == True)]
    
    if not available_times.empty:
        times_list = available_times['datetime'].dt.strftime('%Y-%m-%d %H:%M').tolist()
        return {"success": True, "available_times": times_list}
    else:
        return {"success": False, "message": "No available times for this date."}
