connect = True

while connect == True:
    number = input("Число: ")
    procent = input("Процент: ")
    while type(number) != int:
        try:
            number = int(number)
            procent = int(procent)

        except ValueError:
            print("Вводи целочисленные значения!")
            number = input("Число: ")
            procent = input("Процент: ")

    while type(procent)!= float:
         try:
            number = float(number)
            procent = float(procent)

         except VaLueError:
            print("Вводи целочисленные значения")
            number = input("Число: ")
            procent = input("Процент: ")


    finish = number / 100 * procent
    print("Ваш ответ: ", float(finish))


             
