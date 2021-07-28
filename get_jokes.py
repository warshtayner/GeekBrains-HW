from random import randrange, choice



def get_jokes(n, repeat=False):
    """
    Creates random jokes

    :param n: the numbers of jokes
    :param repeat: the flag of repeat jokes
    :return: jokes in the form of a list
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом", "шышка"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "где то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "чекнутый"]

    res = []
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    min_list = min(no, adv, adj)

    while n and len(min_list):
        i = randrange(len(min_list))
        if repeat:
            res.append(f'{no.pop(i)} {adv.pop(i)} {adj.pop(i)}')
        else:
            res.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1

    return res

print(get_jokes(15, True))