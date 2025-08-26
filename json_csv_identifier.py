import json
import csv


def identify_data_format(data):
    try:
        json.loads(data)
        return 'json'
    except ValueError:
        try:
            csv.reader([data])  # Try to parse as CSV
            return 'csv'
        except csv.Error:
            return 'unknown'


# Example usage:
json_data = '{"name": "John", "age": 30, "city": "New York"}'
csv_data = '''Name,Age,City
            John,30,New York'''

result = identify_data_format(csv_data)

print(f'Format: {result}')
