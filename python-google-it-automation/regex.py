import re

result=re.search(r"app","Bappy")

print(result)

result=re.search(r"^x",'xylophone')

print(result)

result=re.search(r"^p.ng",'pingpong')

print(result)

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


result=re.search(r"cad.","AcAdemia",re.IGNORECASE)

print(result)


result=re.search(r"[Pp]ython","python")

print(result)

result=re.search(r"[a-z]way","This is the highway")

print(result)


def check_punctuation (text):
  result = re.search(r"[,\.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


result=re.search(r"[^a-z ]+","the QUICK brown fox")
print(result)

result=re.search(r"cat|dogs","I don't love dogs!")

print(result)


result=re.search(r"P.*n","Python Programming")

print(result)


def repeating_letter_a(text):
  result = re.search(r"[Aa]+.*[Aa]+.", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

result=re.search(r"P?each","To each of them.")

print(result)


result=re.search(r"P?each","I love peach!")

print(result)



import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s+([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)



import re
def multi_vowel_words(text):
  pattern = r"[\w]*[aeiou]{3,}[\w]*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []




import re
def transform_record(record):
  new_record = re.sub(r"([\w\s]+),([0-9-\s]+),([\w\s]+)",r"\1,+1-\2,\3",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer




import re
def transform_comments(line_of_code):
  result = re.sub(r"([\w\s]*)([#]+)([\w\s]+)",r"\1//\3",line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"



import re
def convert_phone_number(phone):
  result = re.sub(r"([\d]{3})-([\d]{3}-[\d]{4}[^\d]*$)",r"(\1) \2",phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300