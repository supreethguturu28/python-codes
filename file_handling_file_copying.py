# Python code to copy content of one file to another using file handling

original_file = open("test1.robot", "w")
original_file.write("*** Settings ***\r\nDocumentation     A test suite for valid login.\r\n...\r\n...               "
                    "Keywords are imported from the resource file\r\nResource          keywords.resource\r\nDefault "
                    "Tags      positive\r\n\r\n*** Test Cases ***\r\nLogin User with Password\r\n    Connect to "
                    "Server\r\n    Login User            ironman    1234567890\r\n    Verify Valid Login    Tony "
                    "Stark\r\n    [Teardown]    Close Server Connection\r\n\r\nDenied Login with Wrong Password\r\n   "
                    " [Tags]    negative\r\n    Connect to Server\r\n    Run Keyword And Expect Error    *Invalid "
                    "Password    Login User    ironman    123\r\n    Verify Unauthorised Access\r\n    [Teardown]    "
                    "Close Server Connection\r\n    \r\n    \r\n")
original_file.close()

temp_file = open("test2.robot", "w")

with open('test1.robot', 'r') as firstfile, open('test2.robot', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)

temp_file = open("test2.robot", "r")
print(temp_file.read())
