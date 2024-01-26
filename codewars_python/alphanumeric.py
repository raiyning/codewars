import re

def alphanumeric(password):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')

    # Test the regex
    if pattern.match(password):
        return True
    else:
        return False
print(alphanumeric("PassW0rd"))