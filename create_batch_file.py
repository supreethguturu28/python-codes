import os

# Define the path to the Python script
python_script_path = os.path.abspath("script.py")

# Create the content of the batch file
batch_content = f"""
@echo off
python "{python_script_path}"
pause
"""

# Path where the batch file will be created
batch_file_path = "run_python_script.bat"

# Write the content to the batch file
with open(batch_file_path, "w") as batch_file:
    batch_file.write(batch_content)

print(f"Batch file created: {batch_file_path}")
