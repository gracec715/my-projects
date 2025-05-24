favorite_language = {
    'grace': 'python',
    'francis': 'c++',
    'sarah': 'rust',
    'alex': 'python',
}

if 'alice' not in favorite_language.leys():
    print("Alice, please take our poll!")

for name in sorted(favorite_language.key()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

print("\n include set")
for language in set(favorite_language.values()):
    print(language.title())