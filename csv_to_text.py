import csv
from io import StringIO


def extract_csv_keys_from_text(csv_text, separator=','):
    # Create a StringIO object to simulate a file-like object from the string
    csv_file = StringIO(csv_text)

    with csv_file:
        reader = csv.DictReader(csv_file, delimiter=separator)
        # Assuming the first row contains the column headers
        keys = [key.replace(separator, '.') for key in reader.fieldnames]

    return keys


text_csv = """ID,First Name,Last Name,Gender
1,Jessica,Richards,Other
2,Daniel,Odonnell,Female
3,William,Swanson,Male
4,Rachel,Brown,Other
5,Renee,Kelley,Other"""

print(extract_csv_keys_from_text(text_csv))


def extract_csv_keys_from_file(csv_file_path, separator=','):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=separator)
        # Assuming the first row contains the column headers
        keys = [key.replace(separator, '.') for key in reader.fieldnames]

    return keys


print(extract_csv_keys_from_file(r"C:\Users\Supreeth\Downloads\data sets\Jira.csv"))
