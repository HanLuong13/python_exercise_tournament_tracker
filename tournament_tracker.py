import csv

participants_list = {}
error_message = 'Invalid response. Try again'

def start_up():
    global num_slots

    print('Welcome to Tournaments R Us \n' + 
    '============================')
    start_invalid = True
    while start_invalid:
        try:
            num_slots = int(input('Enter the number of participants: '))
            start_invalid = False
        except ValueError:
            print(f'{error_message} \n')
    print(f'There are {num_slots} participant slots ready for sign-ups.\n')
    
def main_menu():    
    #validate input
    menu_invalid = True
    while menu_invalid:
        try:
            menu_input = int(input('Participant Menu \n'+
                '================ \n' +
                '1. Sign Up \n' +
                '2. Cancel Sign Up \n' +
                '3. View Participants \n' +
                '4. Save Changes \n' +
                '5. Exit \n\n' +
                'Enter your choice: '))
            if 1 <= menu_input <= 5:
                menu_choice = menu_input
                menu_invalid = False
            else: 
                print(f'{error_message}')
        except ValueError:
            print(f'{error_message}')

    #going into menu choice
    if menu_choice == 1:
        sign_up()
    elif menu_choice == 2:
        cancel_sign_up()
    elif menu_choice == 3:
        view_participants()
    elif menu_choice == 4:
        save_changes()
    elif menu_choice == 5:
        exit()
    else:
        print('Something went wrong.')

def sign_up():
    global participants_list

    print('Participant Sign Up \n' + 
    '====================')
    sign_up_name_invalid = True

    #initialize dictionary
    for key in range(1, num_slots+1):
        participants_list.setdefault(key)

    while sign_up_name_invalid:
        sign_up_name = input('Participant Name: ').title()
        space = sign_up_name.find(' ')
        first_name = sign_up_name[0:space]
        last_name = sign_up_name[space+1: len(sign_up_name)]
        #verifying it has a first and last name
        if ' ' in sign_up_name and len(sign_up_name) >= 3 and first_name.isalpha()\
        and last_name.isalpha():           
            sign_up_name_invalid = False
        else: 
            print(f'{error_message}')

    sign_up_slot_invalid = True
    while sign_up_slot_invalid:
        try:
            sign_up_slot = int(input(f'Desired starting slot #[1-{num_slots}]: '))
            #verifying that slot number is within list
            if 1 <= sign_up_slot <= num_slots:
                # & is not taken
                if participants_list[sign_up_slot] == None:
                    participants_list[sign_up_slot] = sign_up_name 
                    sign_up_slot_invalid = False
                    print(f'Success:\n{sign_up_name} is signed up in starting slot #{sign_up_slot}.')
                else:
                    print(f'Error:\nSlot #{sign_up_slot} is filled. Please try again')
            else:
                print(error_message)
        except ValueError:
            print(error_message)
    main_menu()

def cancel_sign_up():
    print('Participant Cancellation \n' + 
    '========================')
    cancel_slot_invalid = True
    while cancel_slot_invalid:
        try:
            cancel_slot_input = int(input(f'Starting slot #[1-{num_slots}]: '))
            cancel_name_input = input('Participant Name: ').title()
            if 1 <= cancel_slot_input <= num_slots:
                if participants_list[cancel_slot_input] == cancel_name_input:
                    participants_list[cancel_slot_input] = None 
                    cancel_slot_invalid = False
                    print(f'Success:\n{cancel_name_input} has been cancelled from starting slot #{cancel_slot_input}.')
                else:
                    print(f'{cancel_name_input} is not in that starting slot.')
            else:
                print('Slot number not in range. Try again.')
        except ValueError:
            print(error_message)
    main_menu()

def view_participants():
    print('View Participants \n' + 
    '=================')
    view_invalid = True
    while view_invalid:
        try:
            slot_input = int(input(f'Starting slot #[1-{num_slots}]: '))
            if 1 <= slot_input <= num_slots:
                start = slot_input - 5
                if start < 1:
                    start = 1
                end = slot_input + 6
                if end > num_slots:
                    end = num_slots
                print('Starting Slot: Participant')
                for slot in range(start, end):
                    if participants_list[slot] == None: 
                        print(f'{slot}: [empty]')
                    else:
                        print(f'{slot}: {participants_list[slot]}')
                view_invalid = False
        except ValueError:
            print(error_message)  
    main_menu()        

def save_changes():
    print('Save Changes \n' + 
    '============')
    save_invalid = True
    while save_invalid:
        save_input = input('Save your changes to CSV? [y/n] ').lower()
        if save_input == 'y':
            with open('Participants_List.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                for key, value in participants_list.items():
                    writer.writerow([key, value])
            print('Saved.')
            save_invalid = False
        elif save_input == 'n':
            print('Not saved')
            save_invalid = False
        else: 
            print(error_message)
    main_menu()

def exit():
    print('Exit \n' + 
    '=====\n' +
    'Any unsaved changes will be lost.')
    exit_invalid = True
    while exit_invalid:
        exit_input = input('Are you sure you want to exit? [y/n] ')
        if exit_input == 'y':
            print('Goodbye!')
            quit()
        elif exit_input== 'n':
            main_menu()
            exit_invalid = False
        else:
            print(error_message)

start_up()
main_menu()

#verify if name is already in list (maybe later)
    # if sign_up_name in participants_list.values():
    # 
    #    
    # print(participants_list)