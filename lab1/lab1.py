#Замена текстовых подстрок в файле (реализовать программу, заменяющую слова из черного списка на звездочки,
#  вход файл черного списка, по одному слову в строке и файл текста, в котором делаются замены).
#b. * Каждая строка в файле списка имеет вид имя: значение, и при замене строки “имя” используются не звездочки,
#  а соответствующие значения из файла списка.

from datetime import datetime

#функция замены текстовых подстрок в файле
def repSub(black_list_file, source_file):
    # словарь содержащий слова для замены (слово:новое значение)
    blacklist = {}

    # заполнение словаря blacklist из файла
    for str in open(black_list_file):
        str = str.split('\n')
        str = str[0]  # удаление символа переноса
        str = str.split(':')  # разделение на имя и значение

        blacklist[str[0]] = str[1]  # добавление в словарь

    #открытие запись из файла исходного текста
    file= open(source_file)
    textarr = []
    for str in file:
        textarr.append(str)
    file.close()

    # замена слов в тексте на новые слова
    for x in range(0, len(textarr)):
        if x % 1000 is 0:
            print(x)
            arr = textarr[x].split(" ")
            for y in range(0, len(arr)):
                for key in blacklist:
                    if arr[y] == key:
                        arr[y] = blacklist[key]
            newline = " ".join(arr)
            textarr[x] = newline

    #открытие файла для записи изменённого текста
    file=open(source_file, 'w')
    file.writelines(textarr)
    file.close()

start = datetime.now()
repSub('files/replaces.txt','files/test.txt')
end = datetime.now()
time=((end - start))

#вывод результатов работы функции(время)
print(time)
