from collections import deque

def is_palindrome(s):
    formatted_string = ''.join(ch.lower() for ch in s if ch.isalnum())

    d = deque(formatted_string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True