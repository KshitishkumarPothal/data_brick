import re

print(re.__all__)
text = 'Hello i am dev my num is 991-982-9864 and 123-346-4433  and 12-22-3444'
patten = r"\d{3}-\d{3}-\d{4}"
match = re.findall(patten,text)
print(match)    
# print(match.group())
# print(match.start(),"-" , match.end())


text2 = "Contact me at join@email.com or jane@email.org"
pat2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.findall(pat2,text2)
print(email)

text3= "The date is 2023-12-02"
pat3 = r'(\d{4})-(\d{2})-(\d{2})'
num = re.search(pat3,text3)
print(num.group())
replacement = r'\2/\3/\1'


text1 = "123"
pat = r'\d+'
print((re.fullmatch(pat,text1).group()))