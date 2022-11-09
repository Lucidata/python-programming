

import re
# Prompt the user to enter name of file with original text
original_file = open(input('Enter file name containing original text:'), 'r')
# Prompt the user to enter name of file with sensitive words
sensitive_file = open(input('Enter file name containing sensitive words:'), 'r')
# Prompt the user to enter name of file with sensitive words redacted
redacted_file = open(input('Enter file name to write text with redacted words:'), 'w')

# Make a list of sensitive words
sensitive_words = sensitive_file.readlines()

# Read original text
original_data = original_file.read()

for i in sensitive_words:
    src_str  = re.compile(i.strip(), re.IGNORECASE)
    original_data = src_str.sub('*', original_data)
    
# Write the text with redacted words in file
redacted_file.write(original_data)

# Close all files
redacted_file.close()
original_file.close()
sensitive_file.close()

