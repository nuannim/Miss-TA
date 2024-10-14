def main():
    number = int(input('Enter number of student: '))
    ta_number = 0
    if 20 >= number:
        ta_number = 0
    elif 35 >= number >= 21:
        ta_number = 1
    elif 50 >= number >= 36:
        ta_number = 2
    elif 65 >= number >= 51:
        ta_number = 3
    elif 80 >= number >= 66:
        ta_number = 4
    elif number > 80:
        ta_number = 4
        for i in range(int((number-80)/15)):
            ta_number += 1
    print(ta_number)
main()