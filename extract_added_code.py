import sys
import difflib
from diff_match_patch import diff_match_patch

# Read the diff output file as input
with open(sys.argv[1], 'r') as f:
    diff_output = f.read()

# Split the diff output into lines
diff_lines = diff_output.splitlines()

# Initialize a diff_match_patch object
dmp = diff_match_patch()

# Initialize variables to store added and removed code
added_code = ''
removed_code = ''

# Loop through the lines of the diff output
for line in diff_lines:
    if line.startswith('+'):
        # If the line starts with a plus sign, it is added code
        added_code += line[1:] + '\n'
    elif line.startswith('-'):
        # If the line starts with a minus sign, it is removed code
        removed_code += line[1:] + '\n'

# Output the added code
print(added_code.strip())
