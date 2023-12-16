#!/usr/bin/env python
# coding: utf-8

# In[20]:


import re
text = 'Pythone Exercise, PHP exercise.'
result = re.sub(r'[ ,.]', ':', text)
print(result)


# In[24]:


import pandas as pd
import re 
data = {' ': ['hello, world!', 'test    ', 'four five six']}
df = pd.DataFrame(data)

def clean_text(text):

  cleaned_text = re.sub(r'[^\w\s]', '', text)
  return cleaned_text
print(df)


# In[29]:


import re 

def find_long_words(input_string):
  pattern = re.compile(r'\b\w{4,}\b')
  long_words = pattern.findall(input_string)
  return long_words

input_string = "This is a string with words of various lengths extract four character length."
result = find_long_words(input_string)
print(result)


# In[32]:


import re

def find_specific_length_words(input_string):
    pattern = re.compile(r'\b\w{3,5}\b')
    
    specific_length_words = pattern.findall(input_string)
    
    return specific_length_words
input_string = "This is apr string with words of various lengths extract four character length."
result = find_specific_length_words(input_string)

print(result)


# In[37]:


import re 
import pandas as pd 
def remove_parentheses(strings_list):
    
    pattern = re.compile(r'\(|\)')
    cleaned_list = [pattern.sub('', string) for string in strings_list]
    
    return cleaned_list

input_list = ["example(.com)", "hr@filiprobo(.com)", "github(.com)", "Hello (Data Science World)", "Data(Scientist)"]
result = remove_parentheses(input_list)
new_result = pd.DataFrame(result)

print(new_result.to_string(index=False, header=None, justify ='left'))


# In[ ]:





# In[38]:


import re
sample_text = "ImortanceOfRegularExpressionInPython"

result = re.findall(r'[A-Z][a-z]*', sample_text)
print(result)


# In[40]:


import re

def insert_spaces_before_numbers(text):
    modified_text = re.sub(r'(?<=[a-zA-Z])(?=\d)', ' ', text)
    return modified_text

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces_before_numbers(sample_text)
print(result)


# In[ ]:


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].str[:6]
print(df.head())


# In[44]:


import re 
def match_string(input_string):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    
    if pattern.match(input_string):
        return True
    else:
        return False
test_string1 = "Hello123"
test_string2 = "Special@Character"
test_string3 = "Alpha_Beta_123"
    
print(match_string(test_string1))
print(match_string(test_string2))
print(match_string(test_string3))


# In[45]:


def starts_with_number(input_string, number):
    return input_string.startswith(str(number))

test_string1 = "123Hello"
test_string2 = "111World"
test_string3 = "222Python"

number_to_check = 111

print(starts_with_number(test_string1, number_to_check))
print(starts_with_number(test_string2, number_to_check))
print(starts_with_number(test_string3, number_to_check))


# In[46]:


def remove_leading_zeros(ip_address):
    ip_parts = ip_address.split('.')
    cleaned_ip = '.'.join(str(int(part)) for part in ip_parts)
    return cleaned_ip
    
ip_address_with_zeros = "192.001.002.003"    
cleaned_ip_address = remove_leading_zeros(ip_address_with_zeros)

print(f"Original IP: {ip_address_with_zeros}")
print(f"Cleaned IP: {cleaned_ip_address}")


# In[ ]:





# In[47]:


def search_literals(sample_text, searched_words):
    found_words = [word for word in searched_words if word in sample_text]
    return found_words
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
result = search_literals(sample_text, searched_words)

print(f"Sample Text: '{sample_text}'")
print(f"Searched Words: {searched_words}")
print(f"Found Words: {result}")


# In[50]:


def search_literal_and_location(sample_text, searched_word):
    location = sample_text.find(searched_word)
    return location
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

location = search_literal_and_location(sample_text, searched_word)

print(f"Sample Text: '{sample_text}'")
print(f"Searched Word: '{searched_word}'")
if location != -1:
   print(f"Location: Found at index {location}")
else:
    print(f"Location: Word not found")


# In[52]:


def find_substrings(sample_text, pattern):
    positions = []
    start = sample_text.find(pattern)
    
    while start != -1:
        positions.append(start)
        start = sample_text.find(pattern, start + 1)
        
    return positions
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

positions = find_substrings(sample_text, pattern)

print(f"Sample Text: '{sample_text}'")
print(f"Pattern: '{pattern}'")
if positions: 
    print(f"Occurrences at positions: {positions}")
else:
    print("Pattern not found")


# In[55]:


import re
def find_occurrence_and_position(sample_text, pattern):
    occurrences = []
    
    for match in re.finditer(pattern, sample_text):
        occurrence={
            'substring': match.group(),
            'position': match.start(),
            'end_position': match.end()
        }
        occurrences.append(occurrence)
    return occurrences
sample_text = 'Python exercise, PHP exercises, C# exercises'
pattern = 'exercises'

result = find_occurrence_and_position(sample_text, pattern)

print(f"Sample Text: '{sample_text}'")
print(f"Pattern:'{pattern}'")
if result:
    print("Occurrences:")
    for occurrence in result:
        print(f" Substring: '{occurrence['substring']}'")
        print(f" Position: {occurrence['position']}")
        print(f" End Position: {occurrence['end_position']}")
else: 
       print("Pattern not found")


# In[56]:


from datetime import datetime

def convert_date_format(input_date):
    try:
        parsed_date = datetime.strptime(input_date, '%Y-%m-%d')
        formated_date = parsed_date.strftime('%d-%m-%Y')
        
        return formated_date 
    except ValueError:
        return "Invalid date format"
        
input_date = '2022-12-31'
output_date = convert_date_format(input_date)

print(f"Input Date: {input_date}")
print(f"Converted Date: {output_date}")


# In[57]:


import re

def find_decimal_numbers(input_string):
    pattern = re.compile(r'\b\d+(\.\d{1,2})?\b')
    decimal_numbers = pattern.findall(input_string)
    return decimal_numbers
    
input_string = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output_numbers = find_decimal_numbers(input_string)

print(f"Sample Text: '{input_string}'")
print(f"Decimal Numbers with precision of 1 or 2: {output_numbers}")


# In[58]:


import re 

def find_numbers_and_positions(input_string):
        pattern = re.compile(r'\b\d+\b')
        matches = pattern.finditer(input_string)
        
        results = []
        
        for match in matches:
            number = match.group()
            position =match.span()
            results.append({'number': number, 'position': position})
        
        return results
    
input_string = "There are 3 apples, 27 oranges and 5 bananas."

results = find_numbers_and_positions(input_string)

print(f"Sample Text: '{input_string}'")
print("Numbers and their Positions")
for result in results:
    print(f" Number:{result['number']}, Position: {result['position']}")
    


# In[59]:


import re

def extract_maximum_number(input_string):
    numbers = [int(match) for match in re.findall(r'\b\d+\b', input_string)]
    if numbers: 
        return max(numbers)
    else:
        return None
    
sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
max_number = extract_maximum_number(sample_text)

print(f"Sample Text: '{sample_text}'")
if max_number is not None:
    print(f"Maximum Numeric Value: {max_number}")
else:
    print("No numeric values found")
    


# In[62]:


import re 
def insert_spaces_before_capital(input_string):
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1\2', input_string)
    modified_text = re.sub(r'([a-zA-Z])([A-Z])', r'\1\2', modified_text)
    return modified_text

sample_text = "RegularExpressionIsAnImportantTopicInPython"
output_text = insert_spaces_before_capital(sample_text)

prbCdEfGhIint(f"Sample Text: '{sample_text}'")
print(f"Modified Text: '{output_text}'")


# In[63]:


import re

sample_text = "Find Sequence of One Uppercase Followed by Lowercase: AbCdEfGhIjKlMnOpQrStUvWxYz"

pattern = re.compile(r'\b[A-Z][a-z]*\b')
matches = pattern.findall(sample_text)

print(f"Sample text: '{sample_text}'")
print(f"Matches: {matches}")


# In[66]:


import re 

def remove_continous_duplicates(input_sentence):
    cleaned_sentence = re.sub(r'\b(\w+)( \1)+\b', r'\1',input_sentence)
    return cleaned_sentence

sample_text = "Hello hello world world"
output_text = remove_continous_duplicates(sample_text)

print(f"Sample Text: '{sample_text}'")
print(f"Cleaned text: '{output_text}'")


# In[67]:


import re

def ends_with_alphanumeric(input_string):
    pattern = re.compile(r'^.*[a-zA-Z0-9]$')
    return bool(pattern.match(input_string))

test_string1 = "abc123"
test_string2 = "xyz789!"
test_string3 = "special@characters"

print(f"Test String 1: '{test_string1}', Ends with Alphanumeric:{ends_with_alphanumeric(test_string1)}")
print(f"Test String 2: '{test_string2}', Ends with Alphanumeric:{ends_with_alphanumeric(test_string2)}")
print(f"Test String 3: '{test_string3}', Ends with Alphanumeric:{ends_with_alphanumeric(test_string3)}")


# In[68]:


import re 
def extract_hashtags(input_text):
    pattern = re.compile(r'#\w+')
    hashtags = pattern.findall(input_text)
    return hashtags
sample_text = """RT @kapil_kaushik: #Doltiwal I mean #xyzabc is "hurt" by
#Demonetization as the same
has rendered USELESS <ed><U+00BD><ed><U+0089> "acquired funds" No wo"""

hashtags_result = extract_hashtags(sample_text)

print(f"Sample Text: {sample_text}'")
print(f"Extracted Hashtags: {hashtags_result}")


# In[70]:


import re 
def remove_special_symbols(input_text):
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')
    cleaned_text = pattern.sub('', input_text)
    return cleaned_text
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"
cleaned_text = remove_special_symbols(sample_text)

print(f"Sample Text: '{sample_text}'")
print(f"Cleaned Text: '{cleaned_text}'")


# In[71]:


import re

def remove_words_of_length_between_2_and_4(input_string):
    pattern = re.compile(r'\b\w{2,4}\b')
    cleaned_text = pattern.sub('',input_string)
    return cleaned_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements.4 elements are then added to the ArrayList and teh ArrayList is trimmed accordingly."

output_text = remove_words_of_length_between_2_and_4(sample_text)

print(f"Sample Text: '{sample_text}'")
print(f"Cleaned text: '{output_text}'")


# In[ ]:




