# coding=utf-8
def iseven(value): return value % 2 == 0
# Стандартное исполнение, лекго узнаваемый код, работает только с типом int


def iseven_with_and(value):
    return value & 1 == 0
# Проверяет младший бит числа, это редкое исполнение, работает только с типом int


def iseven_with_str(value):
    return str(value)[-1] in ("0", "2", "4", "6", "8")
# Проверяет четность с помощью среза строки, может работать с int, float, str типами
