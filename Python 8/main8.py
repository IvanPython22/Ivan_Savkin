# nums = [1, 7, 3, 6, 5, 6]
# nums = [2, 1, -1]
#
# pivot = -1
# for i in range(len(nums)):
#     if sum(nums[:i]) == sum(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)

# import re   # библиотека для патернов

# text = 'milk how dogs python'

# match = re.search(r'\w{4}', text)    # ищет первое вхождение
# print(match.group())

# matches = re.findall(r'\w{4}\b', text)

# matches = re.findall(r'\s\w{4,}\b', text)
#
# print(matches)

# import re  # библиотека для патернов
#
# text = '1234 124 748 78 5 147'
#
# match = re.findall(r'\b\d{3}\d', text)
# print(match)

# dates = '10.12.2001 15/01/2004 14.02.14 18-05-2024'
# # match = re.findall(r'\d{2}\.\d{2}\.\d{4}', dates)    # лучше способ чем ниже
# match = re.findall(r'\d\d\.\d\d\.\d\d\d\d', dates)
# match_sub = re.sub(r'\d{2}\.\d{2}\.\d{4}', r'dd.mm.yyyy', dates)
# print(match_sub)

# text = 'Ivan, Bob; Maria, Petr'
#
# names = re.split(r'[,;]', ''.join(text.split()))    # джойном убираем проблемы между разделением строк
# print(names)


# tels = '+79999999999 +7 (999)999999 +7 (999)-999-9998 +7 (999)-999-99-78'
# corect_tel = re.findall(r'\+7 \(\d\d\d\)-\d\d\d-\d\d-\d\d', tels)
#
# print(corect_tel)
# import re
# email = 'testmail.ru test@mail.ru test123@mail.com test@mail!com'
# corect_email = re.findall(r'\w+@\w{2,20}\.[a-z]{2,3}', email)

print(corect_email)

# text = 'Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups.'
#
# text_1 = re.findall(r'\b\w{4}', text)
# text_1 = re.findall(r'\w+,', text)
# print(text_1)

# text = 'А578ВЕ77 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# text_1 = re.findall(r'[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2}', text)
# text_2 = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', text)
# print(text_1)
# print(text_2)

# import requests
#
# url = 'http://www.columbia.edu/~fdc/sample.html'
# response = requests.get(url)
#
# text = response.text
#
# headings = re.findall(r'<h3 id="\w*">(.*)</h3>', text)
# print(headings)

# text = '232'
# if re.match(r'\d{4}', text):
#     print('ok')
# print(re.match(r'\f{4}', text))


import re

# Dictionary to store information about employees
company = {}

# Function to validate phone numbers
def validate_phone(phone):
    pattern = r'^\+1\d{10}$'  # Example: +12345678901
    return re.match(pattern, phone)

# Function to validate email addresses
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to add employee information
def add_employee():
    full_name = input("Enter employee's full name: ")
    phone = input("Enter phone number: ")
    if not validate_phone(phone):
        print("Invalid phone number format. Please try again.")
        return
    email = input("Enter work email: ")
    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return
    job_title = input("Enter job title: ")
    office_number = input("Enter office number: ")
    skype = input("Enter Skype ID: ")

    company.setdefault(full_name, {
        'Phone': phone,
        'Email': email,
        'Job Title': job_title,
        'Office Number': office_number,
        'Skype': skype
    })
    print(f"Employee {full_name} added.")

# Function to delete employee information
def delete_employee():
    full_name = input("Enter the full name of the employee to delete: ")
    if full_name in company:
        del company[full_name]
        print(f"Information for employee {full_name} deleted.")
    else:
        print("Employee not found.")

# Function to search for employee information
def search_employee():
    full_name = input("Enter the full name of the employee to search for: ")
    if full_name in company:
        info = company[full_name]
        print("Employee information:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")

# Function to update employee information
def update_employee():
    full_name = input("Enter the full name of the employee to update information for: ")
    if full_name in company:
        print("Enter new information:")
        add_employee()
    else:
        print("Employee not found.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Search Employee")
    print("4. Update Employee Information")
    print("5. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        delete_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

