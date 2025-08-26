import win32com.client
import os

try:
    # Initialize Outlook
    outlook = win32com.client.gencache.EnsureDispatch("Outlook.Application")

    # Create a new mail item
    mail = outlook.CreateItem(0)

    # Set email details
    mail.To = "email_id"
    mail.Subject = "File - PIP"
    mail.Body = "Hi there!\n\nHereby, attaching the file related to the installation of pip."

    # # Specify the attachment file path
    # attachment_path = r"C:\Users\User\Downloads\file_name.py"
    #
    # # Check if file exists before attaching
    # if os.path.exists(attachment_path):
    #     mail.Attachments.Add(attachment_path)
    # else:
    #     print(f"Error: Attachment file not found at {attachment_path}")

    # Display the email before sending (optional)
    # mail.Display()

    # Send the email
    mail.Send()

    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
