import random

S_BOX_5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
           14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
           4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
           11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

S_BOX_LINEAR = []

S_BOX_RANDOM = []

S_BOX_DEFINE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def precompute():
    global S_BOX_LINEAR, S_BOX_RANDOM

    S_BOX_LINEAR = []
    S_BOX_RANDOM = []
    for i in range(64):
        S_BOX_LINEAR.append(i + 1)
        S_BOX_RANDOM.append(random.randint(0, 15))


def get_s_box_by_index(index, s_box = S_BOX_5):
    b = [0] * 6
    n = index
    for i in range(6):
        b[5-i] = n % 2
        n //= 2
    return s_box[(b[0]*2 + b[5])*16 + b[1]*8 + b[2]*4 + b[3]*2 + b[4]]


def calculate_dif(arg):
    global S_BOX_LINEAR, S_BOX_RANDOM, S_BOX_5, S_BOX_DEFINE
    if arg == 0:
        __s_box = S_BOX_5
    elif arg == 1:
        __s_box = S_BOX_LINEAR
    elif arg == 2:
        __s_box = S_BOX_RANDOM
    else:
        __s_box = S_BOX_DEFINE

    dif_tab = [[0 for col in range(16)] for row in range(64)]
    for i in range(64):
        for j in range(64):
            in_dif = i ^ j
            out_dif = get_s_box_by_index(i, __s_box) ^ get_s_box_by_index(j, __s_box)
            dif_tab[in_dif][out_dif] += 1
    return dif_tab


def main(arg=0):
    precompute()
    __dif_tab = calculate_dif(arg)
    for i in range(len(__dif_tab)):
        print(i, __dif_tab[i])


if __name__ == '__main__':
    main()