################### 1-.عددی را دریافت کرده و اعداد کوچکتر از آن را چاپ کند.
# myList = []
# for _ in range(3):
#     user_input = int(input("Please input a number: "))
#     myList.append(user_input)


# smallest = myList[0]
# biggest = myList[0]

# for x in myList: 
#     if(x < smallest): 
#         smallest = x
#     elif x > biggest:
#         biggest = x
# print(f"The biggest inputed number is: ", {biggest}, " and the smallest number is ", {smallest})

##################عددی رو دریافت کرده و مقسوم علیه های آن را چاپ کند.
# user_i = int(input("Please enter a number: "))
# for x in range(1, user_i):
#     if(user_i%x == 0):
#         print(x)

##########################عددی رو دریافت کرده و تشخیص دهد عدد اول هست یا نه؟
# flag = True
# user_i = int(input("Please enter a number: "))
# for x in range(2, user_i-1):
#     if(user_i%x == 0):
#         flag = False

# if flag: 
#     print (f"{user_i} is a primitive number")
# else:
#     print(f"{user_i} is not primitive! ")

######.عددی رو دریافت کرده و اعداد زوج کوچکتر از آن را چاپ کند.
# user_i = int(input("Please enter a number: "))
# print(f"The even numbers up to {user_i} are: ")
# for x in range(0,user_i,2):
#     print(x)

# #####.عددی رو دریافت کرده و اعداد زوج دورقمی کوچکتر از آن را چاپ کند.
# user_i = int(input("Please enter a number: "))
# print(f"The even numbers up to {user_i} are: ")
# for x in range(0,user_i,2):
#     if x > 9:
#      print(x)

#########.عددی رو دریافت کرده و اعداد اول کوچکتر از آن را چاپ کند.
# def is_prime(num):
#     flag = True
#     if num < 2: flag = False
#     for x in range(2, num-1):
#         if(num % x == 0):
#             flag = False
#             break
#     return flag
# user_i = int(input("Please enter a number: "))
# prime_check = bool()
# print(f"The prime numbers up to {user_i} are: ")
# for z in range(1, user_i):
#     prime_check = is_prime(z)
#     if prime_check == True: 
#         print(z)


#############.دو عدد رو دریافت کرده و مقسوم علیه مشترک شأن را چاپ کند
# def reminder_add(num):
#     reminders = []
#     for x in range(1, num+1):
#         if(num % x == 0):
#            reminders.append(x)
#     return reminders

# first_num = int(input("Please enter the first number: "))
# second_num = int(input("Please enter the second number: "))

# reminders_first = reminder_add(first_num)
# reminders_second = reminder_add(second_num)
# commens = []
# for i in reminders_first:
#     for r in reminders_second:
#         if(i == r):
#             commens.append(i)

# print(commens)


###########.دو عدد رو دریافت کرده و با انتخاب کاربر اعداد زوج و یا فرد بین دو عدد را چاپ کند.
# def calc_odd(num1, num2):
#     numberList = []
#     for x in range(num1-1, num2, 2):
#        if(x>num1):
#            numberList.append(x)
#     return numberList

# def calc_even(num1, num2):
#     number = num2 - num1
#     numberList = []
#     for x in range(num1 , num2, 2):
#        numberList.append(x)
#     return numberList

# first_num = int(input("Please enter the first number: "))
# second_num = int(input("Please enter the second number: "))
# choice = int(input("Enter 1 for Odd numebrs and 2 for Even numbers between the two numbers: "))
# numList = []
# if(choice == 1):
#     numList = calc_odd(first_num,second_num)
#     print(f"the odd number between {first_num} and {second_num} are: {numList}")
# elif(choice == 2):
#     numList = calc_even(first_num,second_num)
#     print(f"the even number between {first_num} and {second_num} are: {numList}")

#########.تعدادی عدد از کاربر دریافت کرده و بزرگترین و مجموع  آنها را چاپ کند(دقت کنید محدودیتی برای تعداد در نظر گرفته نشده و می تونید مثلا عدد صفر  و یا ۰۱ رو پایان ورود اعداد دریافتی قرار دهید)
num = 1
numberList = []
biggest = 0
while num != 0:
    num = int(input("Please enter a number (ENTER 0 to stop): "))
    numberList.append(num)  
    biggest = numberList[0]
    for x in numberList:
        if(x > biggest):
            biggest = x
    print(f"{biggest} IS SO FAR THE BIGGEST")

print(f"{biggest} IS THE BIGGEST")