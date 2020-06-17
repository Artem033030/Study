'''get_b:
делит аргумент на 3 и возвращает результат
get_c:
вызывает get_b с аргументом b,
умножает результат на b, делит результат на 4 и возвращает результат
get_d:
 вызывает get_с с аргументами b,c и  get_c с аргументом а. Результат вызова двух функций умножает на 100 и возвращает результат
get_e:
вызывает функцию get_c с аргументами а, b и get_c  аргументами c and d.
 Результаты вызова функций передает в get_c, результат делит на а и возвращет число, которое получилось'''

def get_b(a):
    b = a/3
    return b
def get_c(b):
    a = get_b(b)
    c = b*a
    n = c/4
    return n
def get_d(a,b):
    aa = get_c(b)
    bb = get_c(a)
    cc = aa+bb
    dd = cc*100
    return dd
def get_e(a,b):
    aaa = get_c(b)
    bbb = get_d(a,aaa)
    c = aaa/bbb
    return c






def run():
    a = 150
    b = get_b(a)
    c = get_c(a)
    d = get_d(a,c)
    e = get_e(d,b)
    return e
run()
