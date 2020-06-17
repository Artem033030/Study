def run():
    a = 150
    b = get_b(a)
    c = get_c(a,b)
    d = get_d(a,b,c)
    e = get_e(a,b,c,d)
    return e
run()


def death():
    e = 0
    ress = []
    while True:
        e +=100000000000000000000
        ress.append(e)
        print(ress)
        print(e)


if __name__ == '__main__':
    death()
