import os
import datetime


def add_new(filename:str):
    id_name = input("Введите идентификатор заметки :")
    name = input("Введите заголовок заметки :")
    body = input("Введите текст заметки :")
    dt = datetime.datetime.now()
    with open (filename, 'a', encoding="utf-8") as fd :
        fd.write (f'{id_name}, {name}, {body}, {dt}\n')

def show_all(filename : str):
    with open(filename , 'r', encoding ="utf-8") as fd:
        data = fd.read()
        print (data)

def remove_1(filename :str):
    del_data = find_by_attribute(filename, True)
    print (del_data)
    with open(filename, 'r', encoding ="utf-8") as f :
        data = f.readlines()
        # s= data.index (del_data)
        data.remove(del_data)
    with open (filename,'w', encoding ="utf-8") as f :
        f.writelines(data)

def correct_1(filename :str):
    old_data = find_by_attribute(filename, True)
    print ("Введите новые данные :")
    id_name_ = input ("Введите id :")
    name_ = input ("Введите заголовок :")
    body = input ("Введите текст :")
    dt = datetime.datetime.now()
    with open(filename, 'r', encoding ="utf-8") as f :
        data = f.readlines()
        s = data.index (old_data)
        data[s] = f'{id_name_}, {name_}, {body}, {dt}\n'
    with open (filename,'w', encoding ="utf-8") as f :
        f.writelines(data)

def main():
    os.system ("cls")
    Flag_Exit = False
    while Flag_Exit==False:
        print ( "1 Добавление новой записи")
        print ( "2 Вывести все записи")
        print ( "3 Удалить запись")
        print ( "4 Изменить запись")
        print ( "5 Поиск по id\заголовку")
        a = input("Введите операцию или x для выхода :")  
        if a == "1" : add_new("Notes.txt")
        elif a == "2" : show_all("Notes.txt")
        elif a == "3" : remove_1("Notes.txt")
        elif a == "4" : correct_1("Notes.txt")
        elif a == "5" : find_by_attribute("Notes.txt", False)
        elif a =="x" : Flag_Exit=True

def find_by_attribute (filename :str, option:bool ):
    op=0
    c=input ("Введите 1 для поиска по id или 2 для поиска по заголовку :\n")
    print ("")
    if c=='1' :op=0
    elif c=='2' : op=1
    attr = input("Введите id/заголовок \n ")
    print ("")
    with open(filename, 'r',encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[op]== attr,data))
        result = (list(zip (range(1,len(data)+1),data)))
        if result == [] : 
            print ("                  Такой записи нет в справочнике")
            print (" ")
            return  
        else :
            
            for idx, val in enumerate(data):
                if attr in val: print (f' {idx} {val}' )
            
        if option:
            id=int ( input ("Введите индекс выбранной записи "))
            return data[id-1]



if __name__ == '__main__':        
    main()


    