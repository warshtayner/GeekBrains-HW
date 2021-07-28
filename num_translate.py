
def  num_translate(num):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два',
                'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

    return(num_dict.get(num))

print(num_translate(input('Enter any number: ')))