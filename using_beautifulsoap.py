import re
import json


def extract_img_src_from_js(html_file_path):
    # Read the HTML content from the file
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
        print(html_content)

    # Use regular expression to find the JavaScript array assignment
    pattern = r'window\.output\["strings"\]\s*=\s*(\[.*?\]);'
    print(pattern)
    match = re.findall(pattern, html_content, re.DOTALL)
    print(match)

    # if match:
    #     # Extract the JavaScript array string
    #     js_array_string = match.group(1)
    #
    #     # Load the JavaScript array as JSON (assuming it's valid JSON format)
    #     try:
    #         js_array = json.loads(js_array_string)
    #         print(js_array)
    #     except json.JSONDecodeError as e:
    #         print(f"Error decoding JSON: {e}")
    #         return []
    #
    #     # Extract img src attributes from each JavaScript string in the array
    #     img_src_list = []
    #     for item in js_array:
    #         # Use regex to find img src attribute within the JavaScript string
    #         img_src_matches = re.findall(r'<img\s+src=["\'](.*?)["\']', item)
    #         if img_src_matches:
    #             img_src_list.extend(img_src_matches)

    #     return img_src_list
    # else:
    #     print("JavaScript array 'window.output[\"strings\"]' not found in the HTML content.")
    #     return []

    return match


# Example usage:
html_path = r'C:\Users\Supreeth\PycharmProjects\pythonProject\log_file\log.html'
img_src_list = extract_img_src_from_js(html_path)
print("Extracted img src attributes:", img_src_list)
# for img_src in img_src_list:
#     print(img_src)
