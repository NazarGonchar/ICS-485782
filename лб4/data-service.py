from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    remainder: str
    received: int

@dataclass
class MoveOfMainAssets:
    name: str
    code: int
    remainder: int
    received: int

type_array = []
type_array.append(TypeOfMainAssets(1001, "Програмно-апаратна організація комп'ютера IBM PC", "П. Нортон", 400))
type_array.append(TypeOfMainAssets(1002, "Посібник з експлуатації ПЕОМ IBM PC", "Р. Джордейн", 400))
type_array.append(TypeOfMainAssets(1003, "Операційна система MS DOS 3.3", "Р. Джордейн и др." , 700))
type_array.append(TypeOfMainAssets(1004, "Асемблер для IBM PC", "А. Абель", 400))
type_array.append(TypeOfMainAssets(1005, "Мова програмування С", "Керніган, Рітчі", 300))
type_array.append(TypeOfMainAssets(1006, "TURBO PASCAL для професіоналів", "Г. Шилдт", 650))

move_array = []
move_array.append(MoveOfMainAssets("КНТЕУ", 1101, 1001, 5))
move_array.append(MoveOfMainAssets("КНТЕУ", 1222, 1002, 5))
move_array.append(MoveOfMainAssets("КНТЕУ", 1029, 1003, 20))
move_array.append(MoveOfMainAssets("КНТЕУ", 1040, 1004, 5))
move_array.append(MoveOfMainAssets("КНТЕУ", 1050, 1005, 30))
move_array.append(MoveOfMainAssets("КНЕУ", 1100, 1006, 200))
move_array.append(MoveOfMainAssets("КНЕУ", 1101, 1001, 6))
move_array.append(MoveOfMainAssets("КНЕУ", 1222, 1002, 6))
move_array.append(MoveOfMainAssets("КНЕУ", 1029, 1003, 25))
move_array.append(MoveOfMainAssets("КНЕУ", 1040, 1004, 7))
move_array.append(MoveOfMainAssets("КНЕУ", 1050, 1005, 25))
move_array.append(MoveOfMainAssets("КНЕУ", 1100, 1006, 220))
move_array.append(MoveOfMainAssets("КНУ", 1101, 1001, 8))
move_array.append(MoveOfMainAssets("КНУ", 1222, 1002, 8))
move_array.append(MoveOfMainAssets("КНУ", 1029, 1003, 23))
move_array.append(MoveOfMainAssets("КНУ", 1040, 1004, 7))
move_array.append(MoveOfMainAssets("КНУ", 1050, 1005, 28))
move_array.append(MoveOfMainAssets("КНУ", 1100, 1006, 210))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Заявка на постачання товарів"
    with names and values'''

    print("Замовник: {name}, Код замовлення: {code}, Код товару: {remainder}, Кількість: {received}"
          .format(name=moveOfMainAssets.name, code=moveOfMainAssets.code, remainder=moveOfMainAssets.remainder,
                  received=moveOfMainAssets.received)) 
for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Довідник товарів"
    with names and values'''

    print("Код: {code}, Назва: {name}, Автор: {remainder}, Ціна: {received}"
        .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, remainder=typeOfMainAssets.remainder, received=typeOfMainAssets.received))

for data in type_array:
    printTypeOfMainAssets(data)