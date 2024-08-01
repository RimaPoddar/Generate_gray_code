def generate_gray_code(n):
    """Generate n-bit Gray code."""
    gray_code = []
    for i in range(1 << n):
        gray_code.append(i ^ (i >> 1))
    return gray_code

def print_gray_code(gray_code):
    """Print Gray code in binary format."""
    for code in gray_code:
        print(f'{code:0{len(bin(max(gray_code)))-2}b}')   #The line print(f'{code:0{len(bin(max(gray_code)))-2}b}') is a formatted string in Python that prints binary numbers with leading zeros to ensure that all numbers have the same length.

# Example usage
n = int(input())  # Number of bits
gray_code = generate_gray_code(n)
print_gray_code(gray_code)
