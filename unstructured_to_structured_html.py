from bs4 import BeautifulSoup


def structure_html(unstructured_html):
    # Parse the unstructured HTML using BeautifulSoup
    soup = BeautifulSoup(unstructured_html, 'html.parser')

    # Use prettify() to structure the HTML
    structured_html = soup.prettify()

    return structured_html


if __name__ == "__main__":
    # Replace 'path/to/your/input/file.html' and 'path/to/your/output/structured_file.html' with the actual paths
    input_file_path = 'unstructured_html.txt'
    output_file_path = 'structured_html.html'

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            unstructured_html_code = file.read()
            structured_html_code = structure_html(unstructured_html_code)

            # Save the structured HTML code to a new file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(structured_html_code)

            print(f"Structured HTML code saved to '{output_file_path}'")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
