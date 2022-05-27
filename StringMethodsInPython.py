a='Christriano Ronaldo'
print(a.startswith('C'))
print(a.startswith('Chri'))
print(a.upper())
print(a.lower())
print(a.split())
print(a.find('r'))
print(a.index('r'))
print(a.rfind('r'))#reverse find
print(a.rindex('r'))#reverse index
b='    Technical Hub    '
print(b.strip())#removes extra spaces
print(a.center(30))#adding extra spaces
print(a.isupper())
print(a.islower())
s=['h','e','l','l','o']
print("".join(s))
print("".join(s[::-1]))#reverse functions are not available for strings
print(a.replace('i','l'))
