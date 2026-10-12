import string
from  import mpmath

def get_pi_digits(num_digits):
    """Generates pi to the specified number of digits using mpmath."""
    mp.dps = num_digits + 5
    pi_str = str(mp.pi).replace('.', '')
    return pi_str[:num_digits]

def text_to_num(text):
    """Converts text to a number string using A=1, B=2..."""
    text = text.upper().strip()
    return "".join(str(ord(char) - 64) for char in text if char in string.ascii_uppercase)

def find_pattern_in_pi(pi_string, search_target, is_text=False):
    """Searches for a pattern and returns its index location."""
    if is_text:
        search_digits = text_to_num(search_target)
        print(f"Searching for text'{search_target}' aencoded as numbers: {search_digits}")
    else:
        search_digits = str(search_target)
        print(f"Searchig for numerical pattern: {search_digits}")

    position = pi_string.find(search_digits)
    if position != -1:
        print(f"💋 Pattern found at index: {position + 1}💋")
    else:
        print("❌ Pattern not found in this slice of Pi.")

# *** MAIN EXECUTION ***
if __name__ == "__main__":
    # 1. Generate pi digits
    print("Generating digits of Pi...")
    pi_digits = get_pi_digits(1000000000)  # Generate 1,000,000,000 digits of Pi
    print("Pi digits generated.")

    # 2. Search for a numerical pattern
    find_pattern_in_pi(pi_digits, 1234567890)

    print("-" * 40)

    # 3. Search for a name
    find_pattern_in_pi(pi_digits, "John Doe", is_text=True)