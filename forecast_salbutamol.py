import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


# Prediction model that takes memory and mean reversion into account
def predict_demand(data, memory=0.5, mean_reversion=0.2, future_periods=10):
    """
    Predict future demand based on past data using memory and mean reversion.

    Parameters:
    - data: List or numpy array containing historical demand data.
    - memory: A float (0 to 1) determining how much recent data influences predictions.
    - mean_reversion: A float (0 to 1) determining how much mean reversion influences predictions.
    - future_periods: Number of future periods to predict.

    Returns:
    - List of predicted values.
    """
    if len(data) < 2:
        raise ValueError("Not enough data to make predictions.")

    long_term_avg = np.mean(data)
    predictions = [data[-1]]

    for _ in range(future_periods):
        recent_demand = predictions[-1]
        next_demand = (memory * recent_demand +
                       (1 - memory) * long_term_avg +
                       mean_reversion * (long_term_avg - recent_demand))
        predictions.append(next_demand)

    return predictions


# Function to remove outliers based on 3 standard deviations from the mean
def find_outlier_indices(data):
    if len(data) < 2:  # Ensure enough data for calculating statistics
        return []

    mean = np.mean(data)
    std_dev = np.std(data)
    lower_bound = mean - 3 * std_dev
    upper_bound = mean + 3 * std_dev

    return [i for i, x in enumerate(data) if x < lower_bound or x > upper_bound]


# Function to remove rows from a NumPy array based on a set of row indices
def remove_rows(array, rows_to_remove):
    if array.shape[0] == 0:
        raise ValueError("Cannot remove rows from an empty array.")

    valid_rows = {r for r in rows_to_remove if r < array.shape[0]}
    if not valid_rows:
        return array

    mask = np.ones(array.shape[0], dtype=bool)
    mask[list(valid_rows)] = False
    return array[mask]


# Dictionary to store total quantities aggregated per region
total_quantity_by_region = defaultdict(lambda: defaultdict(float))
month_counts_by_region = defaultdict(lambda: defaultdict(int))

# Process CSV files for months 3 to 5
months = [202403, 202404, 202405]

for month in months:
    filename = f'English Prescribing Dataset (EPD) - {month}.csv'
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            first_row = next(csv_reader)

            master_matrix = []
            count = 1
            unidentifiable_practices = []

            for row in csv_reader:
                if len(row) == 0 or len(row) < 22:  # Ensure row has the expected number of columns
                    continue

                master_matrix.append(row)
                count += 1

                if row[4] != "FALSE":
                    unidentifiable_practices.append(count - 2)

            if len(master_matrix) == 0:
                print(f"File {filename} is empty or couldn't be processed.")
                continue

            data_TQ = []
            data_Ad = []
            data_NIC = []
            data_AC = []

            for row in master_matrix:
                try:
                    data_TQ.append(float(row[1]))  # Total Quantity
                    data_Ad.append(float(row[18]))  # Adjustments
                    data_NIC.append(float(row[21]))  # NIC
                    data_AC.append(float(row[9]))  # Actual Cost
                except (ValueError, IndexError):
                    continue

            indices_of_outliers = set(unidentifiable_practices)
            indices_of_outliers.update(find_outlier_indices(data_AC))
            indices_of_outliers.update(find_outlier_indices(data_Ad))
            indices_of_outliers.update(find_outlier_indices(data_TQ))
            indices_of_outliers.update(find_outlier_indices(data_NIC))

            updated_matrix = [row for idx, row in enumerate(master_matrix) if idx not in indices_of_outliers]

            if not updated_matrix:
                print(f"All data removed after outlier processing for file {filename}.")
                continue

            nd1 = np.array(updated_matrix)
            nd2 = np.transpose(nd1)

            if nd2.size == 0:
                print(f"File {filename} resulted in an empty matrix after transpose.")
                continue

            irrelevant_rows = {0, 2, 3, 4, 5, 6, 7, 10, 12, 13, 14, 15, 16, 17, 22, 24, 25}

            valid_irrelevant_rows = {r for r in irrelevant_rows if r < nd2.shape[0]}

            nd3 = remove_rows(nd2, valid_irrelevant_rows)
            operating_matrix = np.transpose(nd3)

            print(f"Processed data for file {filename} has shape: {operating_matrix.shape}")

            region_column_index = 6  # Replace with the actual index of the region column
            TQ_column_index = 0  # Replace with the actual index of the total quantity column

            for row in operating_matrix:
                try:
                    region = row[region_column_index]
                    total_quantity = float(row[TQ_column_index])

                    # Accumulate total quantity for each region
                    total_quantity_by_region[region][month] += total_quantity
                    month_counts_by_region[region][month] += 1

                except (ValueError, IndexError):
                    continue

    except FileNotFoundError:
        print(f"File {filename} not found. Skipping.")

# Compute total quantities per region for all months
aggregated_data = defaultdict(list)

for region, months_data in total_quantity_by_region.items():
    total_quantities = [months_data[month] for month in sorted(months_data.keys())]
    aggregated_data[region] = total_quantities

print("\n10-Month Future Predictions Per Region:")
for region, quantities in aggregated_data.items():
    if len(quantities) >= 2:
        # Predict future demand using the memory and mean reversion model
        predicted_usage = predict_demand(list(quantities), memory=0.7, mean_reversion=0.3, future_periods=10)
        print(f"Predicted Future Usage for Region {region}: {predicted_usage[1:]}")

        # Optionally plot the results
        months = list(range(1, len(quantities) + 1))
        future_months = list(range(len(quantities) + 1, len(quantities) + 1 + len(predicted_usage) - 1))

        plt.figure(figsize=(12, 6))
        plt.plot(months, quantities, label="Historical Demand", marker='o')
        plt.plot(future_months, predicted_usage[1:], label="Predicted Demand", marker='x', linestyle='--')
        plt.xlabel("Month")
        plt.ylabel("Demand")
        plt.title(f"Total Quantity Demand Prediction for Region {region}")
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print(f"Insufficient data to calculate predictions for region {region}.")
