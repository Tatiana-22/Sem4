#2.Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
#где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление. 
#reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

names = ['rev', 'acc', 'stroka']
vals = [True, "YES", 4]

def form_dict(name_list, val_list):
    new_dict = {}
    for name, val in zip(name_list, val_list):
        try:
            new_dict[val] = name
        except TypeError:
            new_dict[str(val)] = name
    return new_dict

print(form_dict(names, vals))



