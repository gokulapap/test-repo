import re
import sys

password_pattern = r'(?i)\b(password|passwd|pwd|secret|token|apiKey|accessKey|accessToken|client_secret|oauth_token|bearer_token|session_id|session_token|csrf_token)\b\s*[=:]\s*([\'"])([^\'"]+)\2'
basic_auth_pattern = r'(?i)Authorization:\s*Basic\s*([\'"]?)(\w+)\1'
bearer_auth_pattern = r'(?i)Authorization:\s*Bearer\s*([\'"]?)(\w+)\1'

with open(sys.argv[1], 'r') as f:
    contents = f.read()

password_matches = re.findall(password_pattern, contents)
basic_auth_matches = re.findall(basic_auth_pattern, contents)
bearer_auth_matches = re.findall(bearer_auth_pattern, contents)

f = open("output.txt", "w")
if password_matches or basic_auth_matches or bearer_auth_matches:
    f.write('Found hardcoded passwords or tokens: \n')
    for match in password_matches:
        key = match[0]
        value = match[2]
        f.write(f"{key}: {value}")
    for match in basic_auth_matches:
        value = match[1]
        f.write(f"Authorization: Basic {value}")
    for match in bearer_auth_matches:
        value = match[1]
        f.write(f"Authorization: Bearer {value}")
else:
    pass

