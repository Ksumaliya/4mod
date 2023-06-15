def poll(string: str):                      # Функция, которая ищет полиндром, принимает только строковый объект string
    counter = 0                             # Счетчик, сколько раз совпали противоположные символы в строке string

    for sym in range(len(string)):          # Повторяем проверку столько раз, сколько символов в строке string

        if string[sym] == string[-sym-1]:   # Если n-ный символ строки string слева равен n-ному символу строки string справа,
            counter += 1                    # то прибавляем это совпадение к счетчику counter
            
        else:                               # Иначе это уже не полиндром,
            print(False)                    # сразу выводим False,
            break                           # дальше проверять нет смысла

        if counter == len(string):          # Когда счетчик counter сравнялся с длиной строки string, т.е. все символы совпали,
            print(True)                     # значит был введен полиндром, выводим True
            break                           # и заканчиваем цикл

s = input('Введите строку: ')        # "На вход подается строка,
s_l = s.lower()                      # все символы находятся в нижнем регистре 
s_fin = s_l.replace(' ', '')         # и без пробелов"

poll(s_fin)                     # Запуск функции poll