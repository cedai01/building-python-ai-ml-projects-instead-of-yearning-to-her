def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(1))



def repeat_worod(n, text):
    return text * n

print(repeat_worod(3, "nigga"))


def sum_list(list):
        total = 0
        for num in list:
            total += num
        return total

print(sum_list([1,5,6,2,8,5,6,2]))


def reversed_word(words):
    return words[:: -1]
    

print(reversed_word("Nigga"))