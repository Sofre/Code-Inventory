def process_text(input_text):
  
    upper_text = input_text.upper()
    
    sliced_text = upper_text[3:7:2]
    
    return upper_text, sliced_text

user_input = input("Enter text in all small letters: ")
uppercase_text, sliced_text = process_text(user_input)

print("Uppercase Text:", uppercase_text)
print("Sliced Text (index 3 to 7, step 2):", sliced_text)