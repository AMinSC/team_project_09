def chicken(x):
    if x == 0: return 0
    if x == 1: return 1
    a,b = 1,1
    while 1:
        c = a+b
        if c > x: return a + chicken(x-b)
        elif c == x: return b
        a, b = b, c

num = int(input('같이 먹는 사람 수: '))
print('시켜야 되는 샐러드 양은: {}'.format(chicken(num)))
print('맥주: {}ml'.format(num * 400))

