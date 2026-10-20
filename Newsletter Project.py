import string
import mpmath as mp

def get_pi_digits(num_digits: int) -> str:
    """Generates pi to the specified number of digits using mpmath."""
    if not isinstance(num_digits, int) or isinstance(num_digits, bool) or num_digits < 1:
        raise ValueError("num_digits must be a positive integer")

    pi_context = mp.mp.clone()
    pi_context.dps = num_digits + 10
    pi_string = pi_context.nstr(pi_context.pi, n=num_digits + 10)
    return pi_string.replace(".", "")[:num_digits]

def text_to_num(text: str) -> str:
    """Converts text to a number string using A=1, B=2..."""
    text = text.upper().strip()
    return "".join(str(ord(char) - 64) for char in text if char in string.ascii_uppercase)

def find_pattern_in_pi(pi_string: str, search_target: str | int, is_text: bool = False) -> int:
    """Searches for a pattern and returns its zero-based index, or -1 if not found."""
    if is_text:
        search_digits = text_to_num(str(search_target))
        print(f"Searching for text '{search_target}' encoded as numbers: {search_digits}")
    else:
        search_digits = str(search_target)
        print(f"Searching for numerical pattern: {search_digits}")

    if not search_digits:
        print("Search pattern is empty.")
        return -1

    position = pi_string.find(search_digits)
    if position != -1:
        print(f"Pattern found at index: {position + 1}")
    else:
        print("Pattern not found in this slice of Pi.")
    return position

# *** MAIN EXECUTION ***
if __name__ == "__main__":
    # 1. Generate pi digits
    print("Generating digits of Pi...")
    pi_digits = get_pi_digits(100_000)
    print("Pi digits generated.")

    # 2. Search for a numerical pattern
    find_pattern_in_pi(pi_digits, 1234567890)

    print("-" * 40)

    # 3. Search for a name
    find_pattern_in_pi(pi_digits, "John Doe", is_text=True)