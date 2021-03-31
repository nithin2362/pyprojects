from random import randint, shuffle             # Imprting necessary modules


def getvalues(n):                               # Inputs values for custom password
    cap, small, char, num = 0, 0, 0, 0
    userdef = 0
    while userdef not in [1, 2]:
        if userdef != 0:
            print('Try again !')
        userdef = int(input('''
1. Random Password 
2. Get credentials from user 
    Choice: '''))
    if userdef == 2:
        while cap + small + char + num != n:
            if (cap, small, char, num) != (0, 0, 0, 0):
                print('Try again !')
            cap = int(input('\nUpper case letters: '))
            small = int(input('Lower case letters: '))
            num = int(input('Numbers: '))
            char = int(input('Special Characters: '))

    else:
        while sum([cap, small, char, num]) != n:
            cap = randint(1, n - 1)
            small = randint(1, n - 1)
            char = randint(1, n - 1)
            num = randint(1, n - 1)
        [char, num, small, cap] = sorted([cap, num, char, small])
    return cap, small, char, num


def password_generator(n):                                  # Generates the Password (Random or custom)
    if n == 0:
        raise RuntimeError('Password can\'t be of zero length !')

    (cap, small, char, num) = getvalues(n)
    cap_list = list(map(chr, list(range(65, 91))))
    small_list = list(map(chr, list(range(97, 123))))
    other_chars = ['!', '@', '#', '%', '^', '&', '*']
    num_list = list(map(str, range(0, 10)))
    count = int(input('\nHow many passwords to be generated ?: '))
    passwords = []
    for i in range(count):
        chars = []
        caps = []
        smalls = []
        nums = []
        for i in range(char):
            chars.append(other_chars[randint(0, 6)])
        for i in range(num):
            nums.append(num_list[randint(0, 9)])
        for i in range(small):
            smalls.append(small_list[randint(0, 25)])
        for i in range(cap):
            caps.append(cap_list[randint(0, 25)])
        pwd = caps + smalls + chars + nums
        randcnt = randint(3, 7)
        i = 0
        while not pwd[0].isalpha() or i < randcnt:
            shuffle(pwd)
            i += 1
        passwords.append(''.join(pwd))

    return passwords


if __name__ == '__main__':              
    n = int(input('Password Length: '))                 # Enter the length of the password
    pwds = password_generator(n)
    print('\nPassword(s): ', end='\n\t\t')
    for i in range(len(pwds)):
        print(f'{i + 1}. {pwds[i]}', end='\n\t\t')
