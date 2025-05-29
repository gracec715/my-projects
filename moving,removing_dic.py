'''Moving items from one list to another list'''

#Start with users that need to be verified, 
# and an empty list to hold confirmed user. 

unconfirmed_users = ['alice', 'brain', 'candance']
confirmed_users = []

#very each user until there are no more unconfirmed users. 
#Move each verified user into the list with the confirmed_users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    # .append() -> this will update the empty list called confirmed_users
    confirmed_users.append(current_user)

#Disply all confirmed users. 

print("\nThe following user have been confirmed:")
for confirmed in confirmed_users:
    print(confirmed.title())



print("\n Remove specific values from a list")

#list of values, we assign from right side(temporary) to a variable to perist. 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
# fast remove O(1), the value(frequency) shows the key(the animal type) is more than one(duplicate)
print("\n dictionary for a fast lookups no duplicate")

pets = {
    'dog': 2,
    'cat': 3,
    'goldfish': 1,
    'rabbit': 1
}

pet_counts = {}

for animal in pets:
    if animal in pet_counts:
        pet_counts[animal] += 1
    else:
        pet_counts[animal] = 1

print("\nFilling a Dictionary with User Input")

response = {}

#Set a flag to indicate that polling is active. 
polling_active = True

while polling_active:
    #Prompt for the person's name and response. 
    name = input("\nWhat is your name? ")
    mountain = input("What mountain would you like to climb someday? ")

    #Store the answer in the dictionary. 
    response[name] = mountain

    # Find out if anyone else is going to take the poll. 
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
print("\n ---- Poll Results ---- ")
for name, mountain in response.items():
    print(f"{name} would like to climb {mountain}.")

