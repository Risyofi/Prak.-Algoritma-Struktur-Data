def gambarPersegiEmpat(a, b):
    for i in range(a):
        if i == 0 or i == a - 1:
            print('*' * b)
        else:
            print('*' + ' ' * (b-2) + '*')

gambarPersegiEmpat(4,5)