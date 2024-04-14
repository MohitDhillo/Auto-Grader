import difflib
import re

def preprocess_line(line):
    # Remove comments
    line = line.split('#')[0].rstrip('\n')
    # Ignore empty lines
    if not line.strip():
        return ''
    # Convert to lowercase and replace tab spacing
    return line.lower().replace('\t', '')


def replace_name(content, old_name, new_name):


  new_content = []
#   print(old_name)
#   print(new_name)
  for line in content:
    new_line = line.replace(old_name, new_name)
    # print(new_line)
    new_content.append(new_line)
  return new_content


def replace_function_names(content):
    function_counter = 1
    original_to_new = {}
    new_content = []
    function_regex = r'def\s+\w+\(.*\):'

    for line in content:
        if re.search(function_regex, line):
            original_name = line.split('def ')[1].split('(')[0]

            # print(original_name)
            # print("original_name")
            content= replace_name(content, original_name, "func")
            # print(content)

        # else:
                        # print("original_name")


    return content

import re

def replace_variable_names(content):
    variable_counter = 1
    new_content = []
    variable_dict = {}
    function_regex = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*='

    for line in content:
        # print(line)
        if re.search(function_regex, line):
            # print(line)

            original_name = line.split('=')[0]
            original_name = original_name.rstrip() 
            # print(original_name)
            # print("original_name")
            # print(content)
            # print("                  ")
            content= replace_name(content, original_name, f'temp{variable_counter}')
            # print(content)

            variable_counter = variable_counter + 1

    # for line in content:
    #     new_line = line

    #     # Find all matches of type annotations followed by variable names
    #     matches = re.finditer(r'\b(int|str|float|list|dict)\s+([a-zA-Z_][a-zA-Z0-9_]*)\b', line)
    #     print(matches)
    #     for match in matches:
    #         print(match)

    #         old_variable_name = match.group(2)
    #         print(old_variable_name)

    #         # Replace variable name with a new name
    #         new_variable_name = f'{match.group(1)}_{variable_counter}'
    #         # Increment the counter
    #         variable_counter += 1
    #         # Replace the variable name in the line
    #         new_line = new_line.replace(old_variable_name, new_variable_name)
    #     new_content.append(new_line)

    return content

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()

      # Preprocess lines to remove comments and newline characters
    # content1 = [line.split('#')[0].rstrip('\n') for line in content1]
    # content2 = [line.split('#')[0].rstrip('\n') for line in content2]
    # print()
    # print()

    # for line in content1:
    #     print(line)
    content1 = [preprocess_line(line) for line in content1 if preprocess_line(line)]

    content2 = [preprocess_line(line) for line in content2 if preprocess_line(line)]
    # print(content1)
    # print()
    # print()

    # for line in content1:
    #     print(line)
    # Replace function names
    content1 = replace_function_names(content1)
    content2 = replace_function_names(content2)
    # print(content1)


    # Replace variable names
    content1 = replace_variable_names(content1)
    content2 = replace_variable_names(content2)
    # print(content1)
   

    # print()
    # print()

    # for line in content2:
    #     print(line)


    # Preprocess lines
  

    content1 = [line.replace(' ', '') for line in content1]
    content2 = [line.replace(' ', '')  for line in content2]

    diff = difflib.ndiff(content1, content2)

    matching_lines = 0
    for line in diff:
        if line.startswith('  '):
            print(line)
            matching_lines += 1

    # Calculate plagiarism percentage
    total_lines = len(content1)
    plagiarism_percentage = (matching_lines / total_lines) * 100

    print(f'The files {file1} and {file2} are {plagiarism_percentage}% plagiarized.')

# Usage
file1 = 'file1.py'
file2 = 'file2.py'

compare_files(file1, file2)