# Function to assign the given json data to a temporary file by splitting
# name as file name and content as content of file

import json

data_given = {
    "name": "testcases.robot",
    "type": "file",
    "content": "*** Settings ***\nDocumentation     A test suite for valid login.\n...\n...               Keywords "
               "are imported from the resource file\nResource          keywords.resource\nDefault Tags      "
               "positive\n\n*** Test Cases ***\nLogin User with Password\n    Connect to Server\n    Login User       "
               "     ironman    1234567890\n    Verify Valid Login    Tony Stark\n    [Teardown]    Close Server "
               "Connection\n\nDenied Login with Wrong Password\n    [Tags]    negative\n    Connect to Server\n    "
               "Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123\n    Verify "
               "Unauthorised Access\n    [Teardown]    Close Server Connection\n\n\n"
}


def function_to_split_data(x):
    y = json.dumps(x)
    y_dict = json.loads(y)
    temp_file = open(y_dict["name"], "w")
    temp_file.write(y_dict["content"])
    temp_file.close()


function_to_split_data(data_given)
