
def thesaurus(*args):
    res = {}
    for name in sorted(args):
        if name[0] in res:
            res[name[0]] += [name]
        else:
            res[name[0]] = [name]

    return res

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Игорь", "Кирил", "Вася", "Виктор"))
