def check_hamming_code(bits):
    n = len(bits)
    error_position = 0
    
    # Check each parity bit
    for i in range(n):
        if bits[i] == 1:
            error_position ^= (i + 1)
    
    if error_position == 0:
        return "No error"
    else:
        return f"Error at position {error_position}"

# Example binary sequence (from your original data)
bits = [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1]
result = check_hamming_code(bits)
print(result)
