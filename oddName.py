"""Lee Jungwoo Practical 3"""
name_list = []
Number = int(input("How many people are you going to input?"))
for i in range(Number):
    valid_input = False
    name = input("Please, input the name")
    while valid_input == False:
        if " " in name:
            print("Do not input blank")
            name = input("Please, input the name")
        else:
            name_list.append(name)
            valid_input = True
for j in range(Number):
    print(name_list[j][1])