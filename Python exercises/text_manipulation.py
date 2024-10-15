def process_text(text):
   
    title_case_text = text.title()
    
  
    replaced_text = title_case_text.replace(' I ', ' We ')
    
   
    character_count = len(text)
    
 
    dollar_sign_text = '$' * character_count
    
    return title_case_text, replaced_text, character_count, dollar_sign_text


text = 'at university american college I study the course software engineering where I learn python programming language!'


title_case_text, replaced_text, character_count, dollar_sign_text = process_text(text)


print("Title Case Text:", title_case_text)
print("Replaced Text:", replaced_text)
print("Character Count:", character_count)
print("Dollar Sign Text:", dollar_sign_text)