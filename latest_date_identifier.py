from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_latest_dates(names, values):
    """Function to get the latest date per month while keeping values aligned."""
    if not names or not values or len(names) != len(values):
        logger.warning("Invalid names or values provided for filtering.")
        return names, values  # Return original data if invalid

    try:
        # Convert date strings to datetime objects
        date_value_pairs = [(datetime.strptime(date, "%Y-%m-%d"), value) for date, value in zip(names, values)]
        # Sort by date (ascending)
        date_value_pairs.sort()
        # Dictionary to store the latest date for each (year, month)
        latest_dates = {}
        for date, value in date_value_pairs:
            key = (date.year, date.month)
            latest_dates[key] = (date, value)  # Keep latest date
        # Extract filtered names and values
        filtered_names = [date.strftime("%Y-%m-%d") for date, _ in latest_dates.values()]
        filtered_values = [value for _, value in latest_dates.values()]
        return filtered_names, filtered_values

    except Exception as e:
        logger.error(f"Error in get_latest_dates: {e}", exc_info=True)
        return names, values  # Return original data to avoid breaking flow


# Example Input
names_input = ["2024-08-21", "2025-01-03", "2024-10-09", "2024-10-14", "2024-10-25", "2025-01-10"]
values_input = [98, 15, 26, 24, 18, 45]

# Get filtered latest dates and values
filtered_names_output, filtered_values_output = get_latest_dates(names=names_input, values=values_input)

# Output Results
print("Filtered Names:", filtered_names_output)
print("Filtered Values:", filtered_values_output)
