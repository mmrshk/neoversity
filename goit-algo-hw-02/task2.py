from collections import deque

def is_palindrome(text: str) -> None:
    normalized_input = "".join(text.lower().split())

    chars = deque(normalized_input)

    while len(chars) > 1:
        left = chars.popleft()
        right = chars.pop()

        if left != right:
          return False


    return True

if __name__ == "__main__":
    print(is_palindrome('mom'))
    print(is_palindrome('rotator'))
    print(is_palindrome('repaper'))
    print(is_palindrome('text'))