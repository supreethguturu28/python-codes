# To remove punctuations from a string using RegEx
import re

random_string = 'Hi there! Meet me @ Palace; '
print("The original string is:", random_string)

final_result = re.sub(r'[!@#$%^&*(/){}?;]', '', random_string)

print("The string after removal of punctuation is:", final_result)
