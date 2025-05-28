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
