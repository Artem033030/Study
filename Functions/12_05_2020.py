from Functions.h_12_5_20 import (check_three)
from Functions.h_3 import (check_five)
from Functions.h_7 import (check_seven)


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
