#WONG WEI FONG
#TP065467

import time


def add_current_tenant_details():
    current_tenant_details = []
    ctd = []
    current_tenant_name = input("Enter name: ")
    if any(map(str.isdigit, current_tenant_name)) == True:
        print("Name shouldn't contain integer, please try again.")
        add_current_tenant_details()
    else:
        current_tenant_name = current_tenant_name.title()
        ctd.append(current_tenant_name)
        current_tenant_ic = input("Enter ic number (______-__-____) : ")
        if any(map(str.isalpha, current_tenant_ic)) == True or len(current_tenant_ic) != 14:
            print("Invalid input, please try again.")
            add_current_tenant_details()
        else:
            ctd.append(current_tenant_ic)
            current_tenant_pob = input("Enter place of birth: ")
            if any(map(str.isdigit, current_tenant_pob)) == True:
                print("Place shouldn't contains integer, please try again.")
                add_current_tenant_details()
            else:
                current_tenant_pob = current_tenant_pob.title()
                ctd.append(current_tenant_pob)
                current_tenant_cob = input("Enter city of birth: ")
                if any(map(str.isdigit, current_tenant_cob)) == True:
                    print("City shouldn't contains integer, please try again.")
                    add_current_tenant_details()
                else:
                    current_tenant_cob = current_tenant_cob.title()
                    ctd.append(current_tenant_cob)
                    current_tenant_work = input("Enter work history: ")
                    ctd.append(current_tenant_work)
                    current_tenant_employer = input("Enter current employer: ")
                    if any(map(str.isdigit, current_tenant_employer)) == True:
                        print("Name shouldn't contains integer, please try again.")
                        add_current_tenant_details()
                    else:
                        current_tenant_employer = current_tenant_employer.title()
                        ctd.append(current_tenant_employer)
                        current_tenant_unit = input("Enter unit rent: ")
                        ctd.append(current_tenant_unit)
                        current_tenant_details.append(ctd)

                    with open('current_tenant_file.txt', 'a') as current_tenant_file:
                        for actd in current_tenant_details:
                            current_tenant_file.write(f'{actd}\n')
                    print("Current tenant details added\n", current_tenant_details)

    quit_key = input("Enter any key to leave. ")
    if quit_key == '0':
        print("Redirecting to Current Tenant Page...")
    else:
        print("Redirecting to Current Tenant Page...")

def view_current_tenant_details():
    print("Printing current tenant details......")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('current_tenant_file.txt', 'r') as current_tenant_file:
        number = 0
        for line in current_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(number, "details printed")

    while True:
        quit_key = input("Enter any key to leave. ")
        if quit_key == '0':
            print("Redirecting to Current Tenant Page...")
            break
        else:
            print("Redirecting to Current Tenant Page...")
            break

def search_current_tenant_details():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('current_tenant_file.txt', 'r') as current_tenant_file:
        number = 0
        printed = 0
        search_key = input("Details to search: ")
        print("Searching details consists of", search_key, "......")
        for line in current_tenant_file:
            line = line.rstrip()
            number += 1
            if not search_key.lower() in line.lower():
                continue
            print(number, ":", line)
            printed += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if printed >= 1:
            print(printed, "details found")
            current_tenant_search_decision()
        elif printed == 0:
            print("No result found")
            current_tenant_search_decision()
def current_tenant_search_decision():
    search_input = input("Search again? (Y/N) ")
    if search_input.upper() == "Y":
        search_current_tenant_details()
    elif search_input.upper() == "N":
        print("Redirecting to Current Tenant Page...")
    else:
        print("Invalid input")
        current_tenant_search_decision()

def modify_current_tenant_details():
    rowvalidate = False
    columnvalidate = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('current_tenant_file.txt', 'r') as current_tenant_file:
        number = 0
        for line in current_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while not columnvalidate:
        row = optionvalid("Number of list to modify: ")
        row = int(row - 1)
        if row >= number or row < 0:
            print("Invalid number of list, please try again.")
        else:
            columnvalidate = True
            while not rowvalidate:
                column = optionvalid("Which column is it on? \n 1/2/3/4/5/6/7: ")
                column = int(column - 1)
                if column < 0 or column > 6:
                    print("Invalid column, please try again.")
                else:
                    rowvalidate = True
                    new = str(input("Change to: "))

    with open('current_tenant_file.txt', 'r+') as current_tenant_file:
        array = []
        for line in current_tenant_file:
            item = line.rstrip().split(", ")
            array.append(item)
        print("The details modified from ", array[row][column], "to ", new)
        a = "'"
        b = "["
        c = "]"
        if column > 0 and column < 6:
            array[row][column] = str(a + new + a)
        elif column == 0:
            array[row][column] = str(b + a + new + a)
        elif column == 6:
            array[row][column] = str(a + new + a + c)

    # adding modified list back to text file
    with open('current_tenant_file.txt', 'r+') as current_tenant_file:
        for line in array:
            y = 7
            x = 6
            for item in line:
                if y > 0:
                    current_tenant_file.write(item)
                    y = y - 1
                    if x > 0:
                        current_tenant_file.write(", ")
                        x = x - 1
                    else:
                        current_tenant_file.write("\n")
        print("Details updated")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('current_tenant_file.txt', 'r') as current_tenant_file:
        number = 0
        for line in current_tenant_file:
            line = line.rstrip()
            number += 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        decision_input = input("Enter any key to skip.")
        if decision_input == 1:
            current_tenant_modify_decision()
        else:
            current_tenant_modify_decision()
def current_tenant_modify_decision():
    modify_input = input("Modify again? (Y/N) ")
    if modify_input.upper() == "Y":
        modify_current_tenant_details()
    elif modify_input.upper() == "N":
        print("Redirecting to Current Tenant Page...")
    else:
        print("Invalid input")
        current_tenant_modify_decision()

def delete_current_tenant_details():
    rowvalidate = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('current_tenant_file.txt', 'r') as current_tenant_file:
        number = 0
        for line in current_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while not rowvalidate:
        row = optionvalid("Which row to delete: ")
        row = int(row - 1)
        if row >= number or row < 0:
            print("Invalid number of list, please try again.")
        else:
            rowvalidate = True
            delete_confirmation = input("Confirm proceed to delete details?\nOnly enter Y will proceed to. ")
            if delete_confirmation.upper() == "Y":
                with open('current_tenant_file.txt', 'r+') as current_tenant_file:
                    lines = current_tenant_file.readlines()
                    current_tenant_file.seek(0)
                    current_tenant_file.truncate()
                    for number, line in enumerate(lines):
                        if number not in [row]:
                            current_tenant_file.write(line)
                    print("Details updated")
            else:
                print("Delete action has cancelled.")
                return

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('current_tenant_file.txt', 'r') as current_tenant_file:
        number = 0
        for line in current_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        quit_key = input("Enter any key to leave. ")
        if quit_key == '0':
            print("Redirecting to Current Tenant Page...")
            break
        else:
            print("Redirecting to Current Tenant Page...")
            break


def add_past_tenant_details():
    past_tenant_details = []
    ptd = []
    past_tenant_name = input("Enter name: ")
    if any(map(str.isdigit, past_tenant_name)) == True:
        print("Name shouldn't contain integer, please try again.")
        add_past_tenant_details()
    else:
        past_tenant_name = past_tenant_name.title()
        ptd.append(past_tenant_name)
        past_tenant_ic = input("Enter ic number (______-__-____) : ")
        if any(map(str.isalpha, past_tenant_ic)) == True or len(past_tenant_ic) != 14:
            print("Invalid input, please try again.")
            add_past_tenant_details()
        else:
            ptd.append(past_tenant_ic)
            past_tenant_pob = input("Enter place of birth: ")
            if any(map(str.isdigit, past_tenant_pob)) == True:
                print("Place shouldn't contains integer, please try again.")
                add_past_tenant_details()
            else:
                past_tenant_pob = past_tenant_pob.title()
                ptd.append(past_tenant_pob)
                past_tenant_cob = input("Enter city of birth: ")
                if any(map(str.isdigit, past_tenant_cob)) == True:
                    print("City shouldn't contains integer, please try again.")
                    add_past_tenant_details()
                else:
                    past_tenant_cob = past_tenant_cob.title()
                    ptd.append(past_tenant_cob)
                    past_tenant_unit = input("Enter unit rent: ")
                    ptd.append(past_tenant_unit)
                    past_tenant_details.append(ptd)

                with open('past_tenant_file.txt', 'a') as past_tenant_file:
                    for aptd in past_tenant_details:
                        past_tenant_file.write(f'{aptd}\n')

                print("Past tenant details added\n", past_tenant_details)

def view_past_tenant_details():
    print("Printing past tenant details......")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Past Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('past_tenant_file.txt', 'r') as past_tenant_file:
        number = 0
        for line in past_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(number, "details printed")

    while True:
        quit_key = input("Enter any key to leave. ")
        if quit_key == '0':
            print("Redirecting to Past Tenant Page...")
            break
        else:
            print("Redirecting to Past Tenant Page...")
            break

def search_past_tenant_details():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Past Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('past_tenant_file.txt', 'r') as past_tenant_file:
        number = 0
        printed = 0
        search_key = input("Details to search: ")
        print("Searching details consists of", search_key, "......")
        for line in past_tenant_file:
            line = line.rstrip()
            number += 1
            if not search_key.lower() in line.lower():
                continue
            print(number, ":", line)
            printed += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if printed >= 1:
            print(printed, "details found")
            past_tenant_search_decision()
        elif printed == 0:
            print("No result found")
            past_tenant_search_decision()
def past_tenant_search_decision():
    search_input = input("Search again? (Y/N) ")
    if search_input.upper() == "Y":
        search_past_tenant_details()
    elif search_input.upper() == "N":
        print("Redirecting to Past Tenant Page...")
    else:
        print("Invalid input")
        past_tenant_search_decision()

def modify_past_tenant_details():
    rowvalidate = False
    columnvalidate = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Past Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('past_tenant_file.txt', 'r') as past_tenant_file:
        number = 0
        for line in past_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while not rowvalidate:
        row = optionvalid("Number of list to modify: ")
        row = int(row - 1)
        if row >= number or row < 0:
            print("Invalid number of list, please try again.")
        else:
            rowvalidate = True
            while not columnvalidate:
                column = optionvalid("Which column is it on? \n 1/2/3/4/5: ")
                column = int(column - 1)
                if column < 0 or column > 4:
                    print("Invalid column, please try again.")
                else:
                    columnvalidate = True
                    new = str(input("Change to: "))

    with open('past_tenant_file.txt', 'r+') as past_tenant_file:
        array = []
        for line in past_tenant_file:
            item = line.rstrip().split(", ")
            array.append(item)
        print("The details modified from ", array[row][column], "to ", new)
        a = "'"
        b = "["
        c = "]"
        if column > 0 and column < 4:
            array[row][column] = str(a + new + a)
        elif column == 0:
            array[row][column] = str(b + a + new + a)
        elif column == 4:
            array[row][column] = str(a + new + a + c)

    with open('past_tenant_file.txt', 'r+') as past_tenant_file:
        for line in array:
            y = 5
            x = 4
            for item in line:
                if y > 0:
                    past_tenant_file.write(item)
                    y = y - 1
                    if x > 0:
                        past_tenant_file.write(", ")
                        x = x - 1
                    else:
                        past_tenant_file.write("\n")
        print("Details updated")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Past Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('past_tenant_file.txt', 'r') as past_tenant_file:
        number = 0
        for line in past_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        decision_input = input("Enter any key to skip.")
        if decision_input == 1:
            past_tenant_modify_decision()
        else:
            past_tenant_modify_decision()
def past_tenant_modify_decision():
    modify_input = input("Modify again? (Y/N) ")
    if modify_input.upper() == "Y":
        modify_past_tenant_details()
    elif modify_input.upper() == "N":
        print("Redirecting to Current Tenant Page...")
    else:
        print("Invalid input")
        past_tenant_modify_decision()

def delete_past_tenant_details():
    rowvalidate = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Past Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('past_tenant_file.txt', 'r') as past_tenant_file:
        number = 0
        for line in past_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while not rowvalidate:
        row = optionvalid("Which row to delete: ")
        row = int(row - 1)
        if row >= number or row < 0:
            print("Invalid number of list, please try again.")
        else:
            rowvalidate = True
            delete_confirmation = input("Confirm proceed to delete details?\nOnly enter Y will proceed to. ")
            if delete_confirmation.upper() == "Y":
                with open('past_tenant_file.txt', 'r+') as past_tenant_file:
                    lines = past_tenant_file.readlines()
                    past_tenant_file.seek(0)
                    past_tenant_file.truncate()
                    for number, line in enumerate(lines):
                        if number not in [row]:
                            past_tenant_file.write(line)
                    print("Details updated")
            else:
                print("Delete action has cancelled.")
                return

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Past Tenant Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('past_tenant_file.txt', 'r') as past_tenant_file:
        number = 0
        for line in past_tenant_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        quit_key = input("Enter any key to leave. ")
        if quit_key == '0':
            print("Redirecting to Past Tenant Page...")
            break
        else:
            print("Redirecting to Past Tenant Page...")
            break


def add_apartment_details():
    apartment_details = []
    ad = []
    apartment_name = input("Enter tenant name: ")
    if any(map(str.isdigit, apartment_name)) == True:
        print("Name shouldn't contain integer, please try again.")
        add_apartment_details()
    else:
        apartment_name = apartment_name.title()
        ad.append(apartment_name)
        apartment_unit = input("Enter unit rented: ")
        ad.append(apartment_unit)
        apartment_date = optionvalid("Enter date of acquisition: ")
        ad.append(apartment_date)
        apartment_footage = optionvalid("Enter square footage: ")
        ad.append(apartment_footage)
        apartment_rent = optionvalid("Enter expected rent: ")
        ad.append(apartment_rent)
        apartment_history = input("Enter rental history: ")
        ad.append(apartment_history)
        apartment_details.append(ad)

    with open('apartment_file.txt', 'a') as apartment_file:
        for aad in apartment_details:
            apartment_file.write(f'{aad}\n')

    print("Apartment details added\n", apartment_details)

def view_apartment_details():
    print("Printing apartment details......")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apartment Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('apartment_file.txt', 'r') as apartment_file:
        number = 0
        for line in apartment_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(number, "details printed")

    while True:
        quit_key = input("Enter any key to leave. ")
        if quit_key == '0':
            print("Redirecting to Apartment Page...")
            break
        else:
            print("Redirecting to Apartment Page...")
            break

def search_apartment_details():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apartment Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('apartment_file.txt', 'r') as apartment_file:
        number = 0
        printed = 0
        search_key = input("Details to search: ")
        print("Searching details consists of", search_key, "......")
        for line in apartment_file:
            line = line.rstrip()
            number += 1
            if not search_key.lower() in line.lower():
                continue
            print(number, ":", line)
            printed += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if printed >= 1:
            print(printed, "details found")
            apartment_search_decision()
        elif printed == 0:
            print("No result found")
            apartment_search_decision()
def apartment_search_decision():
    search_input = input("Search again? (Y/N) ")
    if search_input.upper() == "Y":
        search_apartment_details()
    elif search_input.upper() == "N":
        print("Redirecting to Apartment Page...")
    else:
        print("Invalid input")
        apartment_search_decision()

def modify_apartment_details():
    rowvalidate = False
    columnvalidate = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apartment Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('apartment_file.txt', 'r') as apartment_file:
        number = 0
        for line in apartment_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while not rowvalidate:
        row = optionvalid("Number of list to modify: ")
        row = int(row - 1)
        if row >= number or row < 0:
            print("Invalid number of list, please try again.")
        else:
            rowvalidate = True
            while not columnvalidate:
                column = optionvalid("Which column is it on? \n 1/2/3/4/5/6: ")
                column = int(column - 1)
                if column < 0 or column > 5:
                    print("Invalid column, please try again.")
                else:
                    columnvalidate = True
                    new = str(input("Change to: "))

    with open('apartment_file.txt', 'r+') as apartment_file:
        array = []
        for line in apartment_file:
            item = line.rstrip().split(", ")
            array.append(item)
        print("The details modified from ", array[row][column], "to ", new)
        a = "'"
        b = "["
        c = "]"
        if column > 0 and column < 5:
            array[row][column] = str(a + new + a)
        elif column == 0:
            array[row][column] = str(b + a + new + a)
        elif column == 5:
            array[row][column] = str(a + new + a + c)

    with open('apartment_file.txt', 'r+') as apartment_file:
        for line in array:
            y = 6
            x = 5
            for item in line:
                if y > 0:
                    apartment_file.write(item)
                    y = y - 1
                    if x > 0:
                        apartment_file.write(", ")
                        x = x - 1
                    else:
                        apartment_file.write("\n")
        print("Details updated")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apartment Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('apartment_file.txt', 'r') as apartment_file:
        number = 0
        for line in apartment_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        decision_input = input("Enter any key to skip.")
        if decision_input == 1:
            apartment_modify_decision()
        else:
            apartment_modify_decision()
def apartment_modify_decision():
    modify_input = input("Modify again? (Y/N) ")
    if modify_input.upper() == "Y":
        modify_apartment_details()
    elif modify_input.upper() == "N":
        print("Redirecting to Current Tenant Page...")
    else:
        print("Invalid input")
        apartment_modify_decision()

def delete_apartment_details():
    rowvalidate = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apartment Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('apartment_file.txt', 'r') as apartment_file:
        number = 0
        for line in apartment_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while not rowvalidate:
        row = optionvalid("Which row to delete: ")
        row = int(row - 1)
        if row >= number or row < 0:
            print("Invalid number of list, please try again.")
        else:
            rowvalidate = True
            delete_confirmation = input("Confirm proceed to delete details?\nOnly enter Y will proceed to. ")
            if delete_confirmation.upper() == "Y":
                with open('apartment_file.txt', 'r+') as apartment_file:
                    lines = apartment_file.readlines()
                    apartment_file.seek(0)
                    apartment_file.truncate()
                    for number, line in enumerate(lines):
                        if number not in [row]:
                            apartment_file.write(line)
                    print("Details updated")
            else:
                print("Delete action has cancelled.")
                return

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apartment Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open('apartment_file.txt', 'r') as apartment_file:
        number = 0
        for line in apartment_file:
            line = line.rstrip()
            number += 1
            print(number, ":", line)
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        quit_key = input("Enter any key to leave. ")
        if quit_key == '0':
            print("Redirecting to Apartment Page...")
            break
        else:
            print("Redirecting to Apartment Page...")
            break


def log():
    admin_log = []
    with open('admin_log_file.txt', 'r+') as admin_log_file:
        for admin_print in admin_log_file:
            end_time = round(time.time())
            end_time = str(end_time)
        print("\nTime ended at:", end_time)
        admin_log.append(end_time)
        admin_log = str(admin_log)
        admin_log_file.write(admin_log)
        admin_log_file.write("\n")
        menu()

def tenant_page():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Tenant Page~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Current tenant details")
    print("2. Past tenant details")
    print("3. Apartment details")
    print("4. Back")
    option = optionvalid("Choose to access: ")
    if option == 1:
        tenant_current_tenant_details()
    elif option == 2:
        tenant_past_tenant_details()
    elif option == 3:
        tenant_apartment_details()
    elif option == 4:
        print("Redirecting to Main Menu...")
        menu()
    else:
        print("Invalid option, please try again!")
        tenant_page()

def management_page():
    print("~~~~~~~~~~~~~~~~~~~~~Management Page~~~~~~~~~~~~~~~~~~~~~")
    print("1. Current tenant details")
    print("2. Past tenant details")
    print("3. Apartment details")
    print("4. Logout")
    option = optionvalid("Choose to access: ")
    if option == 1:
        management_current_tenant_details()
    elif option == 2:
        management_past_tenant_details()
    elif option == 3:
        management_apartment_details()
    elif option == 4:
        print("Redirecting to Main Menu...")
        log()
    else:
        print("Invalid option, please try again!")
        management_page()

def login_page():
    admin_log = []
    with open('admin_log_file.txt', 'a') as admin_log_file:
        print("~~~~~~~~~~~~~~~~~~~~~Login Page~~~~~~~~~~~~~~~~~~~~~")
        Un = input("Enter Username: ")
        Pw = input("Enter Password: ")
        if Un == "David":
            if Pw == "David@123":
                print("\nWelcome David")
                start_time = int(time.time())
                start_time = round(start_time)
                start_time = str(start_time)
                print('Time started at:', start_time, '\n')
                admin_log.append(Un)
                admin_log = str(admin_log)
                admin_log_file.write(admin_log)
                admin_log_file.close()
                with open('admin_log_file.txt', 'a') as admin_log_file:
                    admin_log = []
                    admin_log.append(start_time)
                    admin_log = str(admin_log)
                    admin_log_file.write(admin_log)
                    admin_log_file.close()
                    management_page()
            else:
                print("ID or Password Incorrect, please try again!")
                menu()
        elif Un == "John":
            if Pw == "JohnAdmin":
                print("\nWelcome John")
                start_time = int(time.time())
                start_time = round(start_time)
                start_time = str(start_time)
                print('Time started at:', start_time, '\n')
                admin_log.append(Un)
                admin_log = str(admin_log)
                admin_log_file.write(admin_log)
                admin_log_file.close()
                with open('admin_log_file.txt', 'a') as admin_log_file:
                    admin_log = []
                    admin_log.append(start_time)
                    admin_log = str(admin_log)
                    admin_log_file.write(admin_log)
                    admin_log_file.close()
                    management_page()
            else:
                print("ID or Password Incorrect, please try again!")
                menu()
        else:
            print("ID or Password Incorrect, please try again!")
            menu()

def menu():
    print("~~~~~~~~~~~~~~~~~~~~~Welcome to Main Menu~~~~~~~~~~~~~~~~~~~~~")
    print("1. Tenant")
    print("2. Management")
    print("3. Quit")
    user_option = optionvalid("Enter option: ")

    if user_option == 1:
        tenant_page()
    elif user_option == 2:
        login_page()
    elif user_option == 3:
        print("Closing application......")
        exit()
    else:
        print("Invalid option,please try again.")
        menu()


def optionvalid(optionmessage):
    while True:
        try:
            option_input = int(input(optionmessage))
        except ValueError:
            print("Input not an integer. Please try again. ")
            continue
        else:
            return option_input


def tenant_current_tenant_details():
    print("\nTenant Mode\n~~~~~~~~~~You are currently on Current Tenant Page~~~~~~~~~~")
    print("1. View details")
    print("2. Add details")
    print("3. Search details")
    print("4. Back")
    while True:
        tenant_current_option = optionvalid("Enter option: ")
        if tenant_current_option == 1:
            view_current_tenant_details()
            tenant_current_tenant_details()
        elif tenant_current_option == 2:
            add_current_tenant_details()
            tenant_current_tenant_details()
        elif tenant_current_option == 3:
            search_current_tenant_details()
            tenant_current_tenant_details()
        elif tenant_current_option == 4:
            tenant_page()
        else:
            print("Invalid input. Please try again. ")
            tenant_current_tenant_details()

def management_current_tenant_details():
    print("\nManagement mode\n~~~~~~~~~~~~~~~~~~~~~You are currently on Current Tenant Page~~~~~~~~~~~~~~~~~~~~~")
    print("1. View details")
    print("2. Add details")
    print("3. Search details")
    print("4. Modify details")
    print("5. Delete details")
    print("6. Back")
    while True:
        tenant_current_option = optionvalid("Enter option: ")
        if tenant_current_option == 1:
            view_current_tenant_details()
            management_current_tenant_details()
        elif tenant_current_option == 2:
            add_current_tenant_details()
            management_current_tenant_details()
        elif tenant_current_option == 3:
            search_current_tenant_details()
            management_current_tenant_details()
        elif tenant_current_option == 4:
            modify_current_tenant_details()
            management_current_tenant_details()
        elif tenant_current_option == 5:
            delete_current_tenant_details()
            management_current_tenant_details()
        elif tenant_current_option == 6:
            management_page()
        else:
            print("Invalid input. Please try again. ")
            management_current_tenant_details()

def tenant_past_tenant_details():
    print("\nTenant Mode\n~~~~~~~~~~~~~~~~~~~~~You are currently on Past Tenant Page~~~~~~~~~~~~~~~~~~~~~")
    print("1. View details")
    print("2. Search details")
    print("3. Exit")
    while True:
        tenant_past_option = optionvalid("Enter option: ")
        if tenant_past_option == 1:
            view_past_tenant_details()
            tenant_past_tenant_details()
        elif tenant_past_option == 2:
            search_past_tenant_details()
            tenant_past_tenant_details()
        elif tenant_past_option == 3:
            menu()
        else:
            print("Invalid input. Please try again. ")
            tenant_past_tenant_details()

def management_past_tenant_details():
    print("\nManagement Mode\n~~~~~~~~~~~~~~~~~~~~~You are currently on Past Tenant Page~~~~~~~~~~~~~~~~~~~~~")
    print("1. View details")
    print("2. Add details")
    print("3. Search details")
    print("4. Modify details")
    print("5. Delete details")
    print("6. Exit")
    while True:
        tenant_past_option = optionvalid("Enter option: ")
        if tenant_past_option == 1:
            view_past_tenant_details()
            management_past_tenant_details()
        elif tenant_past_option == 2:
            add_past_tenant_details()
            management_past_tenant_details()
        elif tenant_past_option == 3:
            search_past_tenant_details()
            management_past_tenant_details()
        elif tenant_past_option == 4:
            modify_past_tenant_details()
            management_past_tenant_details()
        elif tenant_past_option == 5:
            delete_past_tenant_details()
            management_past_tenant_details()
        elif tenant_past_option == 6:
            management_page()
        else:
            print("Invalid input. Please try again. ")
            management_past_tenant_details()

def tenant_apartment_details():
    print("\nTenant Mode\n~~~~~~~~~~~~~~~~~~~~~You are currently on Apartment Page~~~~~~~~~~~~~~~~~~~~~")
    print("1. View details")
    print("2. Search details")
    print("3. Exit")
    while True:
        apartment_option = optionvalid("Enter option: ")
        if apartment_option == 1:
            view_apartment_details()
            tenant_apartment_details()
        elif apartment_option == 2:
            search_apartment_details()
            tenant_apartment_details()
        elif apartment_option == 3:
            tenant_page()
        else:
            print("Invalid input. Please try again. ")
            tenant_apartment_details()

def management_apartment_details():
    print("\nManagement Mode\n~~~~~~~~~~~~~~~~~~~~~You are currently on Apartment Page~~~~~~~~~~~~~~~~~~~~~")
    print("1. View details")
    print("2. Add details")
    print("3. Search details")
    print("4. Modify details")
    print("5. Delete details")
    print("6. Exit")
    while True:
        apartment_option = optionvalid("Enter option: ")
        if apartment_option == 1:
            view_apartment_details()
            management_apartment_details()
        elif apartment_option == 2:
            add_apartment_details()
            management_apartment_details()
        elif apartment_option == 3:
            search_apartment_details()
            management_apartment_details()
        elif apartment_option == 4:
            modify_apartment_details()
            management_apartment_details()
        elif apartment_option == 5:
            delete_apartment_details()
            management_apartment_details()
        elif apartment_option == 6:
            management_page()
        else:
            print("Invalid input. Please try again. ")
            management_apartment_details()



menu()