from lxml import etree
import base64


def replace_img_src_with_blob(html_file_path, image_path):
    # Read the HTML content from the file
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Parse the HTML content using lxml
    parser = etree.HTMLParser()
    tree = etree.HTML(html_content, parser)

    # Find all <img> tags
    # img_tags = tree.xpath('//img')
    img_tags = tree.xpath('//img[contains(@src, "selenium-screenshot-1.png")]')
    print(img_tags)

    # Iterate over found <img> tags
    for img in img_tags:
        # Get the src attribute of the <img> tag
        src_attribute = img.get('src')
        if src_attribute == image_path:
            # Read the image content and encode it in base64
            with open(image_path, 'rb') as image_file:
                image_content = image_file.read()
                encoded_image = base64.b64encode(image_content).decode('utf-8')

            # Construct the data URI for the image
            data_uri = f'data:image/png;base64,{encoded_image}'

            # Replace the src attribute of the <img> tag with the data URI
            img.set('src', data_uri)

    # Serialize the modified HTML tree back to string
    modified_html_content = etree.tostring(tree, encoding='unicode')

    # Write the modified HTML content back to the file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(modified_html_content)

    print(f"Image tag with src='{image_path}' replaced with base64-encoded image data.")


# Example usage:
html_file_path = r'C:\Users\Supreeth\PycharmProjects\pythonProject\log_file\log.html'
image_path = r'C:\Users\Supreeth\PycharmProjects\pythonProject\selenium-screenshot-1.png'

replace_img_src_with_blob(html_file_path, image_path)
