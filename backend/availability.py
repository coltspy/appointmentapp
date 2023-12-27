import pandas as pd
from datetime import datetime

def check_availability(dataset, requested_datetime):
    # Check if the requested datetime is in the dataset
    matching_slots = dataset[dataset['datetime'] == requested_datetime]

    # If the slot is in the dataset and marked as unavailable, return False
    if not matching_slots.empty and not matching_slots.iloc[0]['Available']:
        return False

    # If the slot is not in the dataset, it's considered available
    return True



# Example usage (You can remove this before integrating with the main app)
if __name__ == "__main__":
    # Assuming dataset is imported or defined here
    dataset = pd.DataFrame()  # Define the dataset variable
    user_requested_datetime = datetime(2023, 12, 26, 10, 0, 0)  # Example date and time
    is_available = check_availability(dataset, user_requested_datetime)
    print(f"Is the slot on {user_requested_datetime} available? {is_available}")
