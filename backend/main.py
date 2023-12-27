from dataset import load_appointments
from availability import check_availability
from datetime import datetime
from backend.logic import book_time_slot, list_available_times, get_user_input


def main():
    # Load the dataset from the CSV file
    dataset = load_appointments("appointments.csv")

    # Get user input for the day
    appointment_date = get_user_input()

    # List available times for the selected day
    list_available_times(dataset, appointment_date)

    book_time_slot(dataset, appointment_date)


if __name__ == "__main__":
    main()
