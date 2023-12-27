import pandas as pd

def load_appointments(filename):
    # Load the dataset from a CSV file
    dataset = pd.read_csv(filename)
    # Convert the 'datetime' column to a datetime object
    dataset['datetime'] = pd.to_datetime(dataset['datetime'])
    return dataset


# Example usage
if __name__ == "__main__":
    dataset = load_appointments("appointments.csv")
    print(dataset.head())
