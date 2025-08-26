import pandas as pd

# Read the CSV file into a DataFrame
file_path = r'C:\Users\Supreeth\PycharmProjects\pythonProject\modified_file.csv'
df = pd.read_csv(file_path)

# Modify the "official_email_id" column
df['personal_email_id'] = df['personal_email_id'].apply(lambda x: x.split('@')[0] + '@gmail.com')

# Save the modified DataFrame to a new CSV file
output_file_path = 'modified_file.csv'
df.to_csv(output_file_path, index=False)

print(f"Modified data saved to {output_file_path}")
