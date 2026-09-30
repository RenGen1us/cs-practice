limit = int(input())
n = int(input())
c = ce = cl = cs = s = 0
mx = -1000000000500000000
for i in range(n):
    a = input()
    c += 1
    if a == 'error':
        ce += 1
    if a != 'error':
        if float(a) > limit:
            cl += 1
        mx = max(mx, float(a))
        cs += 1
        s += float(a)
print(c)
print(ce)
print(cl)
print(mx)
print(f'{s / cs:.1f}')

    


