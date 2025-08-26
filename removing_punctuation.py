# To remove punctuations from a string

random_string = "Hi there! Meet me @ Palace; "
print("The original string is:", random_string)

punctuations = '''~!@#$%^&*()_{[}]|:;"'?'''

final_result = " "

for element in random_string:
    if element not in punctuations:
        final_result = final_result + element

print("The string after removal of punctuation is:", final_result)
