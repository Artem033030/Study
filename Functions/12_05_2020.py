def check_odd(first):
    # если чесло делиться на два без остачи то
    check_three()
    check_five()
    check_seven()

    if first % 2 == 0:
        #
        return "Yes,it's odd"
    else:
        result = "Not odd"
        if check_three(first):
            result += "end divided by three"
        else:
            result += "end not divided by three"

        return result



