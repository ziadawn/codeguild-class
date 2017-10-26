'''
Lab27: Contact List
Build a contact list, add to it, retrieve data, etc.
'''

# with open('contacts.csv', 'r') as file:
#     keys = file.readline().strip().split(',')           # splitting off the first line to get my keys, which isn't the people
#     contacts = []
#     for line in file:
#         line = line.strip()     # removes white space, new lines, and the lists from printing with \n at the end
#         line = line.split(',')
#         print(line)
#         contacts.append({keys[0]: line[0], keys[1]: line[1], keys[2]: line[2]})
#     print(contacts)


with open('contacts.csv', 'r') as file:
    keys = file.readline().strip().split(',')           # splitting off the first line to get my keys, which isn't the people
    contacts = []
    for line in file:
        line = line.strip()     # removes white space, new lines, and the lists from printing with \n at the end
        line = line.split(',')
        # print(line)
        contact = {}

        for i in range(len(line)):
            contact[keys[i]] = line[i]

        contacts.append(contact)
    # print(f'contacts = {contacts}')

def create_new_contact(keys):       # if this used more generic variables, it could be used for any dictionary!
    new_contact = {}        # creating a new contact dictionary that we then add to the existing contacts list above
    for key in keys:
        new_contact[key] = input(f'Enter {key}: ')
    print(new_contact)
    return new_contact

def retrieve_contact(contact_list, who_find):
    run = "y"
    found = []
    while run == 'y' and not found:
        for contact in contact_list:
            for value in contact.values():
                if who_find in value.lower():
                    found.append(contact)
                    break
        if not found:                       # could also do if len(found) = 0
            run = input('\nThere are no matches for that entry. Would you like to search again? (y/n): ').lower()
            who_find = input("\nWhat are you looking for: ")
    return found

def update_contact(contact_list):
    to_update = input('\nWhich contact would you like to update? ')
    found = retrieve_contact(contact_list, to_update)
    if len(found) > 1:
        for index, value in enumerate(found):
            print(index, value)
        pick_found = input('\nWhich contact would you like to edit? ')
        edit_contact = found[int(pick_found)]
        edit_index = contact_list.index(edit_contact)
    elif len(found) == 1:
        edit_contact = found[0]
        edit_index = contact_list.index(edit_contact)
    else:
        print("\nThere are no matches for that entry. Would you like to search again? y/n\n")
        return

    print(edit_contact)
    which_field = input('\nEnter the field you would like to edit, and the update, separated by commas.\n')
    which_field = which_field.replace(", ", ",").split(',')
    key = which_field[0]
    value = which_field[1]
    edit_contact[key] = value

    contact_list[edit_index] = edit_contact
    print(edit_contact)
    return edit_contact

def delete_contact(contact_list):
    to_delete = input('\nWhich contact would you like to delete? ' )
    found = retrieve_contact(contact_list, to_delete)
    if len(found) > 1:
        for index, value in enumerate(found):
            print(index, value)
        pick_found = input('\nThere are multiple matches for that entry. Which do you mean? ')
        edit_contact = found[int(pick_found)]
    elif len(found) == 1:
        edit_contact = found[0]
    else:
        print("\nThere are no matches for that entry. Would you like to search again? y/n\n")
        return
    confirm_delete = input(f'\nAre you sure you want to delete {edit_contact["name"]}? This cannot be undone! (y/n) ')
    if confirm_delete == 'y':
        contact_list.remove(edit_contact)

def format_dictionary(contact):
    contact_entry = []                  # THIS WORKS, BUT I'D LIKE TO KEEP TWEAKING THIS FORMATTING, MAYBE AS A STRING?
    for key, value in contact.items():
        contact_entry.append(f'{key}: {value}')
    print(f'{contact_entry}\n')



contacts_action = ''

while contacts_action != '0':
    contacts_action = input('''
    --------------------------
    What would you like to do?
    1: Create new contact
    2: Retrieve contact
    3: Update contact
    4: Delete contact
    5: List contacts
    0: Quit
    -------------------------
    ''')
    if contacts_action == '1':
        contacts.append(create_new_contact(keys))
    elif contacts_action == '2':
        search = input("\nWhat are you looking for? ")
        for line in retrieve_contact(contacts, search):
            print(line)
    elif contacts_action == '3':
        update_contact(contacts)
    elif contacts_action == '4':
        delete_contact(contacts)
    elif contacts_action == '5':
        for contact in contacts:
            format_dictionary(contact)

