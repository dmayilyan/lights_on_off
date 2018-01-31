#!/usr/bin/env python3
import random


def light_on_off(number):
    print(format(number, '08b'))
    print('')
    for j in range(8):
        if j == 7:
            mask = 3
            j = 6
        elif j == 0:
            mask = 3
            j = 0
        else:
            mask = 7
            j -= 1
        # i -= 1
        qwe = (mask << j)
        number = number ^ qwe
        print(format(qwe, '08b'), format(number, '08b'))
    print('')
    print(format(number, '08b'))
    return number


def do_xor(j, number):
    if j == 7:
        mask = 3
        j = 6
    elif j == 0:
        mask = 3
        j = 0
    else:
        mask = 7
        j -= 1
    qwe = (mask << j)

    return number ^ qwe


def get_comb(n):
    '''
    Get combination that leads to all lights off.
    '''
    for i in range(200):
        number = n
        rand_mask_pos = [i for i in range(8)]
        print('\nResetting to 106')
        while len(rand_mask_pos) != 1:
            loc_key = random.sample(rand_mask_pos, 1)
            print(loc_key[0], end=', ')
            number = do_xor(loc_key[0], number)
            if number == 0:
                print('')
                print(format(number, '08b'))
                print('Here is it!')
                break
            loc_key = rand_mask_pos.remove(loc_key[0])


def main():
    number = 104
    print(format(number, '08b'))
    print('')

    light_on_off(number)

    get_comb(number)


if __name__ == '__main__':
    main()
