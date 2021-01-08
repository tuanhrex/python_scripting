hello_file = open("hello.txt", "w")
ga_intro = " Hello GA"
hello_file.write(ga_intro)
# print(hello_file.read())

hello_file.close()

car_file = open("car.txt", "w")
new_car_list = 'BMW M3\nBMW M5\nAudi R8'
car_file.write(new_car_list)
# print(car_file.read())
car_file.close()

# Create a file
# my_new_file = open('person.txt', 'r+')
# my_new_file.write('Tu Anh Huynh')
# print(my_new_file.read())
# my_new_file.close()

# person_file = open('person.txt')
# print(person_file.read())
# person_file.close()

# with open('person.txt', 'w') as person_file:
#     person_file.write('Tron')

# # append
# with open('person.txt', 'a') as person_file:
#     person_file.write('\nTron\nTron')
#     print(person_file.read())


# with open('person.txt') as people:
#     people_list = people.readlines()

#     for each_person in people_list:
#         print(each_person)

# with open('prime_numbers.txt') as numbers:
#     numbers_list = numbers.readlines()

#     for each_number in numbers_list:
#         multiply = int(each_number) * 2
#         print(multiply)

with open('hundred.txt') as text:
    text_list = text.readlines()

    five = []
    for each_text in text_list:
        if 'Five' in each_text or 'Fifteen' in each_text:
            five.append(each_text[:-1])
    print(five)
