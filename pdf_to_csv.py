import csv
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LAParams


def pdf_to_csv(pdf_path, csv_path):
    with open(pdf_path, 'rb') as file:
        # Use layout analysis to preserve the structure of the PDF
        laparams = LAParams()
        text = extract_text(file, laparams=laparams)

    # Split the text into lines
    lines = text.split('\n')

    # Create a CSV file and write lines to it
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Iterate through lines and split based on commas (customize as needed)
        for line in lines:
            row = [cell.strip() for cell in line.split(',')]
            csv_writer.writerow(row)

    return None


if __name__ == "__main__":
    # Replace 'input.pdf' and 'output.csv' with your actual file paths
    pdf_file = r'C:\Users\Supreeth\Downloads\Jira_template.pdf'
    csv_file = r'C:\Users\Supreeth\Downloads\Jira_template.csv'

    pdf_to_csv(pdf_file, csv_file)
