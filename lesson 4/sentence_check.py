check = input('Enter sentence (ends with punctuation): ')

if check.endswith('?'):
    print("Your sentence is an interogative sentence")
elif check.endswith('!'):
    print("Your sentence is an imperative sentence")
elif check.endswith('.'):
    print("Your sentence is a declarative sentence")
else:
    print("We can't classify your sentence.")